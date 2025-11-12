# Development - Mem0
Source: https://docs.mem0.ai/contributing/development
Downloaded: 2025-11-12 21:20:22
================================================================================


# ​Development Contributions
[​](https://docs.mem0.ai/contributing/development#development-contributions)
## ​Submitting Your Contribution through PR
[​](https://docs.mem0.ai/contributing/development#submitting-your-contribution-through-pr)- Fork & Clonethe repository:Mem0 on GitHub
[Mem0 on GitHub](https://github.com/mem0ai/mem0)- Create a Feature Branch: Use a dedicated branch for your changes, e.g.,feature/my-new-feature
`feature/my-new-feature`- Implement Changes: If adding a feature or fixing a bug, ensure to:Write necessarytestsAdddocumentation, docstrings, and runnable examples
- Write necessarytests
- Adddocumentation, docstrings, and runnable examples
- Code Quality Checks:Runlintingto catch style issuesEnsureall tests pass
- Runlintingto catch style issues
- Ensureall tests pass
- Submit a Pull Request
[GitHub’s documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
## ​Dependency Management
[​](https://docs.mem0.ai/contributing/development#dependency-management)`hatch`[official instructions](https://hatch.pypa.io/latest/install/)`pip``conda`
```
# 1. Install base dependencies
make install

# 2. Activate virtual environment (this will install dependencies)
hatch shell  # For default environment
hatch -e dev_py_3_11 shell  # For dev_py_3_11 (differences are mentioned in pyproject.toml)

# 3. Install all optional dependencies
make install_all

```

## ​Development Standards
[​](https://docs.mem0.ai/contributing/development#development-standards)
### ​Pre-commit Hooks
[​](https://docs.mem0.ai/contributing/development#pre-commit-hooks)`pre-commit`
```
pre-commit install

```

### ​Linting withruff
[​](https://docs.mem0.ai/contributing/development#linting-with-ruff)`ruff`
```
make lint

```

### ​Code Formatting
[​](https://docs.mem0.ai/contributing/development#code-formatting)
```
make format

```

### ​Testing withpytest
[​](https://docs.mem0.ai/contributing/development#testing-with-pytest)`pytest`
```
make test

```
`make install_all`
## ​Release Process
[​](https://docs.mem0.ai/contributing/development#release-process)