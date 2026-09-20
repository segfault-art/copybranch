from copy import deepcopy
from typing import overload

from .branch import Branch


class Copy[T]:
    @overload
    def __init__(self, value: T, branch_name: None = None, branch: None = None) -> None:
        ...

    @overload
    def __init__(self, value: T, branch_name: str, *, branch: None = None) -> None:
        ...

    @overload
    def __init__(self, value: T, branch_name: None = None, *, branch: Branch) -> None:
        ...

    def __init__(self, value: T, branch_name: str | None = None, *, branch: Branch | None = None) -> None:
        self._value = deepcopy(value)

        if branch is not None:
            self._branch = branch

        else:
            self._branch = Branch(branch_name)

    def derive(self, branch_name: str | None = None) -> Copy[T]:
        new_copy = Copy(self.value, branch=self.branch.new_child(branch_name))

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
