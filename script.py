from copypaste import Copy

a: list[str] = ["a"]
b: Copy[list[str]] = Copy(a, "b")

a.append("b")

print(b.value, b.branch)

b.value.append("c")

print(b.value, b.branch)

b.value = []

print(b.value, b.branch)

c: Copy[list[str]] = b.derive("c")

print(c.value, c.branch)

c.value.append("o")

print(b.value, b.branch)

d = c.derive("d")
e = c.derive("e")

d.branch.update()

print(d.branch)
print(e.branch)

for branch in d.branch.history():
    print(branch)

print()

for child in c.branch:
    print(child)

print(list(b.branch.walk()))
