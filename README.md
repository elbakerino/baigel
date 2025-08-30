# baigel · AI APIs

[![Github actions Build](https://github.com/elbakerino/baigel/actions/workflows/blank.yml/badge.svg)](https://github.com/elbakerino/baigel/actions)

Experiments around APIs for (image/document) AI models.

- CPU only docker setup
- Expects preloaded models, no (annoying) auto-downloads
- Stats about token usages (partially/WIP)

## Tasks & Models

### Document Processing

- Image to Data (by `donut`)
- Visual Document Question Answering (Image) (by `donut`)
- *WIP* Document Classification (Image) (by `dit`)
    - (dataset) RVL-CDIP: `"letter", "form", "email", "handwritten", "advertisement", "scientific report", "scientific publication", "specification", "file folder", "news article", "budget", "invoice", "presentation", "questionnaire", "resume", "memo"`

### NLI / QA / QAG / QG

> general Natural Language Inference

- Question Answering
- Question Answer Generation
- Question Generation
- Question Natural Language Inference / QNLI

## Usage

Startup server:

```shell
docker compose up
```

- Service Home: [localhost:8702](http://localhost:8702)
- OpenAPI Docs: [localhost:8702/docs](http://localhost:8702/docs) (WIP 🚧)

Run CLI in docker container:

```shell
# build container before using cli (if never `up`ed before)
docker compose build baigel

# open shell in container:
docker compose run --rm baigel bash

# run cli help:
poetry run cli

# download models:
poetry run cli download

# list models:
poetry run cli models
```

## DEV Notes

Manage dependencies with [poetry v2](https://python-poetry.org/):

```shell
poetry lock
poetry sync --no-root
poetry install

# poetry lock --regenerate && poetry sync --no-root && poetry install
```

## License

This project is distributed as **free software** under the **MIT License**, see [License](https://github.com/elbakerino/baigel/blob/main/LICENSE).

© 2024 Michael Becker https://i-am-digital.eu
