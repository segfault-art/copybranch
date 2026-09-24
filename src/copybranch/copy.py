"""Copy implementation."""

from copy import deepcopy
from typing import TypeIs, overload

from .branch import Branch, MergeBranch


class Copy[T, U: (Branch, MergeBranch) = Branch]:
    """Class for copies."""

    _branch: U

    @overload
    def __init__(
        self, value: T, branch_name: None = None, *, branch: None = None
    ) -> None: ...

    @overload
    def __init__(self, value: T, branch_name: str, *, branch: None = None) -> None: ...

    @overload
    def __init__(self, value: T, branch_name: None = None, *, branch: U) -> None: ...

    def __init__(
        self, value: T, branch_name: str | None = None, *, branch: U | None = None
    ) -> None:
        """Initialize a copy with optional name or branch given."""
        self._value = deepcopy(value)
        new_branch = branch if branch is not None else Branch(branch_name)

        def valide_branch(new_branch: Branch) -> TypeIs[U]:
            return isinstance(new_branch, type(branch) if branch is not None else Branch)

        if valide_branch(new_branch):
            self._branch = new_branch

        else:
            raise TypeError("Has occurred an unexpected fatal error.")

    def derive(self, branch_name: str | None = None) -> Copy[T, Branch]:
        """
        Create a new copy derived from this copy.

        Create a new child branch of this copy's branch,
        and create a copy using the new branch.

        Args:
            branch_name: New branch's name.

        Returns:
            A new copy whose branch is a child of this copy's branch.

        """
        new_copy = Copy(self.value, branch=self.branch.new_child(branch_name))

        return new_copy

    def merge[V](
        self,
        *other_copies: Copy[V, Branch | MergeBranch],
        value: T | None = None,
        name: str | None = None,
    ) -> Copy[T, MergeBranch]:
        """
        Create a new copy merging self and other_copies.

        Create a new merge branch of self's branch and other_copies' branches,
        and create a copy using the new branch.

        Args:
            other_copies: Other copies to merge with self.
            value: New copy's value.
            name: New branch's name.

        Returns:
            A new copy whose branch is a merge of self's branch
            and other_copies' branches.

        """
        if value is None:
            value = self.value

        merge_branch = MergeBranch(
            self._branch.version,
            self._branch,
            *(copy._branch for copy in other_copies),
            name=name,
        )

        new_copy = Copy(value, None, branch=merge_branch)

        self._branch._children.append(merge_branch)

        for copy in other_copies:
            copy._branch._children.append(merge_branch)

        return new_copy

    @property
    def value(self) -> T:
        """Return copy's value."""
        return self._value

    @value.setter
    def value(self, new_value: T) -> None:
        self._branch.update()
        self._value = new_value

    @property
    def branch(self) -> U:
        """Return self's branch."""
        return self._branch
