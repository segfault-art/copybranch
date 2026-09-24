"""Branches' implementations."""

from typing import TYPE_CHECKING, override

from .error import GeneticError, ParentError

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import ClassVar, Never


class Branch:
    """Class for all branches."""

    _next_id: ClassVar[int] = 0

    def __init__(
        self, name: str | None = None, _parent: Branch | None = None, _version: int = 0
    ) -> None:
        """Initialize a branch with optional name."""
        self._parent = _parent
        self._children: list[Branch] = []
        self._version = _version
        self.name = name
        self._id = Branch._next_id

        Branch._next_id += 1

    @override
    def __repr__(self) -> str:
        return (
            f"Branch nº {self._id} "
            f"{f'"{self.name}"' if self.name is not None else ''} version {self._version}"
        )

    def __iter__(self) -> Iterator[Branch]:
        """Yield the child branches."""
        return iter(self._children)

    def walk(self) -> Iterator[Branch]:
        """Walk through all descendants."""
        for child in self._children:
            yield from child.walk()

        yield self

    def history(self) -> Iterator[Branch]:
        """Walk through all the ascendants."""
        yield self

        if self.parent is not None:
            yield from self.parent.history()

    def new_child(self, name: str | None = None) -> Branch:
        """Create a new child branch with optional name given."""
        child = Branch(name, self, self._version)
        self._children.append(child)

        return child

    def update(self) -> None:
        """Manually update the branch's version."""
        self._version += 1

    def first_parent(self) -> Branch:
        """Search branch's first parent."""
        if self._parent is None:
            return self

        return self._parent.first_parent()

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
        """The current branch's version."""
        return self._version


class MergeBranch(Branch):
    """Class for merge branches."""

    def __init__(self, version: int, *parents: Branch, name: str | None = None) -> None:
        """Initialize a merge branch with version, parents and optional name given."""
        self._parents = parents
        self._version = version
        self.name = name
        self._children = []
        self._id = Branch._next_id

        Branch._next_id += 1

    @override
    def __repr__(self) -> str:
        return (
            f"Merge branch nº {self._id} "
            f"{f'"{self.name}"' if self.name is not None else ''} version {self._version}"
        )

    @override
    def history(self) -> Iterator[Branch]:
        yield self

        for parent in self._parents:
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
        first_parent = None

        for parent in self._parents:
            current_first_parent = parent.first_parent()

            if first_parent is not None and current_first_parent != first_parent:
                raise GeneticError(
                    "Merge branch parents have different families. "
                    "Cannot determinate the first parent"
                )

            if first_parent is None:
                first_parent = current_first_parent

        if first_parent is None:
            raise ParentError("A merge branch must have 2 or more parents")

        return first_parent

    @property
    @override
    def parent(self) -> Never:
        """ALWAYS RAISES A ParentError. A merged branch has more than one parent."""
        raise ParentError("A merge branch have more than 1 parent")

    @property
    def parents(self) -> tuple[Branch, ...]:
        """The branch's parents."""
        return self._parents
