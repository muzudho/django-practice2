# 目標

| What is        | This is                                                                          |
| -------------- | -------------------------------------------------------------------------------- |
| この連載の目的 | Name of consecutive を作る                                                       |
| この記事の目標 | いきなり Name of consecutive を作るのは難しいから、まず白紙のWebページを開設する |

# 情報

この記事はレッスン編を読み終えた人を対象とする  

| What is    | This is                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------- |
| レッスン編 | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

# 始める前に

👇 Name of consecutive の分かりやすい例は以下を参考  

📖 [世界コンピュータ将棋選手権のプログラム別順位の推移](http://www.yss-aya.com/csa_all.html)  

👇 Name of consecutive の必要性は、主に 以下のことを決める需要からある  

* 何年連続出場というカウントを引き継ぐチーム
* 前年の順位のシード権を引き継ぐチーム
* 新人賞の候補となるチーム

👇 以下のような問題の判定方法は人為的だ。このツールは記録と表示のみ行う  

* 去年 Apple という名前のチームが 今年は Banana という名前で出場している  
* 去年 Cherry という名前のチームが、今年は Durian と Eggfruit という名前で出場している  
* 去年 Fig と Grape という名前のチームが、今年は合体して Hernandia という名前で出場している  
* 数年ぶりに Icaco という名前のチームが出場している  

# Step OAAA1001o2o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OAAA1001o2o0g2o0 フォルダー作成 - apps1/name_of_consecutive_vol1o0 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1                            # 複数のアプリケーションを入れるフォルダー
            └── 📂 name_of_consecutive_vol1o0   # アプリケーション
```

# Step OAAA1001o1o0g3o0 アプリケーション作成

Dockerコンテナ を起動しているターミナルとは別のターミナルをもう１つ開き、  

👇 以下のコマンドを打鍵してほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# アプリケーション新規作成
docker-compose run --rm web python manage.py startapp name_of_consecutive_vol1o0 ./apps1/name_of_consecutive_vol1o0 --settings=project1.settings
#                                                     -------------------------- ----------------------------------            -----------------
#                                                     1                          2                                             3
# 1. 任意のDjangoアプリケーション名
# 2. アプリケーション フォルダーへのパス
# 3. `src1/project1/settings.py` 設定ファイルに従う
#          -----------------
```
