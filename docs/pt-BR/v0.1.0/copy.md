# Copy

Generics:

- `T`
- `U`  
constraints: [`Branch`](branch/branch.md#branch),
[`MergeBranch`](branch/merge_branch.md#merge-branch)  
default: [`Branch`](branch/branch.md#branch)

`Copy` é uma classe para representar cópias,
cópias com `Branch` para versionamento,
usando o genérico `T`,
que é o tipo do valor da cópia
e o genérico `U`,
que é o tipo de Branch.

Variáveis:

- `_branch: U`
- `_value: T`

Propriedades:

|   nome   | tem setter | variável  |
|   :--:   | :--------: | :------:  |
| `value`  |    \[X]    | `_value`  |
| `branch` |    [ ]     | `_branch` |

## Métodos

### `__init__`

Pura: Não  
Assinaturas:

- `(value: T, branch_name: None = None, *, branch: None = None) -> None`
- `(value: T, branch_name: str, *, branch: None = None) -> None`
- `(value: T, branch_name: None = None, *, branch: U) -> None`

`__init__` inicializa uma cópia,
com opcionalmente `branch_name` **OU** `branch`.

### `derive`

Pura: Não  
Assinatura: `(branch_name: str | None = None) -> Copy[T, Branch]`

`derive` cria uma cópia derivada de outra,
criando outra cópia com o mesmo valor
e com a mesma versão, sendo que
a branch da nova cópia é filha
da branch da cópia atual;
`branch_name` é opcionalmente
o nome da nova cópia.

### `merge`

Pura: Não  
Assinatura: `(*other_copies: Copy, value: T | None = None, name: str | None = None) -> Copy[T, MergeBranch]`

`merge` cria uma cópia derivada de várias outras,
a branch da nova cópia é uma `MergeBranch`,
cujo os pais são as branches dessa e
de todas as outras cópias de `other_copies`,
`value` define o novo valor,
por padrão é o valor da cópia atual,
e opcionalmente, `name` é o novo nome.
