# CopyBranch

[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=segfault-art_copybranch&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=segfault-art_copybranch)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=segfault-art_copybranch&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=segfault-art_copybranch)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=segfault-art_copybranch&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=segfault-art_copybranch)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=segfault-art_copybranch&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=segfault-art_copybranch)
[![Licensed under Apache-2.0](https://badge.ttsalpha.com/api?icon=apache&label=license&status=Apache-2.0&color=red&iconColor=D22128)](https://www.apache.org/licenses/LICENSE-2.0)
[![Mypy Passed](https://badge.ttsalpha.com/api?label=mypy&status=passed&color=green)](https://mypy-lang.org)
[![Ruff Passed](https://badge.ttsalpha.com/api?icon=ruff&label=ruff&status=passed&color=green&iconColor=D7FF64)](https://docs.astral.sh/ruff/)
[![Python 3.14](https://badge.ttsalpha.com/api?icon=python&label=python&status=3.14&color=blue&iconColor=3776AB)](https://www.python.org)

Other languages: [pt-BR](README.pt-BR.md)

A Python library for creating versioned copies of values.
Each copy can have child copies, belong to a family, and much more.

## Installation

The library is available on [PyPI](https://pypi.org/project/copybranch/).
Python version 3.14 or newer is required.

```bash
pip install copybranch
```

or...

```bash
uv add copybranch
```

## Usage

There are some examples in the [examples](examples/en) directory.

```Python
from copybranch import Copy

original_value = {"name": "copybranch", "status": "the best copy library"}
original_copy = Copy(original_value)
copy = original_copy.derive()

copy.value["status"] = "good"

print(original_value)  # {'name': 'copybranch', 'status': 'the best copy library'}
print(original_copy.value)  # {'name': 'copybranch', 'status': 'the best copy library'}

# a small demonstration of using branches with copies:

print(original_copy.branch.children)  # [Branch nº 1 version 0]
print(copy.branch.parent)  # Branch nº 0 version 0

copy.value["status"] = "still good"

print(copy.branch.version)  # 0

copy.value = {"value": "completely different"}

print(copy.branch.version)  # 1

another_copy = copy.derive()

print(another_copy.branch.version)  # 1

# This is only a simplified demonstration.
# The library has other features, such as history, walk, and merge.
# For a better demonstration and more information about the library's features,
# see the docs and examples directories.
```

## Typing

CopyBranch was developed with strict static typing.

It has:

- 100% of the library statically typed, with no dependency on stub installation
- 0 `Any`
- 0 `cast`
- 0 `# type: ignore`

The tools used in the project include:

- Mypy
- Ruff
- Ty
- SonarQube

## License

This project is licensed under the Apache-2.0 license.
For more details, see the [LICENSE](LICENSE) file or the [Apache website](https://www.apache.org/licenses/LICENSE-2.0).
