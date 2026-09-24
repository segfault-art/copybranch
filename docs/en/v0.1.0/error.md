# Error

This file defines the errors of `copybranch`.

Errors:

- `Error`: Base for all `copybranch` errors
- `BranchError` (`Error`): Base for all errors related to branches
- `GeneticError` (`BranchError`): Incompatible genetics error, related to families
- `ParentError` (`BranchError`): Parent error, related to the parents of a branch.
