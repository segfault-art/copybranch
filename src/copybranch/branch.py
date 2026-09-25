"""Branches' implementations."""

from typing import TYPE_CHECKING, override
from warnings import deprecated

from copybranch.family import Family

from .error import GeneticError, ParentError

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import ClassVar, Never


class Branch:
    """Class for all branches. Represents a branch."""

    _next_id: ClassVar[int] = 0

    def __init__(
        self,
        name: str | None = None,
        _parent: Branch | None = None,
        _version: int = 0,
        _family: Family | None = None,
    ) -> None:
        """Initialize a branch with optional name."""
        self._parent = _parent
        self._children: list[Branch] = []
        self._version = _version
        self.name = name
        self._id = Branch._next_id

        Branch._next_id += 1

        if _family is None:
            self._family = Family()

        else:
            self._family = _family

    @override
    def __repr__(self) -> str:
        """Represent a Branch."""
        return (
            f'Branch nº {self._id} "{self.name}" '
            if self.name is not None
            else f"version {self.version} family {self.family}"
        )

    def __iter__(self) -> Iterator[Branch]:
        """Yield the child branches."""
        return iter(self.children)

    def walk(self) -> Iterator[Branch]:
        """Walk through all descendants."""
        for child in self.children:
            yield from child.walk()

        yield self

    def history(self) -> Iterator[Branch]:
        """Walk through all the ascendants."""
        yield self

        if self.parent is not None:
            yield from self.parent.history()

    def new_child(self, name: str | None = None) -> Branch:
        """Create a new child branch with optional name given."""
        child = Branch(name, self, self.version, self.family)
        self.children.append(child)

        return child

    def update(self) -> None:
        """Manually update the branch's version."""
        self._version += 1

    def first_parent(self) -> Branch:
        """Search branch's first parent."""
        if self.parent is None:
            return self

        return self.parent.first_parent()

    @deprecated(
        "copy_children is deprecated and scheduled for removal in a future version."
        "Because bugs rationed with genetic and parents",
        stacklevel=2,
    )
    def copy_children(self, parent: Branch) -> None:
        """Copy branch's children to a new branch."""
        parent._children.extend(self._children)

    @property
    def parent(self) -> Branch | None:
        """The branch's parent."""
        return self._parent

    @property
    def children(self) -> list[Branch]:
        """The branch's children."""
        return self._children

    @property
    def version(self) -> int:
        """The branch's version."""
        return self._version

    @property
    def family(self) -> Family:
        """The branch's family."""
        return self._family


class MergeBranch(Branch):
    """Class for merge branches."""

    def __init__(
        self,
        version: int,
        *parents: Branch,
        name: str | None = None,
        family_name: str | None = None,
    ) -> None:
        """Initialize a merge branch with version, parents and optional name given."""
        self._parents = parents
        self._version = version
        self.name = name
        self._children = []
        self._family = Family(family_name, *(p.family for p in parents))
        self._id = Branch._next_id

        Branch._next_id += 1

    @override
    def __repr__(self) -> str:
        return (
            f'Merge branch nº {self._id} "{self.name} "'
            if self.name is not None
            else f"version {self.version} family {self.family}"
        )

    @override
    def history(self) -> Iterator[Branch]:
        yield self

        for parent in self.parents:
            yield from parent.history()

    @override
    def first_parent(self) -> Branch:
        """
        Search branch's first parent.

        Search the first parent of this branch.

        Raises:
            GeneticError: If merged branch parents have different families.
            ParentError: If merged branch has no parent.

        Returns:
            Branch's first parent.

        """
        if len(self.family._parents) > 1:
            raise GeneticError(
                "Cannot determinate the first parent in"
                "a MergeBranch with more than 1 family"
            )

        if not self.parents:
            raise ParentError(
                "Cannot determinate the first parent in a MergeBranch without parents"
            )

        return self.parents[0].first_parent()

    @property
    @override
    def parent(self) -> Never:
        """ALWAYS RAISES A ParentError. A MergeBranch can has more than 1 parent."""
        raise ParentError("A MergeBranch can has more than 1 parent.")

    @property
    def parents(self) -> tuple[Branch, ...]:
        """The branch's parents."""
        return self._parents
