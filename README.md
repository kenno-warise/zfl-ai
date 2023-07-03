# django-on-hatch

[![PyPI - Version](https://img.shields.io/pypi/v/django-hatch.svg)](https://pypi.org/project/django-hatch)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-hatch.svg)](https://pypi.org/project/django-hatch)

-----

**目次**

- [詳細](#詳細)
- [Installation](#installation)
- [License](#license)

## 詳細

このリポジトリはHatchプロジェクトマネージャーを使ったDjangoプロジェクトのテスト（お試し）ツールです。

配布用としてアップロードされたDjangoアプリをこのDjangoプロジェクトに組み込んでテストすることができます。

使用方法は以下からご覧ください。

## Installation

Pythonの環境は任意です。

私はpyenvを使用してPython3.10の環境を設定しています。

```console
$ pyenv local 3.10

$ python3 --version
Python 3.10.0
```

仮想環境を作成して、`Hatch`をインストールします。

```console
$ python3 -m venv .venv && . .venv/bin/activate

(.venv)$ pip install --upgrade pip

(.venv)$ pip install hatch
```

リポジトリを落とします。

```console
$ git clone https://github.com/kenno-warise/django-on-hatch.git

$ cd django-on-hatch
```

アップロード済みのDjangoアプリを設定します。

`config/setting.py`

`app_1`の部分をDjangoアプリ名に当てはめます。

```python
INSTALLED_APPS = [
    ...,
    "app_1",
]
```

`config/urls.py`

`app_1`の部分をDjangoアプリ名に当てはめます。

```python
...
from django.urls import path, include

urlpatterns = [
    ...,
    path('', include('app_1.urls')),
]
```

`pyproject.toml

`app_1`の部分をDjangoアプリ名に当てはめます。

```toml
# デフォルト環境の依存パッケージ
[tool.hatch.envs.default]
dependencies = ["django", "app_1"]

# デフォルト環境のスクリプト
# hatch run run
[tool.hatch.envs.default.scripts]
run = "python3 manage.py runserver"
```

Hatchの環境を使ってDjangoを起動します

```console
$ hatch run run
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 03, 2023 - 10:57:41
Django version 4.2.2, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## License

`django-on-hatch` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
