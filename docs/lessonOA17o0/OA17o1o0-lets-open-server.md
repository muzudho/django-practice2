# はじめに

わたしは今は `さくらのVPS` を使っているので、この連載の内容で何も言及がなければ `さくらのVPS` での説明をしている。  
しかし昔は `AWS` を使っていたので、その記事が混ざっているかもしれない  

* レンタルサーバーは最初に制限がかかっているので、それを解除していくことを覚えてほしい
* サービス、または一部の機能の提供が終了していることがある。そのときは諦めてほしい

📖 [さくらのVPS](https://vps.sakura.ad.jp/)  

# ログインする

📖 [会員IDログイン](https://secure.sakura.ad.jp/vps/login?redirect=%2Fservers)  

# スクリプトを有効にする

ダッシュボードの左のメニュー  

```plaintext
    +-------------+
    | サーバー     |
    +-------------+
    | スイッチ     |
    +-------------+
👉  | スクリプト   |
    +-------------+
    | ストレージ   |
    +-------------+
    | サーバー監視 |
    +-------------+
... 略 ...
```

👆 `スクリプト` をクリック  

```plaintext
さくらインターネット公式スクリプト      もっと見る
```

👆 `もっと見る` をクリック  

📖 [さくらのVPS 「スタートアップスクリプト」の一部提供終了のお知らせ](https://vps.sakura.ad.jp/news/startupscripts-end-jupyterlab/)  

* `pandas` を使えなくなっているから、対応するレッスンは除外してほしい

# さくらのVPSのどこにソースを置く？

例えば:  

```plaintext
    /
    └── 📂 home
        └── 📂 ubuntu
            └── 📂 app
                └── 📂 host1            # ソース
                    ├── 📂 apps1        # 各種アプリケーション
                    ├── 📂 project2     # 本番用プロジェクト
                    ├── 📄 .env
                    ├── 🐳 docker-compose.yml   # `🐳 docker-compose-project2.yml` をリネーム
                    ├── 🐳 Dockerfile
                    ├── 📄 manage.py
                    └── 📄 requirements.txt
```

* git か Visual Studio Code の Remote host を使ってファイルをコピーしてほしい
* settings.py の DEBUGフラッグは下げてほしい
* `📂 project2` settings.py などに `project1` という文字が含まれていれば `project2` に変えてほしい

# コマンド

```shell
cd /home/ubuntu/app/host1

docker-compose -f docker-compose.yml up
# docker-compose -f docker-compose-project2.yml up
```

# Dockerマシンをどうやってインストールする？

この連載では レンタルサーバーのインスタンスに Dockerマシンをインストールする方法 は説明しないが、  
👇 AWSのEC2のインスタンスのケースは 昔に記事を書いたから、参考にしてもいいし、しなくてもいい  

📖 [AWSに電子政府きふわらべをデプロイするオーバービュー（＾～＾）](https://crieit.net/posts/AWS-61a238f50f23a)  

# 備忘録

`さくらのVPS` でドッカーコンテナを起動したら、外部に公開するまで　あと２つ設定が必要。

(1)  
さくらサーバー側でポートを開く。  
セキュリティの関係上、初期設定で SSH しか開いていないので、Webの8000番ポートも通すようにする。  

(2)  
Django の settings.py に `ALLOWED_HOSTS = []` という文字列配列がある。  
ここに外部からアクセスさせる IPアドレスまたは ドメインを書くこと。  
ファイルを保存すると　自動で読込まれるので、ドッカーコンテナの再起動は必要ない。  

# 次の記事

📖 [Djangoでゲーム対局部屋のモデルを定義しよう！](https://qiita.com/muzudho1/items/e1cf253dd6929bcd708d)  

# 参考にした記事

📖 [さくらレンタルサーバーにPythonのモジュールをインストール（7/5）](http://mountainwind.sakura.ne.jp/wp/2017/07/05/%E3%81%95%E3%81%8F%E3%82%89%E3%83%AC%E3%83%B3%E3%82%BF%E3%83%AB%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%81%ABpython%E3%81%AE%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%82%92%E3%82%A4%E3%83%B3/)  
📖 [さくらのVPS（仮想専用サーバー）に解析環境を構築する方法について](https://tellusxdp.github.io/start-python-with-tellus/environment/sakura-vps.pdf)  
