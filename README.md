<!--- --8<-- [start:description] -->
# Unit test prj

Project to run tests

**Key info :**
[![Docs](https://readthedocs.org/projects/unit-test-prj/badge/?version=latest)](https://unit-test-prj.readthedocs.io)
[![Main branch: supported Python versions](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fmzecc%2Funit_test.git%2Fmain%2Fpyproject.toml)](https://github.com/mzecc/unit_test.git/blob/main/pyproject.toml)
[![Licence](https://img.shields.io/pypi/l/unit-test-prj?label=licence)](https://github.com/mzecc/unit_test.git/blob/main/LICENCE)

**PyPI :**
[![PyPI](https://img.shields.io/pypi/v/unit-test-prj.svg)](https://pypi.org/project/unit-test-prj/)
[![PyPI install](https://github.com/mzecc/unit_test.git/actions/workflows/install-pypi.yaml/badge.svg?branch=main)](https://github.com/mzecc/unit_test.git/actions/workflows/install-pypi.yaml)

**Tests :**
[![CI](https://github.com/mzecc/unit_test.git/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/mzecc/unit_test.git/actions/workflows/ci.yaml)
[![Coverage](https://codecov.io/gh/mzecc/unit_test.git/branch/main/graph/badge.svg)](https://codecov.io/gh/mzecc/unit_test.git)

**Other info :**
[![Last Commit](https://img.shields.io/github/last-commit/mzecc/unit_test.git.svg)](https://github.com/mzecc/unit_test.git/commits/main)
[![Contributors](https://img.shields.io/github/contributors/mzecc/unit_test.git.svg)](https://github.com/mzecc/unit_test.git/graphs/contributors)
## Status

<!---

We recommend having a status line in your repo
to tell anyone who stumbles on your repository where you're up to.
Some suggested options:

- prototype: the project is just starting up and the code is all prototype
- development: the project is actively being worked on
- finished: the project has achieved what it wanted
  and is no longer being worked on, we won't reply to any issues
- dormant: the project is no longer worked on
  but we might come back to it,
  if you have questions, feel free to raise an issue
- abandoned: this project is no longer worked on
  and we won't reply to any issues
-->

- prototype: the project is just starting up and the code is all prototype

<!--- --8<-- [end:description] -->

Full documentation can be found at:
[unit-test-prj.readthedocs.io](https://unit-test-prj.readthedocs.io/en/latest/).
We recommend reading the docs there because the internal documentation links
don't render correctly on GitHub's viewer.

## Installation

<!--- --8<-- [start:installation] -->
### As a library

If you want to use Unit test prj as a library,
for example you want to use it
as a dependency in another package/application that you're building,
then we recommend installing the package with the commands below.
This method provides the loosest pins possible of all dependencies.
This gives you, the package/application developer,
as much freedom as possible to set the versions of different packages.
However, the tradeoff with this freedom is that you may install
incompatible versions of Unit test prj's dependencies
(we cannot test all combinations of dependencies,
particularly ones which haven't been released yet!).
Hence, you may run into installation issues.
If you believe these are because of a problem in Unit test prj,
please [raise an issue](https://github.com/mzecc/unit_test.git/issues).

The (non-locked) version of Unit test prj can be installed with

=== "pip"
    ```sh
    pip install unit-test-prj
    ```

Additional dependencies can be installed using

=== "pip"
    ```sh
    # To add plotting dependencies
    pip install 'unit-test-prj[plots]'

    # To add all optional dependencies
    pip install 'unit-test-prj[full]'
    ```

### For developers

For development, we rely on [uv](https://docs.astral.sh/uv/)
for all our dependency management.
To get started, you will need to make sure that uv is installed
([instructions here](https://docs.astral.sh/uv/getting-started/installation/)
(we found that the self-managed install was best,
particularly for upgrading uv later).

For all of our work, we use our `Makefile`.
You can read the instructions out and run the commands by hand if you wish,
but we generally discourage this because it can be error prone.
In order to create your environment, run `make virtual-environment`.

If there are any issues, the messages from the `Makefile` should guide you through.
If not, please raise an issue in the
[issue tracker](https://github.com/mzecc/unit_test.git/issues).

For the rest of our developer docs, please see [development][development].

<!--- --8<-- [end:installation] -->

## Original template

This project was generated from this template:
[copier core python repository](https://gitlab.com/openscm/copier-core-python-repository).
[copier](https://copier.readthedocs.io/en/stable/) is used to manage and
distribute this template.
