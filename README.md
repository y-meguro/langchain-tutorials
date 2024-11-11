# LanChain チュートリアル

- [Tutorials | 🦜️🔗 LangChain](https://python.langchain.com/docs/tutorials/) のコード
- [LangSmith](https://www.langchain.com/langsmith) を利用

## パッケージ管理

[Poetry](https://python-poetry.org/) を利用

## 設定

- `.venv` ディレクトリをプロジェクト直下に作る

```
poetry config virtualenvs.in-project true
```

## コマンド

- ファイルの実行

```
poetry run python projects/simple_llm/main.py
```

- lint

```
poetry run ruff check
poetry run ruff check --fix
```

- format

```
poetry run ruff format
```
