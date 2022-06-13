# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Usage

### Setup Virtual Environment
```
python{{ cookiecutter.python_version }} -m venv env_{{ cookiecutter.project_name }}
source env_{{ cookiecutter.project_name }}/bin/activate
poetry install
```

### Setup Git
```
git init
pre-commit install
git add .
git commit -m "Initial Commit"
```

**NOTE** You may need to `git add` and `git commit` a second time in order to resolve line-length and other subtle issues as a result of the project variability

### Execute Server
```{{ cookiecutter.application_name }}-server```

### Execute CLI
```{{ cookiecutter.application_name }}-cli --help```

### Build Package
```poetry build```
