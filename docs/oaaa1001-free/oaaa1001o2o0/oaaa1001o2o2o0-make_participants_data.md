# 目標

| What is        | This is                                                                                               |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| この連載の目的 | 連続名（Consecutive name）ツール を作る                                                               |
| この記事の目標 | いきなり 連続名（Consecutive name）ツール を作るのは難しいから、まず参加者（Participant）データを作る |

# 情報

👇 この記事はレッスン編と前回の記事を読み終えた人を対象とする  

| What is    | This is                                                                                                          |
| ---------- | ---------------------------------------------------------------------------------------------------------------- |
| レッスン編 | 📖 [[O1o1o0] DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |
| 前回の記事 | 📖 [[OAAA1001o2o1o0] 催事のマスターデータを作ろう！](https://qiita.com/muzudho1/items/662b4aecd07a2f7e79af)       |

👇 Step の変な数字の説明  

📖 [電脳向量表記](https://qiita.com/muzudho1/items/fdbf31e41dd8c247081f)  

# 手順

## Step [OAAA1001o2o1o0g1o0] Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [OAAA1001o2o1o0g2o0] マスターデータ作成 - data/participant/ver1o0.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 static
                    └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                        └── 📂 data
                            └── 📂 participant
👉                              └── 📄 ver1o0.json
```

```json
{
    "participants": [
        {
            "id": 1,
            "event_id": 1,
            "volume_id": 4,
            "name": "Apple"
        },
        {
            "id": 2,
            "event_id": 1,
            "volume_id": 5,
            "name": "Banana"
        },
        {
            "id": 3,
            "event_id": 1,
            "volume_id": 6,
            "name": "Apple"
        },
        {
            "id": 4,
            "event_id": 1,
            "volume_id": 3,
            "name": "Cherry"
        },
        {
            "id": 5,
            "event_id": 1,
            "volume_id": 4,
            "name": "Durian"
        },
        {
            "id": 6,
            "event_id": 1,
            "volume_id": 4,
            "name": "Eggfruit"
        },
        {
            "id": 7,
            "event_id": 1,
            "volume_id": 4,
            "name": "Fig"
        },
        {
            "id": 8,
            "event_id": 1,
            "volume_id": 5,
            "name": "Hernandia"
        },
        {
            "id": 9,
            "event_id": 1,
            "volume_id": 4,
            "name": "Grape"
        }
    ]
}
```

## Step [OAAA1001o2o1o0g2o0] マスターデータ作成 - data/consecutive/ver1o0.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 static
                    └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                        └── 📂 data
                            └── 📂 consecutive
👉                              └── 📄 ver1o0.json
```

```json
{
    "consecutive": [
        {
            "prev": null,
            "id": 1
        },
        {
            "prev": 1,
            "id": 2
        },
        {
            "prev": 2,
            "id": 3
        },
        {
            "prev": null,
            "id": 4
        },
        {
            "prev": 4,
            "id": 5
        },
        {
            "prev": null,
            "id": 6
        },
        {
            "prev": null,
            "id": 7
        },
        {
            "prev": 7,
            "id": 8
        },
        {
            "prev": null,
            "id": 9
        }
    ]
}
```

👆 現在から見て、どれが前回か、という構造にする  
