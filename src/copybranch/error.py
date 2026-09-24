"""Definition of all copybranch's errors."""


class Error(Exception):
    """Base error for all other copybranch's errors."""


class BranchError(Error):
    """Base error for all branch's errors."""


class GeneticError(BranchError):
    """Error for incompatible genetics."""


class ParentError(BranchError):
    """Error in parent(s)."""
