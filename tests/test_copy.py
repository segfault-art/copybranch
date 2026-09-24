from copybranch import Branch, Copy, MergeBranch


def test_copy_creation() -> None:
    branch = Branch()
    value = ["a"]
    copy = Copy(value, branch=branch)
    other_copy = Copy(value, "a")

    assert value is not copy.value
    assert value == copy.value
    assert copy.branch is branch
    assert other_copy.branch.name == "a"


def test_copy_derivation() -> None:
    value = ["a"]
    copy = Copy(value)
    derived_copy = copy.derive()

    assert derived_copy.branch.parent is copy.branch
    assert derived_copy.branch in copy.branch.children
    assert derived_copy.value == copy.value
    assert derived_copy.value is not copy.value


def test_copy_merge() -> None:
    copy = Copy(1)
    other_copy = Copy(2)
    copy_ = copy.merge(other_copy)
    just_a_copy = copy.merge(other_copy, value=3, name="a")

    assert copy_.value == 1
    assert just_a_copy.value == 3
    assert just_a_copy.branch.name == "a"
    assert isinstance(copy_.branch, MergeBranch)
