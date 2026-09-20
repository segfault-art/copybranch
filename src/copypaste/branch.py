from typing import TYPE_CHECKING, override

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import ClassVar

class Branch:
    __n: ClassVar[int] = 0

    def __init__(self, name: str | None = None, _parent: Branch | None = None, _version: int = 0) -> None:
        self._parent = _parent
        self._children: list[Branch] = []
        self._version = _version
        self.name = name
        self._id = Branch.__n

        Branch.__n += 1

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

    def delete(self, new_parent: Branch | None = None) -> None:
        if self._parent is not None:
            self._parent._children.remove(self)

        if new_parent is not None:
            new_parent._children.extend(self._children)

        else:
            for children in self._children:
                children.delete()

        del self._parent
        del self._children

    def update(self) -> None:
        self._version += 1

    @property
    def parent(self) -> Branch | None:
        return self._parent

    @property
    def children(self) -> list[Branch]:
        return self._children

    @property
    def version(self) -> int:
        return self._version
