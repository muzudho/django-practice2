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

## Step [OAAA1001o2o1o0g3o0] マスターデータ作成 - data/consecutive/ver1o0.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 static
                    └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                        └── 📂 data
                            ├── 📂 consecutive
👉                          │   └── 📄 ver1o0.json
                            └── 📂 participant
                                └── 📄 ver1o0.json
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

## Step [OAAA1001o2o1o0g4o0] データ作成 - data/transition/ver1o0.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 static
                    └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                        └── 📂 data
                            ├── 📂 consecutive
                            │   └── 📄 ver1o0.json
                            ├── 📂 participant
                            │   └── 📄 ver1o0.json
                            └── 📂 transition
👉                              └── 📄 ver1o0.json
```

```json
{
    "transitions": [
        {
            "id": 1,
            "last_pcp_id":3,
            "pcp_id": 3,
        },
        {
            "id": 2,
            "last_pcp_id":3,
            "pcp_id": 2,
        },
        {
            "id": 3,
            "last_pcp_id":3,
            "pcp_id": 1,
        },
        {
            "id": 4,
            "last_pcp_id":5,
            "pcp_id": 4
        },
        {
            "id": 5,
            "last_pcp_id":5,
            "pcp_id": 5
        },
        {
            "id": 6,
            "last_pcp_id":6,
            "pcp_id": 6
        },
        {
            "id": 7,
            "last_pcp_id":8,
            "pcp_id": 7
        },
        {
            "id": 7,
            "last_pcp_id":8,
            "pcp_id": 8
        },
        {
            "id": 8,
            "last_pcp_id":9,
            "pcp_id": 9
        }
    ]
}
```

👆 参加者の最終データが、他のボリュームのどの参加者と連続しているか、という構造にする  

これらのデータを元に、以前の [OAAA1001o2o0g8o0] のような JSON に整形することを目指せばよい  

## Step [OAAA1001o2o1o0g5o_1o0] オブジェクト定義 - participant/ver1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                ├── 📂 static
                │   └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                │       └── 📂 data
                │           ├── 📂 consecutive
                │           │   └── 📄 ver1o0.json
                │           ├── 📂 participant
                │           │   └── 📄 ver1o0.json
                │           └── 📂 transition
                │               └── 📄 ver1o0.json
                └── 📂 views
                    └── 📂 participant
👉                      └── 📄 ver1o0.py
```

```py
# BOF [OAAA1001o2o1o0g5o_1o0]

class Participant:
    """[OAAA1001o2o1o0g5o_1o0] 参加者"""

    def __init__(self, id, event_id, volume_id, name):
        self._id = id
        self._event_id = event_id
        self._volume_id = volume_id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def event_id(self):
        return self._event_id

    @property
    def volume_id(self):
        return self._volume_id

    @property
    def name(self):
        return self._name

# EOF [OAAA1001o2o1o0g5o_1o0]
```

## Step [OAAA1001o2o1o0g5o_2o0] オブジェクト定義 - consecutive/ver1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                ├── 📂 static
                │   └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                │       └── 📂 data
                │           ├── 📂 consecutive
                │           │   └── 📄 ver1o0.json
                │           ├── 📂 participant
                │           │   └── 📄 ver1o0.json
                │           └── 📂 transition
                │               └── 📄 ver1o0.json
                └── 📂 views
                    ├── 📂 consecutive
👉                  │   └── 📄 ver1o0.py
                    └── 📂 participant
                        └── 📄 ver1o0.py
```

```py
# BOF [OAAA1001o2o1o0g5o_2o0]

class Consecutive:
    """[OAAA1001o2o1o0g5o_2o0] 連続性"""

    def __init__(self, id, prev):
        self._id = id
        self._prev = prev
        self._originator = None

    @property
    def id(self):
        return self._id

    @property
    def prev(self):
        return self._prev

    @property
    def originator(self):
        return self._originator

    @originator.setter
    def originator(self, value):
        self._originator = value

# EOF [OAAA1001o2o1o0g5o_2o0]
```

## Step [OAAA1001o2o1o0g5o_3o0] オブジェクト定義 - transition/ver1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                ├── 📂 static
                │   └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                │       └── 📂 data
                │           ├── 📂 consecutive
                │           │   └── 📄 ver1o0.json
                │           ├── 📂 participant
                │           │   └── 📄 ver1o0.json
                │           └── 📂 transition
                │               └── 📄 ver1o0.json
                └── 📂 views
                    ├── 📂 consecutive
                    │   └── 📄 ver1o0.py
                    ├── 📂 participant
                    │   └── 📄 ver1o0.py
                    └── 📂 transition
👉                      └── 📄 ver1o0.py
```

```py
# BOF [OAAA1001o2o1o0g5o_3o0]

class Transition:
    """[OAAA1001o2o1o0g5o_3o0] 推移"""

    def __init__(self, id, last_pcp_id, pcp_id):
        self._id = id
        self._last_pcp_id = last_pcp_id
        self._pcp_id = pcp_id

    @property
    def id(self):
        return self._id

    @property
    def last_pcp_id(self):
        return self._last_pcp_id

    @property
    def pcp_id(self):
        return self._pcp_id

# EOF [OAAA1001o2o1o0g5o_3o0]
```

## Step [OAAA1001o2o1o0g5o0] データ自動計算 - consecutive → transition

いきなり最終形を作るのは難しいので、  
consecutive/ver1o0.json を与えると、 transition/ver2o0.json を返すような  
関数を作ることにする  

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 consecutive_name_vol1o0              # アプリケーション
    │           └── 📂 static
    │               └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
    │                   └── 📂 data
    │                       ├── 📂 consecutive
    │                       │   └── 📄 ver1o0.json
    │                       ├── 📂 participant
    │                       │   └── 📄 ver1o0.json
    │                       └── 📂 transition
    │                           └── 📄 ver1o0.json
    └── 📂 src1_meta
        └── 📂 scripts
            └── 📂 auto_generators
                └── 📂 consecutive_name_vol1o0
                    └── 📂 x_con_y_tra
👉                      └── 📄 __init__.py
```

```py
# BOF [OAAA1001o2o1o0g5o0]

class XPcpConYTra:

    @staticmethod
    def convert(participant_js_object, consecutive_js_object):

        pass

# EOF [OAAA1001o2o1o0g5o0]
```

# 参考にした記事

## Python Json

📖 [Python JSON](https://www.programiz.com/python-programming/json)  
