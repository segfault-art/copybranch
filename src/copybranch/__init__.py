"""Base copypaste's package. Errors, branches and copy."""

from .branch import Branch, MergeBranch
from .copy import Copy
from .error import BranchError, Error, GeneticError, ParentError

__all__ = [
    "Branch",
    "BranchError",
    "Copy",
    "Error",
    "GeneticError",
    "MergeBranch",
    "ParentError",
]
