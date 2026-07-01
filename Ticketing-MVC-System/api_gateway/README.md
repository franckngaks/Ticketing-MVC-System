# API Gateway

![PyPI version](https://img.shields.io/pypi/v/api_gateway.svg)

Gestion des employés et des tickets d'incidents

* [GitHub](https://github.com/franckngaks/api_gateway/) | [PyPI](https://pypi.org/project/api_gateway/) | [Documentation](https://franckngaks.github.io/api_gateway/)
* Created by [Franck Ngako](https://github.com/franckngaks) | GitHub [@franckngaks](https://github.com/franckngaks) | PyPI [@franckngaks](https://pypi.org/user/franckngaks/)
* MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://franckngaks.github.io/api_gateway/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/api_gateway.git
cd api_gateway

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `api_gateway`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

API Gateway was created in 2026 by Franck Ngako.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
