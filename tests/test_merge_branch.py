import pytest

from copybranch import Branch, GeneticError, MergeBranch, ParentError


def test_merge_branch_creation() -> None:
    first_parent = Branch()
    second_parent = Branch()
    id = Branch._next_id
    merge_branch = MergeBranch(1, first_parent, second_parent, name="a")

    assert id + 1 == Branch._next_id
    assert merge_branch.parents == (first_parent, second_parent)
    assert merge_branch.version == 1
    assert merge_branch.name == "a"
    assert merge_branch.children == []
    assert merge_branch._id == id


def teste_merge_branch_deletion() -> None:
    first_parent = Branch()
    second_parent = Branch()
    merge_branch = MergeBranch(0, first_parent, second_parent)

    del merge_branch

    assert first_parent.children == []
    assert second_parent.children == []


def test_merge_branch_family_functions() -> None:
    first_parent = Branch()
    second_parent = Branch()
    child_branch = first_parent.new_child()
    merge_branch = MergeBranch(0, child_branch, second_parent)

    assert list(merge_branch.history()) == [
        merge_branch,
        child_branch,
        first_parent,
        second_parent,
    ]

    with pytest.raises(GeneticError):
        merge_branch.first_parent()

    merge_branch._parents = ()

    with pytest.raises(ParentError):
        merge_branch.first_parent()
