# 目標

| What is        | This is                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------- |
| この連載の目的 | 連続名（Consecutive name）ツール を作る                                                  |
| この記事の目標 | いきなり 連続名（Consecutive name）ツール を作るのは難しいから、まずマスターデータを作る |

# 情報

👇 この記事はレッスン編と前回の記事を読み終えた人を対象とする  

| What is    | This is                                                                                                          |
| ---------- | ---------------------------------------------------------------------------------------------------------------- |
| レッスン編 | 📖 [[O1o1o0] DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |
| 前回の記事 | 📖 [[OAAA1001o2o0] 連続名ツールを作ろう！](https://qiita.com/muzudho1/items/0ae87ae14ee28ccbb08e)                 |

👇 Step の変な数字の説明  

📖 [電脳向量表記](https://qiita.com/muzudho1/items/fdbf31e41dd8c247081f)  

# Step [OAAA1001o2o1o0g1o0] Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step [OAAA1001o2o1o0g2o0] マスターデータ作成 - events/ver1o0.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 static
                    └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                        └── 📂 data
                            └── 📂 events
👉                              └── 📄 ver1o0.json
```

```json
{
    "events": [
        {
            "id": "1",
            "display_name": "2020春",
            "sort": 1.1
        },
        {
            "id": "2",
            "display_name": "2020冬",
            "sort": 1.2
        },
        {
            "id": "3",
            "display_name": "2021春",
            "sort": 1.3
        },
        {
            "id": "4",
            "display_name": "2021冬",
            "sort": 1.4
        },
        {
            "id": "5",
            "display_name": "2022春",
            "sort": 1.5
        },
        {
            "id": "6",
            "display_name": "2022冬",
            "sort": 1.6
        }
    ]
}
```
