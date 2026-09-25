from copybranch import Family


def test_family_creation() -> None:
    id = Family._next_id
    family = Family("name")
    child_family = Family(None, family)

    assert family._id == id
    assert id + 2 == Family._next_id
    assert family.name == "name"
    assert family in child_family._parents


def test_family_genetic_test() -> None:
    family = Family()
    child_family = Family(None, family)
    other_family = Family(None, child_family)

    assert other_family.genetic_test(other_family)
    assert child_family.genetic_test(other_family)
    assert family.genetic_test(other_family)
    assert other_family.genetic_test(child_family)
    assert other_family.genetic_test(family)
