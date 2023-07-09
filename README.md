# zfl-ai

[![PyPI - Version](https://img.shields.io/pypi/v/django-hatch.svg)](https://pypi.org/project/django-hatch)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-hatch.svg)](https://pypi.org/project/django-hatch)

-----

**目次**

- [詳細](#詳細)
- [インストール](#インストール)
- [設定（開発＆テスト）](#設定)
- [Djangoプロジェクトに設定（テスト）](#Djangoプロジェクトに設定（テスト）)
- [License](#license)

## 詳細

djangoプロジェクトでインストールできるDjangoアプリです。

使用方法は以下からご覧ください。

## インストール

実行環境は「Python3.7」、「Django2.2.5」です。

Djangoアプリはpipでインストールします。

```console
$ pip install zfl-ai
```

GitHubからインストールする場合。

```console
$ pip github+
```

Djangoプロジェクトを作成

```console
$ django-admin startproject myproject .
```

言語を設定します。

`myproject/settings.py`

```python
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True
```

## Djangoプロジェクトに設定（テスト）

Djangoアプリを設定します。

`myproject/settings.py`

```python
INSTALLED_APPS = [
    ...,
    "ai",
]
```

`myproject/urls.py`

```python
...
from django.urls import path, include

urlpatterns = [
    ...,
    path('', include('ai.urls')),
]
```

サーバーを起動します。

```console
$ python3 manage.py runserver
```

## License

`zfl-ai` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
