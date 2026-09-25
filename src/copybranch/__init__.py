"""Base copypaste's package. Errors, branches and copy."""

from .branch import Branch, MergeBranch
from .copy import Copy
from .error import BranchError, Error, GeneticError, ParentError
from .family import Family

__all__ = [
    "Branch",
    "BranchError",
    "Copy",
    "Error",
    "Family",
    "GeneticError",
    "MergeBranch",
    "ParentError",
]
