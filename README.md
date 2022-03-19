# django-api

## 環境構築手順

1. `python3 -m venv .venv`
1. `source .venv/bin/activate`
1. `python3 -m pip install django`
1. https://www.django-rest-framework.org/tutorial/quickstart/
1. `django-admin startproject api .`

## 開発手順

1. `django-admin startproject <アプリ名>`
1. models.py にモデル追加
1. `python manage.py makemigrations`
1. `python3 manage.py migrate`
1. <アプリ名>/api/serializers.py に model と fields を追加
1. <アプリ名>/api/views.py に api の取得内容を追加
1. <アプリ名>/api/urls.py に views の path を追加
1. api/urls.py に <アプリ名> の path を追加

## 実行手順

1. 仮想環境に入る `source .venv/bin/activate`
1. `python manage.py runserver`
1. http://127.0.0.1:8000/admin へアクセス
1. ログインする
1. http://127.0.0.1:8000/api/(<アプリ名>/api/urls.py の path で設定した path)/ へアクセス
