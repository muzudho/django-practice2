# サンプルを見る

📚 [この連載のレッスンのゴール：〇×ゲーム](http://tic.warabenture.com:8000/tic-tac-toe/v3.4/match-application/)  
📖 [この連載のレッスン終了後の自由課題の例：ライフゲーム](http://tic.warabenture.com:8000/lifegame/v0.3/board)  
📖 [この記事のゴール](http://tic.warabenture.com:8000/)  

# 情報

| What is        | This is                                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| この連載の目的 | ゲーム対局サーバーの **制作進行と自力実装** をしようという意欲のある人に対し、言うなれば高速道路のようなものを用意する |
| この記事の目標 | その目次                                                                                                               |

使うもの:  

* Python
* Django
* Docker
* Web Socket

# ここは目次

学習コストが低くなるように並べている。  
数字の小さな Lesson から　上から下へ１つずつ、飛ばさず全部　読み進めてほしい  

Lesson O1o0 Table of Contents  

* 📖 `O1o1o0 ゲーム対局サーバーを作ろう！` (この記事)  

Lesson O2o0 Install  

* 📖 [O2o1o0 DjangoをDockerコンテナへインストールしよう！](https://qiita.com/muzudho1/items/48e69ed17d70a8f171a7)
* 📖 [O2o2o0 本番環境のプロジェクトの作り方を予習しよう！](https://qiita.com/muzudho1/items/e9b8c1cefa5ddaa21ab2)

Lesson O3o0 Web page  

* 📖 [O3o1o0 Webページを追加しよう！](https://qiita.com/muzudho1/items/06fe071c1147b4b8f062)
* 📖 [o3o2o_1o0 URL設定を自動化しよう！](https://qiita.com/muzudho1/items/eed6f70c0c1502942738)
* 📖 [O3o2o0 HTMLのボイラープレートを減らすテンプレートを使おう！](https://qiita.com/muzudho1/items/7dcfc068e0bec009d371)
* 📖 [O3o3o0 HTMLのボイラープレートを減らすテンプレートを作るのも減らそう！](https://qiita.com/muzudho1/items/606d314c01543666c51b)

Lesson O4o0 Super-user  

* 📖 [O4o1o0 Djangoでスーパーユーザーを追加しよう！](https://qiita.com/muzudho1/items/cf21fa75e23e1f987153)

Lesson O5o0 Portal  

* 📖 [O5o1o0 ポータルページを作成しよう！](https://qiita.com/muzudho1/items/ad2299cf94a9a5b1c254)
* 📖 [O5o2o0 CSVとpandasを使ってPythonコードを編集しなくてもポータルページのリンクを増減できるようにしよう！](https://qiita.com/muzudho1/items/19c44296501c29c41d31)

Lesson O6o0 Auth, Sign up  

* 📖 [O6o1o0 ユーザー認証を付けよう！](https://qiita.com/muzudho1/items/55cb7ac55299afd51887)
  * もっと勉強したい人向けの関連記事
    * 📚 [Djangoで、django-allauthのテンプレートを差し替えよう！](https://qiita.com/muzudho1/items/6120055b2a8eb4e28527)

Lesson O7o0 Reset database

* 📖 [O7o1o0 dataフォルダーを壊してしまったときのリセット方法を覚えよう！](https://qiita.com/muzudho1/items/1ecaac80568c981fcd59)

Lesson O8o0 Auth, Log in/out  

※サインインとログイン、サインアウトとログアウトは、実装としては同じもの  

* 📖 [O8o1o0 ログイン（ユーザー認証）のページを作ろう！](https://qiita.com/muzudho1/items/1d34d64562ff07f1742a)
* 📖 [O8o2o0 ログインしていないと見れないページ，およびログアウト機能を付けよう！](https://qiita.com/muzudho1/items/9f1ae4d0debc0b8aa4b1)
* 📖 [O8o3o0 ログインしていない人には見えず、ログインしている人には見えるボタンを作ろう！](https://qiita.com/muzudho1/items/0c59f3ce7aa6bef2a91f)

Lesson O9o0 User, Extends User, and Active User  

* 📖 [O9o1o0 会員登録ユーザーを一覧しよう！](https://qiita.com/muzudho1/items/13c15be5b9070dab1770)
* 📖 [O9o2o0 Userモデルを拡張しよう！](https://qiita.com/muzudho1/items/2d182729f625234f0eff)
* 📖 [O9o3o0 アクティブユーザーの一覧を作ろう！](https://qiita.com/muzudho1/items/bea77e8a69c5c805e1d7)

Lesson OA10o0. Model  

* 📖 [OA10o1o0 モデルを追加しよう！](https://qiita.com/muzudho1/items/2463cc006da69f5ed7b2)
* 📖 [OA10o2o0 モデルの中身をダンプ出力しよう！](https://qiita.com/muzudho1/items/5db218ed0f12bae43d18)

Lesson OA11o0 CRUD  

* 📖 [OA11o1o0 モデルのインスタンスの一覧表示をしよう！](https://qiita.com/muzudho1/items/77668130b6d941596327)
* 📖 [OA11o2o0 モデルのインスタンスの読取ページを作成しよう！](https://qiita.com/muzudho1/items/ae362f53a670e265a7e4)
* 📖 [OA11o3o0 モデルのインスタンスの削除ページを作成しよう！](https://qiita.com/muzudho1/items/32694c883331c75ef059)
* 📖 [OA11o4o0 モデルのインスタンスの作成／更新ページを作成しよう！](https://qiita.com/muzudho1/items/806ecdba1654ae169f37)

Lesson OA12o0 Vuetify  

* 📖 [OA12o1o0 フロントエンドにVuetifyを使おう！](https://qiita.com/muzudho1/items/e80a72b027249daa4d41)
* 📖 [OA12o2o0 VuetifyのData tableを使おう！](https://qiita.com/muzudho1/items/2b01d3acce5ec1b5770b)
* 📖 [OA12o3o0 Vuetifyのテキストフィールドのバリデーションの練習をしよう！](https://qiita.com/muzudho1/items/fd47e589cd3f9449fcbb)

Lesson OA13o0 JSON  

* 📖 [OA13o1o0 Django のビューの Python スクリプトで JSON ファイルを読み込んで HTML に埋め込んでいる JavaScript にデータを渡そう！](https://qiita.com/muzudho1/items/b3b0c25fc329eb9bc0c1)
* 📖 [OA13o2o0 WebページへJSON形式のテキストを渡そう！](https://qiita.com/muzudho1/items/c50859d9bde800d06a62)
* 📖 [OA13o3o0 サーバーからデータをJSON形式のテキストで受信しよう！](https://qiita.com/muzudho1/items/d83760a6a4abadaf19c4)
* 📖 [OA13o4o0 データをサーバーへJSON形式で渡して、記憶させよう！](https://qiita.com/muzudho1/items/ed0ea262aaa327a2d12b)

Lesson OA14o0 Socket  

* 📖 [OA14o1o0 ソケットを使おう！](https://qiita.com/muzudho1/items/7a6501f7dbafbaa9b96c)

Lesson OA15o0 Web socket  

* 📖 [OA15o1o0 Webサーバーとクライアント側のアプリで通信しよう！](https://qiita.com/muzudho1/items/9bad88a4092bf83a0f12)
* 📖 [OA15o2o0 Webサーバーとクライアント側のアプリ間でJSON形式のテキストを通信しよう！](https://qiita.com/muzudho1/items/a3870c78f609a65debe0)

Lesson OA16o0 Tic tac toe  

* 📖 [OA16o1o0 Webブラウザ越しに２人対戦できる〇×ゲームを作ろう！](https://qiita.com/muzudho1/items/3bd5e55fbea2c0598e8b)
* 📖 [OA16o2o0 Tic-Tac-Toeの思考エンジンを作ろう！](https://qiita.com/muzudho1/items/69021deb9ec541406cfb)
* 📖 [DjangoとDocker練習OA16o3o_1o0 Tic-Tac-Toeのクライアントからサーバーへ送る通信メッセージを取り決めしよう！](https://qiita.com/muzudho1/items/931982d06927dd17e353)
* 📖 [DjangoとDocker練習OA16o3o_2o0 Tic-Tac-Toeのサーバーからクライアントへ送る通信メッセージを取り決めしよう！](https://qiita.com/muzudho1/items/b8522ca256e329977288)
* 📖 [OA16o3o0 Webブラウザ越しに２人対戦できる〇×ゲームを作ろう！ Vuetify編](https://qiita.com/muzudho1/items/f302bdb40fb5c13f9603)

Lesson OA17o0 Open server  

* 📖 [OA17o1o0 さくらVPS 備忘録](https://qiita.com/muzudho1/items/1d3b4b5608716463184c)
* 📖 [OA17o2o0 DjangoとDocker練習O17o2o0 gitでソースをクローンしよう！](https://qiita.com/muzudho1/items/7d4c35b58d6af20e3ceb)

Lesson OA18o0 Make room  

* 📖 [OA18o1o0 ゲーム対局部屋のモデルを定義しよう！](https://qiita.com/muzudho1/items/e1cf253dd6929bcd708d)
* 📖 [OA18o2o0 ゲーム対局部屋を一覧しよう！](https://qiita.com/muzudho1/items/346c286d4f99850afe23)
* 📖 [OA18o3o0 ゲーム対局部屋を読取しよう！](https://qiita.com/muzudho1/items/a39bea2f098951292916)
* 📖 [OA18o4o0 ゲーム対局部屋を削除しよう！](https://qiita.com/muzudho1/items/172485842e7adfb749aa)
* 📖 [OA18o5o0 ゲーム対局部屋を作成または更新しよう！](https://qiita.com/muzudho1/items/6eaf6cf90fe5a6519184)

Lesson OA19o0 User home  

* 📖 [OA19o1o0 ユーザーホームを作ろう！](https://qiita.com/muzudho1/items/37532c83235b7f9e60c9)

Lesson OA20o0 Lobby  

* 📖 [OA20o1o0 ロビー（待合室）を作ろう！](https://qiita.com/muzudho1/items/57677b07854aca71b42d)

Lesson OA21o0 Web page reload and redirect automatically  

* 📖 [OA21o1o0 自動リロードするページを作ろう！](https://qiita.com/muzudho1/items/8df599dc0e0acb25f649)
* 📖 [OA21o2o0 自動リダイレクトするページを作ろう！](https://qiita.com/muzudho1/items/aea9be36422763f082e9)

Lesson OA22o0 Reduce client-side functionality  

* 📖 [OA22o1o0 〇×ゲームのPlayAgainボタンを外そう！](https://qiita.com/muzudho1/items/d4bfde69c1656616f8ce)

Lesson OA23o0 Check-in  

* 📖 [OA23o1o0 チェックインを作ろう！](https://qiita.com/muzudho1/items/1ce542dd66929d7bce3f)

Lesson OA24o0 Monitor  

* 📖 [OA24o1o0 ゲーム対局部屋をモニターしよう！](https://qiita.com/muzudho1/items/e5e6e6ba76da401c4c00)

Lesson OA25o0 Watching game  

* 📖 [OA25o1o0 観戦モードを作ろう！](https://qiita.com/muzudho1/items/9e4a7dd1ccfac6ac8d66)

# 以下は自由課題

* 📖 [DjangoとDocker自由課題OAAA1001o1o0 ライフゲームを作ろう！](https://qiita.com/muzudho1/items/a2c90f8d3dfaad849211)
* 📖 [DjangoとDocker自由課題OAAA1001o1o0ga12o_1o0 ライフゲームの思考エンジンを作ろう！](https://qiita.com/muzudho1/items/4ec5896c7a8fb27161ff)
* 📖 [DjangoとDocker自由課題OAAA1001o1o0ga13o__10o0 ライフゲームのGUIを作ろう！](https://qiita.com/muzudho1/items/01d2482576f8ca8d7e0e)
