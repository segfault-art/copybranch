# Branch

`Branch` é uma classe para representar uma branch, uma árvores de versões.
As Branches podem ter outras branches filhas, branches pais,
e até se pode juntar 2 branches para fazer uma nova.

Variáveis:

- `_next_id: ClassVar[int]`: Representa o ID que a próxima branch
criada irá ter
- `_parent: Branch | None`: Representa a branch pai da atual
- `_children: list[Branch]`: Representa as branches filhas da atual
- `_version: int`: Representa a versão da branch atual
- `_id: int`: Representa o ID da branch atual
- `name: str`: Representa o nome da branch atual

Propriedades:

|    nome    | tem setter |   variável  |
|    :--:    | :--------: |   :------:  |
|  `parent`  |    [ ]     |  `_parent`  |
| `children` |    [ ]     | `_children` |
| `version`  |    [ ]     | `_version`  |

## Métodos

### `__init__`

Pura: Não  
Assinatura: `(name: str | None = None, _parent: Branch | None = None, _version: int = 0) -> None`

`__init__` inicializa uma branch,
opcionalmente recebendo o argumento `name`,
para nomear a branch.

### `__repr__`

Pura: Sim  
Assinatura: `() -> str`

`__repr__` representa uma branch,
colocando o ID, versão e nome dela,
caso tenha.

### `__iter__`

Pura: Sim  
Assinatura: `() -> Iterator[Branch]`

`__iter__` itera uma branch,
retornado um iterador dos filhos dela.

### `walk`

Pura: Sim  
Assinatura: `() -> Iterator[Branch]`

`walk` caminha pelos descendentes de uma branch,
iterando todos os descendentes dela.

### `history`

Pura: Sim  
Assinatura: `() -> Iterator[Branch]`

`history` diz a história de uma branch,
retornando toda a história dela,
iterando todos os ascendentes (antepassados).

### `new_child`

Pura: Não  
Assinatura: `(name: str | None = None) -> Branch`

`new_child` cria uma branch filha de outra branch,
criando uma nova branch e colocando como ela filha da atual.

### `update`

Pura: Não  
Assinatura: `() -> None`

`update` atualiza uma branch,
aumentando a versão dela em 1.

### `first_parent`

Pura: Sim  
Assinatura: `() -> Branch`

`first_parent` diz o primeiro parente de uma branch,
retornando o ancestral mais antigo dela.

### `copy_children`

Pura: Não  
Assinatura: `(parent: Branch) -> None`

`copy_children` copia as branches filhas de uma branch,
copiando as branches filhas da branch atual
para `parent`.
