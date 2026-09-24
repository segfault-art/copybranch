from copybranch import Copy

notas = {"segurança": "A", "confiabilidade": "A"}
copia_notas = Copy(notas)
derivacao_notas = copia_notas.derive()

derivacao_notas.value["manutenibilidade"] = "A"

# quando modificamos derivacao_notas, copia_notas não é modificada, nem notas
print(notas)  # {'segurança': 'A', 'confiabilidade': 'A'}
print(copia_notas.value)  # {'segurança': 'A', 'confiabilidade': 'A'}
print(derivacao_notas.value)
# {'segurança': 'A', 'confiabilidade': 'A', 'manutenibilidade': 'A'}

# mostra todas as branch filhas da branch de copia_notas
# quando criamos uma cópia derivada de outra,
# a branch da cópia derivada é filha da branch da cópia original
print(copia_notas.branch.children)  # Branch nº 1 version 0

# mostra a branch pai da branch de derivacao_notas
print(derivacao_notas.branch.parent)  # Branch nº 0 version 0

outra_copia = derivacao_notas.derive()
copia_alternativa = derivacao_notas.derive()

# mostra a história de todos ascendentes de outra_copia
print(list(outra_copia.branch.history()))
# [Branch nº 2 version 0, Branch nª 1 version 0, Branch nº 0 version 0]

print(list(copia_alternativa.branch.history()))
# [Branch nº 3 version 0, Branch nº 1 version 0, Branch nº 0 version 0]

# já isso, mostra todos os descendentes de copia_notas
print(list(copia_notas.branch.walk()))
# [Branch nº 2 version 0, Branch nº 3 version 0,
# Branch nº 1 version 0, Branch nº 0 version 0]
