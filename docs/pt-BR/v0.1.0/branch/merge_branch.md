# Merge Branch

Estende [`Branch`](branch.md#branch)

`Merge Branch` é uma `Branch`,
mas com um diferencial de ter vários pais.

Variáveis:

- `_parents: tuple[Branch, ...]`: Representa os pais da branch atual
- `_version: int`: Representa a versão da branch atual
- `_children: list[Branch]`: Representa as branches filhas da branch atual
- `_id: int`: Representa o ID da branch atual

Propriedades:

|   nome    | tem setter |       variável       |
|   :--:    | :--------: |       :------:       |
| `parent`  |    [ ]     | Nenhuma. **NÃO USE** |
| `parents` |    [ ]     |      `_parents`      |

## Métodos

### `__init__`

Pura: Não  
Assinatura: `(version: int, *parents: Branch, name: str | None = None) -> None`

`__init__` inicializa uma branch,
opcionalmente definido versão,
pais e nome de acordo com os argumentos.

### `__repr__`

[Override](branch.md#__repr__)  
Pura: Sim  
Assinatura: `() -> str`

`__repr__` representa uma branch,
colocando o ID, versão e o nome dela,
caso tenha.

### `history`

[Override](branch.md#history)  
Pura: Sim  
Assinatura: `() -> Iterator[Branch]`

`history` diz a história de uma branch,
iterando todos seus ascendentes (antepassados)

## `first_parent`

[Override](branch.md#history)  
Pura: Sim  
Assinatura: `() -> Branch`

`first_person` diz o antepassado mais antigo de uma branch,
retornando o seu antepassado mais antigo.

Raises:

- `GeneticError`: Caso 2 pais tenham "famílias" diferentes
- `ParentError`: Caso a branch não tenha os pais, por algum motivo
