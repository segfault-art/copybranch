from copybranch import Copy

grades = {"security": "A", "reliability": "A"}
grades_copy = Copy(grades)
grades_derivation = grades_copy.derive()

grades_derivation.value["maintainability"] = "A"

# when we modify grades_derivation, neither grades_copy nor grades is modified
print(grades)  # {'security': 'A', 'reliability': 'A'}
print(grades_copy.value)  # {'security': 'A', 'reliability': 'A'}
print(grades_derivation.value)
# {'security': 'A', 'reliability': 'A', 'maintainability': 'A'}

# shows all child branches of grades_copy's branch
# when we create a derived copy from another copy,
# the branch of the derived copy becomes a child of the original copy's branch
print(grades_copy.branch.children)  # Branch nº 1 version 0

# shows the parent branch of grades_derivation's branch
print(grades_derivation.branch.parent)  # Branch nº 0 version 0

another_copy = grades_derivation.derive()
alternative_copy = grades_derivation.derive()

# shows the history of all ancestors of another_copy
print(list(another_copy.branch.history()))
# [Branch nº 2 version 0, Branch nº 1 version 0, Branch nº 0 version 0]

print(list(alternative_copy.branch.history()))
# [Branch nº 3 version 0, Branch nº 1 version 0, Branch nº 0 version 0]

# shows all descendants of grades_copy's branch
print(list(grades_copy.branch.walk()))
# [Branch nº 2 version 0, Branch nº 3 version 0,
# Branch nº 1 version 0, Branch nº 0 version 0]
