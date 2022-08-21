from django.urls import path

# O3o1o0gA10o0 こんにちわページ
from apps1.practice_v1.views.page_the_hello.v1o0 import PageTheHello
#          -----------                      ----        ------------
#          11                               12          2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# O8o2o0g4o0 ログイン必須ページ
from apps1.practice_v1.views.login_required.v1o0 import LoggingIn, LoggingOut
#          -----------                      ----        ---------------------
#          11                               12          2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# O8o3o0g5o0 会員用ボタン
from apps1.practice_v1.views.button_for_member.v1o0 import ButtonForMember
#          -----------                         ----        ---------------
#          11                                  12          2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# OA20o1o0g7o0 ロビー ビュー
from apps1.practice_v1.views.lobby.v1o0 import LobbyV
#          -----------             ----        ------
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# OA21o1o0g7o0 自動リロード ビュー
from apps1.practice_v1.views.auto_reload.v1o0 import AutoReloadV
#          -----------                   ----        -----------
#          11                            12          2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# OA21o2o0g6o0 自動リダイレクト ビュー
from apps1.practice_v1.views.auto_redirect.v1o0 import AutoRedirectV
#          -----------                     ----        -------------
#          11                              12          2
#    ------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# OA22o1o0gA10o0 〇×ゲーム v3.1 対局申込中
from apps1.tic_tac_toe_v3.views.match_application.v1o0 import MatchApplicationV as TicTacToeV3g1o0MatchApplicationV
#                       ^three                     ^one
#          --------------                         ----        -----------------    --------------------------------
#          11                                     12          2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# OA22o1o0gA10o0 〇×ゲーム v3.1 対局中
from apps1.tic_tac_toe_v3.views.playing.v1o0 import PlayingV as TicTacToeV3g1o0PlayingV
#                       ^three           ^one
#          --------------               ----        --------    -----------------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# OA23o1o0g4o0 〇×ゲーム v3.2 対局申込中
from apps1.tic_tac_toe_v3.views.match_application.v2o0 import MatchApplicationV as TicTacToeV3g2o0MatchApplicationV
#                       ^three                     ^two
#          --------------                         ----        -----------------    --------------------------------
#          11                                     12          2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# OA24o1o0g8o0 〇×ゲーム v3.3 対局申込中
from apps1.tic_tac_toe_v3.views.match_application.v3o0 import MatchApplicationV as TicTacToeV3g3o0MatchApplicationV
#                       ^three                     ^three
#          --------------                         ----        -----------------    --------------------------------
#          11                                     12          2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# OA24o1o0g8o0 〇×ゲーム v3.3 対局中
from apps1.tic_tac_toe_v3.views.playing.v3o0 import PlayingV as TicTacToeV3g3o0PlayingV
#                       ^three           ^three
#          ----------------             ----        --------    -----------------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# OA25o1o0g5o0 〇×ゲーム v3.4 対局申込中
from apps1.tic_tac_toe_v3.views.match_application.v4o0 import MatchApplicationV as TicTacToeV3g4o0MatchApplicationV
#                       ^three                     ^four
#          --------------                         ----        -----------------    --------------------------------
#          11                                     12          2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# OA25o1o0g5o0 〇×ゲーム v3.4 対局中
from apps1.tic_tac_toe_v3.views.playing.v4o0 import PlayingV as TicTacToeV3g4o0PlayingV
#                       ^three           ^four
#          --------------               ----        --------    -----------------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # O3o1o0gA10o0 こんにちわページ
    path('practice/v1/page-the-hello',
         # -------------------------
         # 1
         PageTheHello.render, name='page_the_hello'),
    #    -------------------        --------------
    #    2                          3
    # 1. 例えば `http://example.com/practice/v1/page-the-hello` のようなURLのパスの部分
    #                              --------------------------
    # 2. PageTheHello クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page_the_hello' %} のような形でURLを取得するのに使える

    # O8o2o0g4o0 ログイン中
    path('practice/v1/login-required', LoggingIn.render,
         # -------------------------   ----------------
         # 1                           2
         name='practice_v1_login_required'),
    #          --------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/login-required` のような URL のパスの部分
    #                              --------------------------
    # 2. LoggingIn クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_login_required' %} のような形でURLを取得するのに使える

    # O8o2o0g4o0 ログアウト中
    path('practice/v1/logout', LoggingOut.render,
         # -----------------   -----------------
         # 1                   2
         name='practice_v1_logout'),
    #          ------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/logout` のような URL のパスの部分
    #                              ------------------
    # 2. LoggingOut クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_logout' %} のような形でURLを取得するのに使える

    # O8o3o0g5o0 会員にだけ見えるボタンを説明するページ
    path('practice/v1/buttom_for_member/',
         # -----------------------------
         # 1
         ButtonForMember.render),
    #    ----------------------
    #    2
    # 1. 例えば `http://example.com/practice/v1/buttom_for_member/` のような URL のパスの部分
    #                              ------------------------------
    # 2. ButtonForMember クラスの render 静的メソッド

    # OA20o1o0g7o0 ロビー
    path('practice/v1/lobby/', LobbyV.render_lobby, name='practice_v1_lobby'),
    #     ------------------   -------------------        -----------------
    #     1                    2                          3
    # 1. 例えば `http://example.com/practice/v1/lobby/` のような URL のパスの部分
    #                              ------------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. LobbyV クラスの render_lobby 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_lobby' %} のような形でURLを取得するのに使える

    # OA21o1o0g7o0 自動再読込
    path('practice/v1/auto_reload/', AutoReloadV.render_auto_reload,
         # -----------------------   ------------------------------
         # 1                         2
         name='practice_v1_auto_reload'),
    #          -----------------------
    #          3
    #
    # 1. 例えば `http://example.com/practice/v1/auto_reload/` のような URL のパスの部分
    #                              ------------------------
    # 2. AutoReloadV クラスの render_auto_reload 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_auto_reload' %} のような形でURLを取得するのに使える

    # OA21o2o0g6o0 自動リダイレクト
    path('practice/v1/auto_redirect/', AutoRedirectV.render_auto_redirect,
         # -------------------------   ----------------------------------
         # 1                           2
         name='practice_v1_auto_redirect'),
    #          -------------------------
    #          3
    #
    # 1. 例えば `http://example.com/practice/v1/auto_redirect/` のような URL のパスの部分
    #                              --------------------------
    # 2. AutoRedirectV クラスの render_auto_redirect メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_auto_redirect' %} のような形でURLを取得するのに使える

    # OA22o1o0gA10o0 〇×ゲーム v3.1 対局申込中
    path('tic-tac-toe/v3.1/match-application/', TicTacToeV3g1o0MatchApplicationV.render,
         # ----------------------------------   ---------------------------------------
         # 1                                    2
         name='tic_tac_toe_v3g1o0_match_application'),
    #          ------------------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3.1/match-application/` のような URL のパスの部分
    #                              -----------------------------------
    # 2. TicTacToeV3g1o0MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g1o0_match_application' %} のような形でURLを取得するのに使える

    # OA22o1o0gA10o0 〇×ゲーム v3.1 対局中
    path('tic-tac-toe/v3.1/playing/<str:kw_room_name>/', TicTacToeV3g1o0PlayingV.render,
         # -------------------------------------------   ------------------------------
         # 1                                             2
         name='tic_tac_toe_v3g1o0_playing'),
    #          --------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3.1/playing/<部屋名>/` のような URL のパスの部分
    #                              ----------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3g1o0PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g1o0_playing' %} のような形でURLを取得するのに使える

    # OA23o1o0g4o0 〇×ゲーム v3.2 対局申込中
    path('tic-tac-toe/v3.2/match-application/', TicTacToeV3g2o0MatchApplicationV.render,
         # ----------------------------------   ---------------------------------------
         # 1                                    2
         name='tic_tac_toe_v3g2o0_match_application'),
    #          ------------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3.2/match-application/` のような URL のパスの部分
    #                              -------------------------------------
    # 2. TicTacToeV3g2o0MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g2o0_match_application' %} のような形でURLを取得するのに使える

    # OA24o1o0g8o0 〇×ゲーム v3.3 対局申込中
    path('tic-tac-toe/v3.3/match-application/', TicTacToeV3g3o0MatchApplicationV.render,
         # ----------------------------------   ---------------------------------------
         # 1                                    2
         name='tic_tac_toe_v3g3o0_match_application'),
    #          ------------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3.3/match-application/` のような URL のパスの部分
    #                              -----------------------------------
    # 2. TicTacToeV3g3o0MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g3o0_match_application' %} のような形でURLを取得するのに使える

    # OA24o1o0g8o0 〇×ゲーム v3.3 対局中
    path('tic-tac-toe/v3.3/playing/<str:kw_room_name>/', TicTacToeV3g3o0PlayingV.render,
         # -------------------------------------------   ------------------------------
         # 1                                             2
         name='tic_tac_toe_v3g3o0_playing'),
    #          --------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3.3/playing/<部屋名>/` のような URL のパスの部分
    #                              ----------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3g3o0PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g3o0_playing' %} のような形でURLを取得するのに使える

    # OA25o1o0g5o0 〇×ゲーム v3.4 対局申込中
    path('tic-tac-toe/v3.4/match-application/', TicTacToeV3g4o0MatchApplicationV.render,
         # ----------------------------------   ---------------------------------------
         # 1                                    2
         name='tic_tac_toe_v3g4o0_match_application'),
    #          --------------------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3.4/match-application/` のような URL のパスの部分
    #                              -----------------------------------
    # 2. TicTacToeV3g4o0MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g4o0_match_application' %} のような形でURLを取得するのに使える

    # OA25o1o0g5o0 〇×ゲーム v3.4 対局中
    path('tic-tac-toe/v3.4/playing/<str:kw_room_name>/', TicTacToeV3g4o0PlayingV.render,
         # -------------------------------------------   ------------------------------
         # 1                                             2
         name='tic_tac_toe_v3g4o0_playing'),
    #          ----------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3.4/playing/<部屋名>/` のような URL のパスの部分
    #                              ----------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3g4o0PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g4o0_playing' %} のような形でURLを取得するのに使える
]
