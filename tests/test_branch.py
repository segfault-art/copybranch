from copybranch import Branch


def test_branch_creation() -> None:
    next_id = Branch._next_id
    branch = Branch("a", _version=1)

    assert next_id + 1 == Branch._next_id

    child_branch = branch.new_child("b")

    assert branch.name == "a"
    assert child_branch.name == "b"
    assert child_branch in branch
    assert branch is child_branch.parent
    assert branch.version == 1
    assert child_branch.version == 1


def test_branch_family_functions() -> None:
    branch = Branch()
    child_branch = branch.new_child()
    other_branch = child_branch.new_child()
    branch_ = child_branch.new_child()

    assert list(other_branch.history()) == [other_branch, child_branch, branch]
    assert list(branch.walk()) == [other_branch, branch_, child_branch, branch]
    assert branch_.first_parent() is branch


def test_branch_update() -> None:
    branch = Branch()

    assert branch.version == 0

    branch.update()

    assert branch.version == 1
