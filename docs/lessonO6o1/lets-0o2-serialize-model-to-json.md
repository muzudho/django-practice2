# 目的

モデルの中身を全部見たい。  
デバッグモードなら、エラー画面で変数の内容を見れるが、エラーじゃないときも見たい  

# 手段

モデルを、JSON形式にシリアライズ（出力）する  

# はじめに

この記事は LessonO2o1 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Auth      | allauth                                   |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 host1
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   │   ├── 📂 data
    │   │   │   │   └── 📄 finished-lesson.csv
    │   │   │   ├── 📂 migrations
    │   │   │   │   └── 📄 __init__.py
    │   │   │   ├── 📂 static
    │   │   │   │   └── 🚀 favicon.ico
    │   │   │   ├── 📂 templates
    │   │   │   │   └── 📂 portal_v1
    │   │   │   │       └── 📂 o1
    │   │   │   │           └── 📄 portal_base.html
    │   │   │   └── 📂 views
    │   │   │       └── 📂 o1
    │   │   │           └── 📄 pages.py
    │   │   └── 📂 practice_v1              # アプリケーション
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト
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
    └── 📄 .gitignore
```

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. データ用意 - 管理画面

管理画面から、都道府県モデルのデータを追加しておいてください  

# Step 3. モデルヘルパー モジュール作成 - mh_json フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                 # アプリケーション
                └── 📂 models_helper
                    └── 📂 o1
                        └── 📂 mh_json
👉                          └── 📄 __init__.py
```

```py
class MhJson():
    """JSONモデルヘルパー"""

    # 以下のファイルはあとで作ります
    from .m_from_model_to_json_str import from_model_to_json_str
    #    -------------------------        ----------------------
    #    1                                2
    # 1. `host1/apps1/practice_v1/model_helper/o1/mh_json/m_from_model_to_json_str.py`
    #                                                     ------------------------
    # 2. `1.` に含まれる関数

    from .m_from_model_to_json_str import from_model_to_json_str_with_indent
```

# Step 4. モデルヘルパー モジュール作成 - m_from_model_to_json_str フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                 # アプリケーション
                └── 📂 models_helper
                    └── 📂 o1
                        └── 📂 mh_json
                            ├── 📄 __init__.py
👉                          └── 📄 m_from_model_to_json_str.py
```

```py
import json
from django.core import serializers


def from_model_to_json_str(any_object):
    """モデルをJSON文字列に変換する"""
    return serializers.serialize('json', any_object)


def from_model_to_json_str_with_indent(any_object):
    """モデルをインデント付きでJSON文字列に変換する"""
    json_str = from_model_to_json_str(any_object)
    doc = json.loads(json_str)
    return json.dumps(doc, indent=4)
```

# Step 5. ビュー モジュール作成 - debug フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                 # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 o1
                │       └── 📂 mh_json
                │           ├── 📄 __init__.py
                │           └── 📄 m_from_model_to_doc.py
                └── 📂 views
                    └── 📂 o1
                        └── 📂 debug
👉                          └── 📄 __init__.py
```

```py
from django.http import HttpResponse

# JSONモデルヘルパー
from apps1.practice_v1.models_helper.mh_json import MhJson
#    ----- ----------- ---------------------        ------
#    1     2           3                            4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. クラス名

# 都道府県モデル
from apps1.practice_v1.models.o1.m_prefecture import Prefecture
#          -----------           ------------        ----------
#          1.1                   2                   3
#    ----------------------------------------
#    1
# 1. ディレクトリー
# 1.1 アプリケーション
# 2. Pythonファイル名 拡張子抜き
# 3. クラス名


class DebugV():
    """デバッグ ビュー"""

    @staticmethod
    def render_model_as_json(request):
        """描画 - モデルをダンプ出力する"""

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

# Step 6. ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                 # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 o1
        │       │       └── 📂 mh_json
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 m_from_model_to_doc.py
        │       └── 📂 views
        │           └── 📂 o1
        │               └── 📂 debug
        │                   └── 📄 __init__.py
        └── 📂 project1                      # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# デバッグ用。モデルをダンプ出力
from apps1.practice_v1.views.o1.debug import DebugV
#          -----------          -----        ------
#          11                   12           2
#    --------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [
    # ...略...


    # デバッグ用。モデルをダンプ出力
    path('practice/v1/from-object-to-json-str/',
         # -----------------------------------
         # 1
         DebugV.render_model_as_json, name='practice_v1_from_object_to_json_str'),
    #    ---------------------------        -----------------------------------
    #    2                                  3
    # 1. 例えば `http://example.com/practice/v1/from-object-to-json-str/` のような URL のパスの部分
    #                              ------------------------------------
    # 2. DebugV クラスの render_model_as_json 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_from_object_to_json_str' %} のような形でURLを取得するのに使える
]
```

# Step 7. Web画面へアクセス

📖 [http://localhost:8000/practice/v1/from-object-to-json-str/](http://localhost:8000/practice/v1/from-object-to-json-str/)  

# Step 8. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                    # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1
        │       ├── 📂 models_helper
        │       │   └── 📂 o1
        │       │       └── 📂 mh_json
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 m_from_model_to_doc.py
        │       └── 📂 views
        │           └── 📂 o1
        │               └── 📂 debug
        │                   └── 📄 __init__.py
        └── 📂 project1                      # プロジェクト
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
