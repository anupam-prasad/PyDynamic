# Advices and tips for contributors

If you want to become active as developer, we provide all important information here
to make the start as easy as possible. The code you produce should be seamlessly
integrable into PyDynamic by aligning your work with the established workflows.
This guide should work on all platforms and provide everything needed to start
developing for PyDynamic. Please open an issue or ideally contribute to this
guide as a start, if problems or questions arise.

## Guiding principles

The PyDynamic development process is based on the following guiding principles: 

- support all [major Python versions supported upstream
  ](https://devguide.python.org/#status-of-python-branches).
- actively maintain, ensuring security vulnerabilities or other issues
  are resolved in a timely manner 
- employ state-of-the-art development practices and tools, specifically
  - follow [semantic versioning](https://semver.org/)
  - use [conventional commit messages](https://www.conventionalcommits.org/en/v1.0.0/)
  - consider the PEP8 style guide, wherever feasible

## Get started developing

### Get the code on GitHub and locally

For collaboration we recommend forking the repository as described 
[here](https://help.github.com/en/articles/fork-a-repo). Simply apply the changes to
your fork and open a Pull Request on GitHub as described
[here](https://help.github.com/en/articles/creating-a-pull-request). For small
changes it will be sufficient to just apply your changes on GitHub and send the PR
right away. For more comprehensive work, you should clone your fork and read on
carefully.
   
### Initial development setup

This guide assumes you already have a valid runtime environment for PyDynamic as
described in the [README](https://github.com/PTB-PSt1/PyDynamic/blob/master/README.md).
To start developing, install the required dependencies for your specific Python
version. To find it, activate the desired virtual environment and execute:

```shell
(PyDynamic_venv) $ python --version
Python 3.8.3
```

Then upgrade/install _pip_ and _pip-tools_ which we use to pin our dependencies to
specific versions:
 
```shell
(PyDynamic_venv) $ pip install --upgrade pip pip-tools
```

You can then initially install or at any later time update
all dependencies to the versions we use. From the repository root run _pip-tools_'
command [`pip-sync`](https://pypi.org/project/pip-tools/#example-usage-for-pip-sync)
e.g. for Python 3.8:

```shell
(PyDynamic_venv) $ pip-sync requirements/dev-requirements-py38.txt requirements/requirements-py38.txt
```

### Advised toolset

We use [_black_](https://pypi.org/project/black/) to implement our coding style,
[_Sphinx_](https://pypi.org/project/Sphinx/) for automated generation of [our
 documentation on ReadTheDocs](https://pydynamic.readthedocs.io/en/latest/). We use
[_pytest_](https://pypi.org/project/pytest/) managed by
[_tox_](https://pypi.org/project/tox/) as testing framework backed by
[_hypothesis_](https://pypi.org/project/hypothesis/) and
[_coverage_](https://pypi.org/project/coverage/). For automated releases we use
[_python-semantic-release_](https://github.com/relekang/python-semantic-release) in
[our pipeline on _CircleCI_](https://app.circleci.com/pipelines/github/PTB-PSt1/PyDynamic)
. All requirements for contributions are derived from this. If you followed the
steps for the [initial development setup](#Initial-development-setup) you have
everything at your hands.

### Coding style

As long as the readability of mathematical formulations is not impaired, our code
should follow [PEP8](https://www.python.org/dev/peps/pep-0008/). For automating this 
uniform formatting task we use the Python package
[_black_](https://pypi.org/project/black/). It is easy to handle and [integrable into
 most common IDEs](https://github.com/psf/black#editor-integration), such that it is
automatically applied.

### Commit style

[Conventional commit messages](https://www.conventionalcommits.org/en/v1.0.0/#summary)
are required for the following:

- Releasing automatically according to [semantic versioning](https://semver.org/)
- [Generating  a changelog automatically](https://github.com/PTB-PSt1/PyDynamic/releases/tag/v1.4.0)

Parts of the commit messages and links appear in the changelogs of subsequent
releases as a result. We use the following types:

- _feat_: for commits that introduce new features 
- _docs_: for commits that contribute significantly to documentation
- _fix_: commits in which bugs are fixed
- _build_: Commits that affect packaging
- _ci_: Commits that affect the CI pipeline
- _test_: Commits that apply significant changes to tests
- _chore_: Commits that affect other non-PyDynamic components (e.g. ReadTheDocs, Git
, ... )
- _revert_: commits, which undo previous commits using `git revert`
- _refactor_: commits that merely reformulate, rename or similar
- _style_: commits, which essentially make changes to line breaks and whitespace
- _wip_: Commits which are not recognizable as one of the above-mentioned types until
  later, usually during a PR merge.  The merge commit is then marked as the
  corresponding type.

###  Testing

We strive to increase [our code coverage](https://codecov.io/gh/PTB-PSt1/PyDynamic) with 
every change introduced. This requires that every new feature and every change to 
existing features is accompanied by appropriate _pytest_ testing. We test the basic
components for correctness and, if necessary, the integration into the big picture.
It is usually sufficient to create
[appropriately named](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery)
methods in one of the existing modules in the subfolder test. If necessary add
a new module that is appropriately named.

## Workflow for adding completely new functionality

In case you add a new feature you generally follow the pattern:

- read through and follow this contribution advices and tips, especially regarding 
  the [advised tool](#advised-toolset) set and [commit style](#commit-style)
- open an according issue to submit a feature request and get in touch with other
  PyDynamic developers and users
- fork the repository or update the _master_ branch of your fork and create an
  arbitrary named feature branch from _master_
- decide which package and module your feature should be integrated into
- if there is no suitable package or module, create a new one and a corresponding
  module in the _test_ subdirectory with the same name prefixed by _test__
- after adding your functionality add it to all higher-level `__all__` variables in
  the module itself and in the higher-level `__init__.py`s
- if new dependencies are introduced, add them to _setup.py_ or _dev-requirements.in_
- during development write tests in alignment with existing test modules, for example
  [_test_interpolate_](https://github.com/PTB-PSt1/PyDynamic/blob/master/test/test_interpolate.py)
  or [_test_propagate_filter_](https://github.com/PTB-PSt1/PyDynamic/blob/master/test/test_propagate_filter.py)
- write docstrings in the
  [NumPy docstring format](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
- as early as possible create a draft pull request onto the upstream's _master_
  branch
- once you think your changes are ready to merge,
  [request a review](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/requesting-a-pull-request-review)
  from the _PTB-PSt1/pydynamic-devs_ (you will find them in the according drop-down) and
  [mark your PR as _ready for review_](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/changing-the-stage-of-a-pull-request#marking-a-pull-request-as-ready-for-review)
- at the latest now you will have the opportunity to review the documentation
  automatically generated from the docstrings on ReadTheDocs after your reviewers
  will set up everything 
- resolve the conversations and have your pull request merged

## Documentation

The documentation of PyDynamic consists of three parts. Every adaptation of an
existing feature and every new feature requires adjustments on all three levels:

- user documentation on ReadTheDocs
- examples in the form of Jupyter notebooks for extensive features and Python scripts
  for features which can be comprehensively described with few lines of commented code 
- developer documentation in the form of comments in the code

### User documentation

To locally generate a preview of what ReadTheDocs will generate from your docstrings,
you can simply execute after activating your virtual environment:

```shell
(PyDynamic_venv) $ sphinx-build docs/ docs/_build
Sphinx v3.1.1 in Verwendung
making output directory...
[...]
build abgeschlossen.

The HTML pages are in docs/_build.
```

After that you can open the file ./docs/_build/index.html relative to the project's
root with your favourite browser. Simply re-execute the above command after each
change to the docstrings to update your local version of the documentation.

### Examples

We want to provide extensive sample material for all PyDynamic features in order to
simplify the use or even make it possible in the first place. We collect the
examples in a separate repository [PyDynamic_tutorials
](https://github.com/PTB-PSt1/PyDynamic_tutorials) separate from PyDynamic to
better distinguish the core functionality from additional material. Please refer to
the corresponding README for more information about the setup and create a pull
request accompanying the pull request in PyDynamic according to the same procedure
we describe here.

### Comments in the code

Regarding comments in the code we recommend to invest 45 minutes for the PyCon DE
2019 Talk of Stefan Schwarzer, a 20+-years Python developer:
[Commenting code - beyond common wisdom](https://www.youtube.com/watch?v=tP5uWCruaBs&list=PLHd2BPBhxqRLEhEaOFMWHBGpzyyF-ChZU&index=22&t=0s).

## Manage dependencies

As stated in the README and above we use
[_pip-tools_](https://pypi.org/project/pip-tools/) for dependency management. The
requirements subdirectory contains a _requirements.txt_ and a _dev-requirements.txt_
for all supported Python versions, with a suffix naming the version, for example
[_requirements-py35.txt_](https://github.com/PTB-PSt1/PyDynamic/blob/master/requirements/requirements-py35.txt)
To keep them up to date semi-automatically we use the bash script
[_requirements/upgrade_dependencies.sh_](https://github.com/PTB-PSt1/PyDynamic/blob/master/requirements/upgrade_dependencies.sh).
It contains extensive comments on its use. _pip-tools_' command `pip-compile` finds
the right versions from the dependencies liste in _setup.py_ and the
_dev-requirements.in_.

## Licensing

All contributions are released under PyDynamic's 
[GNU Lesser General Public License v3.0](https://github.com/PTB-PSt1/PyDynamic/blob/master/licence.txt).