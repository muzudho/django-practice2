class MatchApplicationV():
    """対局申込ビュー"""

    # 〇×ゲーム v3o1
    _path_of_http_playing = "/tic-tac-toe/v3o1/playing/{0}/?&myturn={1}"
    #                                      ^^^three.one
    #                        ------------------------------------------
    #                        1
    # 1. http://example.com:8000/tic-tac-toe/v3o1/playing/Elephant/?&myturn=X
    #                           ---------------------------------------------

    # 〇×ゲーム v2
    path_of_html = "tic_tac_toe_v2/o1/gui/match_application.html"
    #                            ^two
    #               --------------------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/o1/gui/match_application.html` を取得
    #                                          --------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1.gui.match_application.v_render import render_match_application
        #                       ^two
        #    ------------------------------------------------------------        ------------------------
        #    1                                                                   2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o1/gui/match_application/v_render.py`
        #                                                               --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV._path_of_http_playing,
            MatchApplicationV.path_of_html,
            MatchApplicationV.on_sent,
            MatchApplicationV.open)

    @staticmethod
    def on_sent(request):
        """送信後"""

        # 何もしません
        pass

    @staticmethod
    def open(request):
        """訪問後"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1.gui.match_application import match_application_open_context
        #                       ^two
        #    ---------------------------------------------------        ------------------------------
        #    1                                                          2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o1/gui/match_application/__init__.py`
        #           ---------------------------------------------------
        # 2. `1.` の `__init__.py` ファイルに含まれる match_application_open_context 変数

        return match_application_open_context
