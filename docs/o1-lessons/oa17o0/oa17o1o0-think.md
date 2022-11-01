# 没文章

よくあるミス:  

* Linux にはファイルのパーミッションという考え方がある。Windowsに慣れてると気づかない
* エラーが起きてビルドに失敗していても、動いているように見えるからエラーメッセージが原因でないことがある
* レンタルサーバーは最初に制限がかかっているので、それを解除していくことを覚えてほしい
* サービス、または一部の機能の提供が終了していることがある。そのときは諦めてほしい

# スタートアップスクリプトを入れたいとき

**この連載では不要です**  

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

サービスの提供は、無くなることもある  

📖 [さくらのVPS 「スタートアップスクリプト」の一部提供終了のお知らせ](https://vps.sakura.ad.jp/news/startupscripts-end-jupyterlab/)  

# さくらのVPSのどこにソースを置く？

例えば:  

```plaintext
    /
    └── 📂 home
        └── 📂 ubuntu
            └── 📂 repos
                └── 📂 django-practice2
                    └── 📂 src1            # ソース
                        ├── 📂 apps1        # 各種アプリケーション
                        ├── 📂 project2     # 本番用プロジェクト
                        ├── 📄 .env
                        ├── 🐳 docker-compose.yml   # `🐳 docker-compose-project2.yml` をリネーム
                        ├── 🐳 Dockerfile
                        ├── 📄 manage.py
                        └── 📄 requirements.txt
```

* git か Visual Studio Code の Remote host を使ってファイルをコピーしてほしい
* `📂 project2` settings.py などに `project1` という文字が含まれていれば `project2` に変えてほしい

# コマンド

```shell
cd /home/ubuntu/repos/django-practice2/src1

docker-compose up
# ファイルを指定するなら
# docker-compose -f docker-compose-project2.yml up
```
