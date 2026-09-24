# Merge Branch

Extends [`Branch`](branch.md#branch)

`Merge Branch` is a `Branch`,
but with the difference of having multiple parents.

Variables:

- `_parents: tuple[Branch, ...]`: Represents the parents of the current branch
- `_version: int`: Represents the version of the current branch
- `_children: list[Branch]`: Represents the child branches of the current branch
- `_id: int`: Represents the ID of the current branch

Properties:

|   name    | has setter |       variable       |
| :-------: | :--------: | :------------------: |
|  `parent` |    [ ]     | None. **DO NOT USE** |
| `parents` |    [ ]     |      `_parents`      |

## Methods

### `__init__`

Pure: No  
Signature: `(version: int, *parents: Branch, name: str | None = None) -> None`

`__init__` initializes a branch,
optionally defining its version,
parents, and name according to the arguments.

### `__repr__`

[Override](branch.md#__repr__)  
Pure: Yes  
Signature: `() -> str`

`__repr__` represents a branch,
including its ID, version, and name,
if it has one.

### `history`

[Override](branch.md#history)  
Pure: Yes  
Signature: `() -> Iterator[Branch]`

`history` tells the history of a branch,
iterating over all of its ancestors.

## `first_parent`

[Override](branch.md#history)  
Pure: Yes  
Signature: `() -> Branch`

`first_parent` gets the oldest ancestor of a branch,
returning its oldest ancestor.

Raises:

- `GeneticError`: If 2 parents have different "families"
- `ParentError`: If the branch does not have any parents, for some reason
