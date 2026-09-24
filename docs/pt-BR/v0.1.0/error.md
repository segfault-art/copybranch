# Error

Esse arquivo define os erros de `copybranch`.

Erros:

- `Error`: Base para todos os erros de `copybranch`
- `BranchError` (`Error`): Base para todos os erros relacionados a branch
- `GeneticError` (`BranchError`): Erro de genética incompatível, relacionado as famílias
- `ParentError` (`BranchError`): Erro de pais, relacionado aos pais de uma branch.
