"""Family's implementation."""

from typing import ClassVar, override


class Family:
    """Class for families. Represents a family."""

    _next_id: ClassVar[int] = 0

    def __init__(self, name: str | None = None, *descendants: Family) -> None:
        """Initialize a Family, with optional name and descendants."""
        self._id = Family._next_id
        self._parents = descendants
        self.name = name

        Family._next_id += 1

    @override
    def __repr__(self) -> str:
        """Represent a Family."""
        return f"Family nº {self._id} {f'"{self.name}"' if self.name is not None else ''}"

    def genetic_test(self, other: Family) -> bool:
        """Test `other` and current family genetic compatibility."""
        return self._genetic_test(other) or other._genetic_test(self)

    def _genetic_test(self, other: Family) -> bool:
        if other is self:
            return True

        if not self._parents:
            return False

        for parent in self._parents:
            if parent.genetic_test(other):
                return True

        return False
