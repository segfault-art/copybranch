from copybranch import Copy

tools = ["Ruff", "Mypy"]
tools_copy = Copy(tools)

tools_copy.value.append("Ty")

# tools remains unchanged when we modify tools_copy
print(tools)  # ['Ruff', 'Mypy']
print(tools_copy.value)  # ['Ruff', 'Mypy', 'Ty']

tools.append("SonarQube")

# the same thing happens when we modify tools
print(tools)  # ['Ruff', 'Mypy', 'SonarQube']
print(tools_copy.value)  # ['Ruff', 'Mypy', 'Ty']
