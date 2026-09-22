# CopyBranch

[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=segfault-art_copybranch&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=segfault-art_copybranch)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=segfault-art_copybranch&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=segfault-art_copybranch)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=segfault-art_copybranch&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=segfault-art_copybranch)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=segfault-art_copybranch&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=segfault-art_copybranch)
[![Licensed under Apache-2.0](https://badge.ttsalpha.com/api?icon=apache&label=license&status=Apache-2.0&color=red&iconColor=D22128)](https://www.apache.org/licenses/LICENSE-2.0)
[![Mypy Passed](https://badge.ttsalpha.com/api?label=mypy&status=passed&color=green)](https://mypy-lang.org)
[![Ruff Passed](https://badge.ttsalpha.com/api?icon=ruff&label=ruff&status=passed&color=green&iconColor=D7FF64)](https://docs.astral.sh/ruff/)
[![Python 3.14](https://badge.ttsalpha.com/api?icon=python&label=python&status=3.14&color=blue&iconColor=3776AB)](https://www.python.org)

Outras línguas disponíveis: [en](README.md)

Uma biblioteca de Python para criar cópias versionadas de valores,
cada cópia pode ter uma cópia filha, pode ter uma família e muito mais.

## Instalação

A biblioteca está disponível no [PyPI](https://pypi.org/project/copybranch/),
é necessário ter o Python versão 3.14 ou maior.

```bash
pip install copybranch
```

ou...

```bash
uv add copybranch
```

## Uso

Há alguns exemplos na pasta [examples](examples/).

```Python
from copybranch import Copy

valor_original = {"name": "copybranch", "status": "a melhor biblioteca de cópia"}
copia_original = Copy(valor_original)
copia = copia_original.derive()

copia.value["status"] = "boa"

print(valor_original)  # {'name': 'copybranch', 'status': 'a melhor biblioteca de cópia'}
print(
    copia_original.value
)  # {'name': 'copybranch', 'status': 'a melhor biblioteca de cópia'}

# uma pequena demonstração de utilização de branch com cópias:

print(copia_original.branch.children)  # [Branch nº 1 version 0]
print(copia.branch.parent)  # Branch nº 0 version 0

copia.value["status"] = "ainda boa"

print(copia.branch.version)  # 0

copia.value = {"valor": "totalmente outro"}

print(copia.branch.version)  # 1

outra_copia = copia.derive()

print(outra_copia.branch.version)  # 1

# Esta é apenas uma demonstração simplificada.
# A biblioteca possui outros recursos, como history, walk e merge.
# Para uma demonstração melhor e saber mais sobre os recursos da biblioteca,
# olhe as pastas docs e examples
```

## Tipagem

O copybranch foi desenvolvido com uma tipagem estática rigorosa.

Tendo:

- 100% de tipagem na biblioteca, sem dependência de instalação de stubs
- 0 `Any`
- 0 `cast`
- 0 `# type: ignore`

As ferramentas que foram utilizadas na aplicação incluem:

- Mypy
- Ruff
- SonarQube

## Licença

Este projeto está licenciado sob a licença Apache-2.0.
Para mais detalhes, visite o arquivo [LICENSE](LICENSE) ou o [site da Apache](https://www.apache.org/licenses/LICENSE-2.0)
