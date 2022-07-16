# 目的

モデルの中身を全部見たい。  
デバッグモードなら、エラー画面で変数の内容を見れるが、エラーじゃないときも見たい  

# 手段

モデルを、JSON形式にシリアライズ（出力）する  

# はじめに

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    │   │   ├── 📂 allauth_customized    # アプリケーション
    │   │   ├── 📂 portal                # アプリケーション
    │   │   │   ├── 📂 data
    │   │   │   │   └── 📄 finished-lesson.csv
    │   │   │   ├── 📂 migrations
    │   │   │   │   └── 📄 __init__.py
    │   │   │   ├── 📂 static
    │   │   │   │   └── 🚀 favicon.ico
    │   │   │   ├── 📂 templates
    │   │   │   │   └── 📂 portal
    │   │   │   │       └── 📂 v0o0o1
    │   │   │   │           └── 📄 portal_base.html
    │   │   │   └── 📂 views
    │   │   │       └── 📂 v0o0o1
    │   │   │           └── 📄 pages.py
    │   │   └── 📂 practice              # アプリケーション
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

# Step 2. モデルヘルパー モジュール作成 - mh_json フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice                 # アプリケーション
                └── 📂 models_helper
                    └── 📂 mh_json
👉                      └── 📄 __init__.py
```

```py
class MhJson():
    """JSONモデルヘルパー"""

    # 以下のファイルはあとで作ります
    from .m_from_model_to_json_str import from_model_to_json_str
    #    -------------------------        ----------------------
    #    1                                2
    # 1. `host1/apps1/practice/model_helper/mh_json/m_from_model_to_json_str.py`
    #                                               ------------------------
    # 2. `1.` に含まれる関数
```

# Step 3. モデルヘルパー モジュール作成 - m_from_model_to_json_str フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice                 # アプリケーション
                └── 📂 models_helper
                    └── 📂 mh_json
                        ├── 📄 __init__.py
👉                      └── 📄 m_from_model_to_json_str.py
```

```py
from django.core import serializers


def from_model_to_json_str(model):
    """モデルをJSON文字列に変換する"""
    return serializers.serialize('json', model)
```

# Step 4. ビュー モジュール作成 - debug フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice                 # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 mh_json
                │       ├── 📄 __init__.py
                │       └── 📄 m_from_model_to_doc.py
                └── 📂 views
                    └── 📂 v0o0o1
                        └── 📂 debug
👉                          └── 📄 __init__.py
```

```py
from django.http import HttpResponse

from apps1.practice.models_helper.mh_json import MhJson
#    ----- -------- ---------------------        ------
#    1     2        3                            4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. クラス名

from apps1.practice.models.v0o0o1.m_prefecture import Prefecture
#          --------               ------------        ----------
#          1.1                    2                   3
#    ----------------------------
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
        json_str = MhJson.from_model_to_json_str(prefecture_resultset)
        return HttpResponse(json_str)
```

# Step 5. ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice                 # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 mh_json
        │       │       ├── 📄 __init__.py
        │       │       └── 📄 m_from_model_to_doc.py
        │       └── 📂 views
        │           └── 📂 v0o0o1
        │               └── 📂 debug
        │                   └── 📄 __init__.py
        └── 📂 project1                      # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# デバッグ用。モデルをダンプ出力
from apps1.practice.views.v0o0o1.debug import DebugV
#          --------              -----        ------
#          1.1                   1.2          2
#    ---------------------------------
#    1
# 1. ディレクトリー
# 1.1 アプリケーション
# 1.2 ディレクトリー
# 2. `1.2` に含まれる __init__.py ファイルにさらに含まれる クラス名


urlpatterns = [
    # ...略...


    # デバッグ用。モデルをダンプ出力
    path('practice/from-object-to-json-str/',
         # -------------------------------
         # 1
         DebugV.render_model_as_json, name='practice_from_model_to_json_str'),
    #    ---------------------------        -------------------------------
    #    2                                  3
    # 1. 例えば `http://example.com/practice/from-object-to-json-str/` のような URL のパスの部分
    #                              --------------------------------
    # 2. DebugV クラスの render_model_as_json 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_from_model_to_json_str' %} のような形でURLを取得するのに使える
]
```

# Step 6. Web画面へアクセス

📖 [http://localhost:8000/practice/from-object-to-json-str/](http://localhost:8000/practice/from-object-to-json-str/)  

# Step 7. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal                    # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice
        │       ├── 📂 models_helper
        │       │   └── 📂 mh_json
        │       │       ├── 📄 __init__.py
        │       │       └── 📄 m_from_model_to_doc.py
        │       └── 📂 views
        │           └── 📂 v0o0o1
        │               └── 📂 debug
        │                   └── 📄 __init__.py
        └── 📂 project1                      # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/from-object-to-json-str/,モデルをダンプ出力する
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでモデルのインスタンスの一覧表示をしよう！](https://qiita.com/muzudho1/items/77668130b6d941596327)  
