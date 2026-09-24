# Copy

Generics:

- `T`
- `U`  
constraints: [`Branch`](branch/branch.md#branch),
[`MergeBranch`](branch/merge_branch.md#merge-branch)  
default: [`Branch`](branch/branch.md#branch)

`Copy` is a class for representing copies,
copies with `Branch` for versioning,
using the generic `T`,
which is the type of the copy's value,
and the generic `U`,
which is the type of `Branch`.

Variables:

- `_branch: U`
- `_value: T`

Properties:

|   name   | has setter | variable  |
|   :--:   | :--------: | :------:  |
| `value`  |    \[X]    | `_value`  |
| `branch` |    [ ]     | `_branch` |

## Methods

### `__init__`

Pure: No  
Signatures:

- `(value: T, branch_name: None = None, *, branch: None = None) -> None`
- `(value: T, branch_name: str, *, branch: None = None) -> None`
- `(value: T, branch_name: None = None, *, branch: U) -> None`

`__init__` initializes a copy,
optionally with `branch_name` **OR** `branch`.

### `derive`

Pure: No  
Signature: `(branch_name: str | None = None) -> Copy[T, Branch]`

`derive` creates a copy derived from another,
creating another copy with the same value
and with the same version, where
the branch of the new copy is a child
of the branch of the current copy;
`branch_name` is optionally
the name of the new copy.

### `merge`

Pure: No  
Signature: `(*other_copies: Copy, value: T | None = None, name: str | None = None) -> Copy[T, MergeBranch]`

`merge` creates a copy derived from several others,
the branch of the new copy is a `MergeBranch`,
whose parents are the branches of this
and all other copies in `other_copies`,
`value` defines the new value,
by default it is the value of the current copy,
and optionally, `name` is the new name.
