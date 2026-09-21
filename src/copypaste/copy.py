from copy import deepcopy
from typing import overload

from .branch import Branch, MergeBranch


class Copy[T, U: (Branch, MergeBranch) = Branch]:
    _branch: U

    @overload
    def __init__(self, value: T, branch_name: None = None, *, branch: None = None) -> None:
        ...

    @overload
    def __init__(self, value: T, branch_name: str, *, branch: None = None) -> None:
        ...

    @overload
    def __init__(self, value: T, branch_name: None = None, *, branch: U) -> None:
        ...

    def __init__(self, value: T, branch_name: str | None = None, *, branch: U | None = None) -> None:
        self._value = deepcopy(value)

        if branch is not None:
            self._branch = branch

        else:
            self._branch = Branch(branch_name) # type: ignore[assignment]  # ty: ignore[invalid-assignment]

    def derive(self, branch_name: str | None = None) -> Copy[T, Branch]:
        new_copy = Copy(self.value, branch=self.branch.new_child(branch_name))

        return new_copy

    def merge(self, *other_copies: Copy[T], new_value: T | None = None, name: str | None = None) -> Copy[T, MergeBranch]:
        if new_value is None:
            new_value = self.value

        merged_branch = MergeBranch(
            self._branch.version,
            self._branch,
            *(copy._branch for copy in other_copies),
            name=name
        )

        new_copy = Copy(new_value, None, branch=merged_branch)

        self._branch._children.append(merged_branch)

        for copy in other_copies:
            copy._branch._children.append(merged_branch)

        return new_copy

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, new_value: T) -> None:
        self._branch.update()
        self._value = new_value

    @property
    def branch(self) -> U:
        return self._branch
