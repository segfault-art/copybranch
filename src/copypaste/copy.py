from copy import deepcopy

from .branch import Branch


class Copy[T]:
    def __init__(self, value: T) -> None:
        self._value = deepcopy(value)
        self._branch = Branch()

    def derive(self) -> Copy[T]:
        new_copy = Copy(self.value)

        new_copy._branch = self._branch.new_child()
        return new_copy

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, new_value: T) -> None:
        self._branch.update()
        self._value = new_value

    @property
    def branch(self) -> Branch:
        return self._branch
