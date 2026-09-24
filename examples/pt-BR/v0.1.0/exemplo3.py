# ty: ignore[invalid-ignore-comment]

from copybranch import Copy, ParentError

tipagem = {"# type: ignore": 0, "cobertura": 100}
copia_tipagem = Copy(tipagem)

# NÃO juntar as 2 atribuições em uma só, caso contrário, as 2 ficam com a mesma branch
copia_filha = copia_tipagem.derive()
outra_copia = copia_tipagem.derive()

merged_copy = outra_copia.merge(copia_filha)

# e novamente, mexer na filha não mexe nas originais e vice-versa
merged_copy.value["cast"] = 0

print(copia_filha.value)  # {'# type: ignore': 0, 'cobertura': 100}
print(outra_copia.value)  # {'# type: ignore': 0, 'cobertura': 100}

copia_filha.value["Any"] = 0

print(merged_copy.value)  # {'# type: ignore': 0, 'cobertura': 100, 'cast': 0}
print(outra_copia.value)  # {'# type: ignore': 0, 'cobertura': 100}

# é filha de 2 branches, então aparece 2 vezes na "família"
print(list(copia_tipagem.branch.walk()))
# [Merge branch nº 3 version 0, Merge branch nº 1 version 0, Branch nº 3 version 0,
# Branch nº 2 version 0, Branch nº 0 version 0]

# também aparece como a filha das 2 branches
print(copia_filha.branch.children)  # [Merge Branch nº 3 version 0]
print(outra_copia.branch.children)  # [Merge Branch nº 3 version 0]

# outra forma de provar é que aparece que as 2 branches como pais de merged_copy
try:
    # IMPORTANTE: NÃO USE ISSO. Esse é o jeito para branches normais.
    # porque como as merge branches não tem apenas 1 pai, dá erro.
    print(merged_copy.branch.parent)

except ParentError as e:
    print(e)

# esse é o jeito certo
print(merged_copy.branch.parents)  # (Branch nº 2 version 0, Branch nº 1 version 0)
