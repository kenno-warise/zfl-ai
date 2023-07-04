# django-on-hatch

[![PyPI - Version](https://img.shields.io/pypi/v/django-hatch.svg)](https://pypi.org/project/django-hatch)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-hatch.svg)](https://pypi.org/project/django-hatch)

-----

**目次**

- [詳細](#詳細)
- [インストール](#インストール)
- [設定](#設定)
- [Djangoプロジェクトに設定（開発）](#Djangoプロジェクトに設定（開発）)
- [Djangoプロジェクトに設定（テスト）](#Djangoプロジェクトに設定（テスト）)
- [実行](#実行)
- [License](#license)

## 詳細

このリポジトリはHatchプロジェクトマネージャーを使ったDjangoプロジェクトの開発またはテスト（お試し）ツールです。

配布用としてDjangoアプリをアップロードする環境を自動構築または配布用としてアップロードされたDjangoアプリをこのDjangoプロジェクトに組み込んでテストすることができます。

使用方法は以下からご覧ください。

## インストール

Pythonの環境は任意です。

私はpyenvを使用してPython3.10の環境を設定しています。

```console
$ pyenv local 3.10

$ python3 --version
Python 3.10.0
```

仮想環境を作成して有効にし、`Hatch`をインストールします。

```console
$ python3 -m venv .venv && . .venv/bin/activate

$ pip install --upgrade pip

$ pip install hatch
```

リポジトリを落とします。

```console
$ git clone https://github.com/kenno-warise/django-on-hatch.git

$ cd django-on-hatch
```

## 設定（開発＆テスト）

Hatchが配置する仮想環境のディレクトリを決める。

デフォルト設定で配置されるディレクトリは以下のコマンドで参照できる。

```console
$ hatch config show | grep 'data'
data = "/home/user/.local/share/hatch"
```

デフォルト値を変更する場合は以下のコマンドを実行する。

```console
$ hatch config set dirs.data 配置するディレクトリ
```

Djangoプロジェクトを作成

```console
$ hatch run django-admin startproject myproject .
```

言語を設定します。

```python
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True
```

Djangoを起動します。

```console
$ hatch run runserver
```

## Djangoプロジェクトに設定（開発）

Djangoアプリを作成

```console
$ hatch run python3 manage.py startapp app_1
```

## Djangoプロジェクトに設定（テスト）
アップロード済みのDjangoアプリを設定します。

`config/settings.py`

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

`pyproject.toml`

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

## 実行

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
