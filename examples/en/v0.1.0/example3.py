# ty: ignore[invalid-ignore-comment]

from copybranch import Copy, ParentError

typing = {"# type: ignore": 0, "coverage": 100}
typing_copy = Copy(typing)

# DO NOT combine the 2 assignments into one, otherwise both will have the same branch
child_copy = typing_copy.derive()
another_copy = typing_copy.derive()

merged_copy = another_copy.merge(child_copy)

# and again, modifying the child does not modify the originals and vice versa
merged_copy.value["cast"] = 0

print(child_copy.value)  # {'# type: ignore': 0, 'coverage': 100}
print(another_copy.value)  # {'# type: ignore': 0, 'coverage': 100}

child_copy.value["Any"] = 0

print(merged_copy.value)  # {'# type: ignore': 0, 'coverage': 100, 'cast': 0}
print(another_copy.value)  # {'# type: ignore': 0, 'coverage': 100}

# it is a child of 2 branches, so it appears twice in the "family"
print(list(typing_copy.branch.walk()))
# [Merge branch nº 3 version 0, Merge branch nº 1 version 0, Branch nº 3 version 0,
# Branch nº 2 version 0, Branch nº 0 version 0]

# it also appears as a child of both branches
print(child_copy.branch.children)  # [Merge Branch nº 3 version 0]
print(another_copy.branch.children)  # [Merge Branch nº 3 version 0]

# another way to prove it is that both branches appear as parents of merged_copy
try:
    # IMPORTANT: DO NOT USE THIS. This is the way for normal branches.
    # because merge branches do not have only 1 parent, it raises an error.
    print(merged_copy.branch.parent)

except ParentError as e:
    print(e)

# this is the correct way
print(merged_copy.branch.parents)  # (Branch nº 2 version 0, Branch nº 1 version 0)
