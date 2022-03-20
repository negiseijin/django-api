# django-api

## 環境構築手順

1. `python3 -m venv .venv`
1. `source .venv/bin/activate`
1. `python3 -m pip install django`
1. [Django REST framework](https://www.django-rest-framework.org/) をインストール
1. `django-admin startproject api .`
1. 管理者ユーザーを作成
   `python3 manage.py createsuperuser`
   (ユーザー名、メールアドレス、パスワードを入力)

## 開発手順

1. `django-admin startproject {アプリ名}`
1. {アプリ名}/models.py にモデル追加
1. `python manage.py makemigrations`
1. `python3 manage.py migrate`
1. {アプリ名}/api/serializers.py に model と fields を追加
1. {アプリ名}/api/views.py に api の取得内容を追加
1. {アプリ名}/api/urls.py に views の path を追加
1. {アプリ名}/api/admin.py に
   - `from .models import {追加した model}` を追加
   - `admin.site.register({追加した model})` を追加
1. api/urls.py に {アプリ名} の path を追加
1. api/settings.py の INSTALLED_APPS に{アプリ名}を追加

## 実行手順

1. 仮想環境に入る `source .venv/bin/activate`
1. `python manage.py runserver`
1. [Django 管理サイト](http://127.0.0.1:8000/admin) へアクセス
1. 開発構築手順で作成した管理者ユーザーでログインする

### モデル操作

1. [Django 管理サイト](http://127.0.0.1:8000/admin)でモデルデータを CUD する

### api 操作

1. http://127.0.0.1:8000/api/{アプリ名}/api/{urls.py の path で設定した path}/ へアクセス
1. api 操作を実行する

## Python コマンド

- requirements.txt にモジュール出力
  `pip freeze > requirements.txt`
- `git clone` した場合などの環境構築
  ` python3 -m pip install -r requirements.txt`
