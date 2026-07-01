# Incident Service

![PyPI version](https://img.shields.io/pypi/v/identite_service.svg)

Gestion des tickets

* [GitHub](https://github.com/franckngaks/identite_service/) | [PyPI](https://pypi.org/project/identite_service/) | [Documentation](https://franckngaks.github.io/identite_service/)
* Created by [Franck Ngako](https://github.com/franckngaks) | GitHub [@franckngaks](https://github.com/franckngaks) | PyPI [@franckngaks](https://pypi.org/user/franckngaks/)
* MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://franckngaks.github.io/identite_service/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/identite_service.git
cd identite_service

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `identite_service`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

Incident Service was created in 2026 by Franck Ngako.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
