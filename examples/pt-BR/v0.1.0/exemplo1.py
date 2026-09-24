from copybranch import Copy

ferramentas = ["Ruff", "Mypy"]
copia_ferramentas = Copy(ferramentas)

copia_ferramentas.value.append("Ty")

# ferramentas continua igual quando alteramos copia_ferramentas
print(ferramentas)  # ['Ruff', 'Mypy']
print(copia_ferramentas.value)  # ['Ruff', 'Mypy', 'Ty']

ferramentas.append("SonarQube")

# a mesma coisa quando alteramos ferramentas
print(ferramentas)  # ['Ruff', 'Mypy', 'SonarQube']
print(copia_ferramentas.value)  # ['Ruff', 'Mypy', 'Ty']
