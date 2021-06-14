# heroku-sandbox

heroku の実験場


# 動かすために必要なこと

herokuアプリケーションを作成.

```
heroku-create <APP_NAME>
```

buildpacks python をインストール

```
heroku buildpacks:add heroku/python
```

buildpacks nginx をインストール

```
heroku buildpacks:add heroku-community/nginx
```
