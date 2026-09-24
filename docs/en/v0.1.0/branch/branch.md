# Branch

`Branch` is a class for representing a branch, a tree of versions.
Branches can have other child branches, parent branches,
and can even join 2 branches to create a new one.

Variables:

- `_next_id: ClassVar[int]`: Represents the ID that the next branch
created will have
- `_parent: Branch | None`: Represents the parent branch of the current one
- `_children: list[Branch]`: Represents the child branches of the current one
- `_version: int`: Represents the version of the current branch
- `_id: int`: Represents the ID of the current branch
- `name: str`: Represents the name of the current branch

Properties:

|    name    | has setter |   variable  |
| :--------: | :--------: | :---------: |
|  `parent`  |    [ ]     |  `_parent`  |
| `children` |    [ ]     | `_children` |
| `version`  |    [ ]     | `_version`  |

## Methods

### `__init__`

Pure: No  
Signature: `(name: str | None = None, _parent: Branch | None = None, _version: int = 0) -> None`

`__init__` initializes a branch,
optionally receiving the `name` argument
to name the branch.

### `__repr__`

Pure: Yes  
Signature: `() -> str`

`__repr__` represents a branch,
including its ID, version, and name,
if it has one.

### `__iter__`

Pure: Yes  
Signature: `() -> Iterator[Branch]`

`__iter__` iterates over a branch,
returning an iterator over its children.

### `walk`

Pure: Yes  
Signature: `() -> Iterator[Branch]`

`walk` walks through the descendants of a branch,
iterating over all of its descendants.

### `history`

Pure: Yes  
Signature: `() -> Iterator[Branch]`

`history` tells the history of a branch,
returning its entire history,
iterating over all of its ancestors.

### `new_child`

Pure: No  
Signature: `(name: str | None = None) -> Branch`

`new_child` creates a child branch of another branch,
creating a new branch and making it a child of the current one.

### `update`

Pure: No  
Signature: `() -> None`

`update` updates a branch,
increasing its version by 1.

### `first_parent`

Pure: Yes  
Signature: `() -> Branch`

`first_parent` gets the first parent of a branch,
returning its oldest ancestor.

### `copy_children`

Pure: No  
Signature: `(parent: Branch) -> None`

`copy_children` copies the child branches of a branch,
copying the child branches of the current branch
to `parent`.
