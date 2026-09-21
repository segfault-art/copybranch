from typing import TYPE_CHECKING, override

from .error import GeneticError, ParentError

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import ClassVar, Never

class Branch:
    _next_id: ClassVar[int] = 0

    def __init__(self, name: str | None = None, _parent: Branch | None = None, _version: int = 0) -> None:
        self._parent = _parent
        self._children: list[Branch] = []
        self._version = _version
        self.name = name
        self._id = Branch._next_id

        Branch._next_id += 1

    def __del__(self) -> None:
        if self._parent is not None:
            self._parent._children.remove(self)

    @override
    def __repr__(self) -> str:
        return f"Branch nº {self._id} {f'"{self.name}"' if self.name is not None else ""} version {self._version}"

    def __iter__(self) -> Iterator[Branch]:
        return iter(self._children)

    def walk(self) -> Iterator[Branch]:
        for child in self._children:
            yield from child.walk()

        yield self

    def history(self) -> Iterator[Branch]:
        yield self

        if self.parent is not None:
            yield from self.parent.history()

    def new_child(self, name: str | None = None) -> Branch:
        child = Branch(name, self, self._version)
        self._children.append(child)

        return child

    def update(self) -> None:
        self._version += 1

    def first_parent(self) -> Branch:
        if self._parent is None:
            return self

        return self._parent.first_parent()

    def copy_children(self, parent: Branch) -> None:
        parent._children.extend(self._children)

    @property
    def parent(self) -> Branch | None:
        return self._parent

    @property
    def children(self) -> list[Branch]:
        return self._children

    @property
    def version(self) -> int:
        return self._version

class MergeBranch(Branch):
    def __init__(
        self,
        version: int,
        *parents: Branch,
        name: str | None = None
    ) -> None:
        self._parents = parents
        self._version = version
        self.name = name
        self._children = []
        self._id = Branch._next_id

        Branch._next_id += 1

    @override
    def __del__(self) -> None:
        for parent in self._parents:
            parent._children.remove(self)

    @override
    def __repr__(self) -> str:
        return f"Merged branch nº {self._id} {f'"{self.name}"' if self.name is not None else ""} version {self._version}"

    @override
    def history(self) -> Iterator[Branch]:
        yield self

        for parent in self._parents:
            yield from parent.history()

    @override
    def first_parent(self) -> Branch:
        first_parent = None

        for parent in self._parents:
            current_first_parent = parent.first_parent()

            if first_parent is not None and current_first_parent != first_parent:
                raise GeneticError("Merged branch parents have different families. Cannot determinate the first parent")

            if first_parent is None:
                first_parent = current_first_parent

        if first_parent is None:
            raise ParentError("A merged branch must have 2 or more parents")

        return first_parent

    @property
    @override
    def parent(self) -> Never:
        raise ParentError("A merged branch have more than 1 parent")

    @property
    def parents(self) -> tuple[Branch, ...]:
        return self._parents
