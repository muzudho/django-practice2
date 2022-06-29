# django-practice2

Djangoの練習２

## TODO

サインアップ画面を作るより先に、スーパーユーザーを作った方がいい  

## Trouble shooting

📖 [Django: relation "django_site" does not exist](https://stackoverflow.com/questions/23925726/django-relation-django-site-does-not-exist)  

* Docker を停止
* data フォルダーを消す  
* Docker を起動
* 以下のコマンドを打鍵

```shell
docker-compose run --rm web python3 manage.py migrate sites
docker-compose run --rm web python3 manage.py migrate
```
