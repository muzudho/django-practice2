# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/v1/from-object-to-json-str/)  

# 目標

モデルの中身を全部見たい。  
デバッグモードなら、エラー画面で変数の内容を見れるが、エラーじゃないときも見たい  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is   | This is                                   |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Auth      | allauth                                   |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1        # アプリケーション
    │   │   ├── 📂 portal_v1                    # アプリケーション
    │   │   └── 📂 practice_v1                  # アプリケーション
    │   ├── 📂 data
    │   ├── 📂 project1                         # プロジェクト
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_accounts.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2
    │   ├── 🐳 docker-compose-project2.yml
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    └── 📄 .gitignore
```

# 手順

## Step OA10o2o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA10o2o0g2o0 データ用意 - 管理画面

管理画面から、都道府県モデルのデータを追加しておいてください  

## Step OA10o2o0g3o0 モデルヘルパー作成 - json/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                 # アプリケーション
                └── 📂 models_helper
                    └── 📂 json
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class MhJson():
    """OA10o2o0g3o0 JSONモデルヘルパー"""

    # OA10o2o0g3o0 以下のファイルはあとで作ります
    from .m_from_model_to_json_str import from_model_to_json_str, from_model_to_json_str_with_indent
    #    -------------------------        ----------------------
    #    1                                2
    # 1. `src1/apps1/practice_v1/model_helper/json/v1o0/m_from_model_to_json_str.py`
    #                                                   ------------------------
    # 2. `1.` に含まれる関数
```

## Step OA10o2o0g4o0 モデルヘルパー モジュール作成 - m_from_model_to_json_str フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                 # アプリケーション
                └── 📂 models_helper
                    └── 📂 json
                        └── 📂 v1o0
                            ├── 📄 __init__.py
👉                          └── 📄 m_from_model_to_json_str.py
```

```py
import json
from django.core import serializers


def from_model_to_json_str(any_object):
    """OA10o2o0g4o0 モデルをJSON文字列に変換する"""
    return serializers.serialize('json', any_object)


def from_model_to_json_str_with_indent(any_object):
    """OA10o2o0g4o0 モデルをインデント付きでJSON文字列に変換する"""
    json_str = from_model_to_json_str(any_object)
    doc = json.loads(json_str)
    return json.dumps(doc, indent=4)
```

## Step OA10o2o0g5o0 ビュー作成 - debug フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                 # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 json
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
                │           └── 📄 m_from_model_to_doc.py
                └── 📂 views
                    └── 📂 debug
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
from django.http import HttpResponse

# OA10o2o0g5o0 JSONモデルヘルパー
from apps1.practice_v1.models_helper.json.v1o0 import MhJson
#          -----------                    ----        ------
#          11                             12          2
#    -----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# OA10o2o0g5o0 都道府県モデル
from apps1.practice_v1.models.prefecture.v1o0 import Prefecture
#          -----------                   ----        ----------
#          11                            12          2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


class DebugV():
    """OA10o2o0g5o0 デバッグ ビュー"""

    @staticmethod
    def render_model_as_json(request):
        """OA10o2o0g5o0 描画 - モデルをダンプ出力する"""

        prefecture_resultset = Prefecture.objects.all()

        # * これだと１行で表示されて見づらい
        # json_str = MhJson.from_model_to_json_str(prefecture_resultset)
        # return HttpResponse(json_str)

        # * インデントを付けて、<pre>タグで挟む
        # * Unicode文字 が数字になって見づらいという副作用はある
        json_str = MhJson.from_model_to_json_str_with_indent(
            prefecture_resultset)
        return HttpResponse(f"<pre>{json_str}</pre>")
```

## ~~Step OA10o2o0g6o0~~

Merged to OA10o2o0g6o1o0  

## Step OA10o2o0g6o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_v1                 # アプリケーション
    │           ├── 📂 models_helper
    │           │   └── 📂 json
    │           │       └── 📂 v1o0
    │           │           ├── 📄 __init__.py
    │           │           └── 📄 m_from_model_to_doc.py
    │           └── 📂 views
    │               └── 📂 debug
    │                   └── 📂 v1o0
    │                       └── 📄 __init__.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_autogen.py,practice/v1/from-object-to-json-str/,practice_v1_from_object_to_json_str,"OA10o2o0g6o1o0 デバッグ用。モデルをダンプ出力",apps1.practice_v1.views.debug.v1o0,DebugV,,render_model_as_json
```

## Step OA10o2o0g6o2o0 ルート編集 - コマンド打鍵

👇 以下のコマンドを打鍵してほしい  

```shell
cd ../src1_meta
python -m scripts.auto_generators.urls
cd ../src1
docker-compose restart
```

* ディレクトリーは、がんばって移動してほしい
* スクリプトについて See also: O3o2o_1o0g2o0
* 設定ファイルを変更したら、サーバーの再起動が必要

## Step OA10o2o0g7o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/from-object-to-json-str/](http://localhost:8000/practice/v1/from-object-to-json-str/)  

## Step OA10o2o0g8o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                    # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1
        │       ├── 📂 models_helper
        │       │   └── 📂 json
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 m_from_model_to_doc.py
        │       └── 📂 views
        │           └── 📂 debug
        │               └── 📂 v1o0
        │                   └── 📄 __init__.py
        └── 📂 project1                         # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/from-object-to-json-str/,モデルをダンプ出力する
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでモデルのインスタンスの一覧表示をしよう！](https://qiita.com/muzudho1/items/77668130b6d941596327)  
