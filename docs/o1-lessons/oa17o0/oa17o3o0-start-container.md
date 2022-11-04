DjangoとDocker練習[OA17o3o0] さくらのVPS コンテナー起動

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

# 手順

## Step [OA17o3o_1o0] ドッカ―コンテナ起動

```shell
# cd src1

# Docker を実行する権限のあるユーザーで実行
sudo docker-compose up
```

### Dockerコンテナの停止の方法

```shell
# 停止したくなったときに
sudo docker-compose down
```

📖 [Dockerイメージとコンテナの削除方法](https://qiita.com/tifa2chan/items/e9aa408244687a63a0ae)  

## Step [OA17o3o0] 備忘録

`さくらのVPS` でドッカーコンテナを起動したら、外部に公開するまで　あと２つ設定が必要。

## Step [OA17o3o1o0] (1) ポートを開く

さくらサーバー側でポートを開きたい。  
セキュリティの関係上、初期設定で SSH しか開いていないので、Webの8000番ポートも通したい  

`さくらのVPS` - `サーバー` - `{サーバー名}` - `パケットフィルター設定`  

👇 カスタムを追加  

```plaintext
    SSH    TCP 22    送信元IPアドレス：すべて許可する
👉  カスタム    TCP 8000    送信元IPアドレス：すべて許可する
```

`設定を保存する` をクリック  

## Step [OA17o3o2o0] (2) ホストを設定する

Django の settings.py に `ALLOWED_HOSTS = []` という文字列配列がある。  
ここに外部からアクセスさせる IPアドレスまたは ドメインを書くこと。  
ファイルを保存すると　自動で読込まれるので、ドッカーコンテナの再起動は必要ない。  

わたしは、ドメインは `Value Domain` のようなサービスを使って購入している  

📖 [Value Domain](https://www.value-domain.com/)  

# 次の記事

📖 [Djangoでゲーム対局部屋のモデルを定義しよう！](https://qiita.com/muzudho1/items/e1cf253dd6929bcd708d)  
