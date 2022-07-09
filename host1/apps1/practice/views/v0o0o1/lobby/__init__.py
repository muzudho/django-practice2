class LobbyV():
    """ロビー ビュー"""

    # 一覧ページ
    _path_of_lobby_page = "practice/v0o0o1/lobby.html"
    #                      --------------------------
    #                      1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/lobby.html` を取得
    #                                    --------------------------

    @staticmethod
    def render_lobby(request):
        """描画 - ロビー"""

        # 以下のファイルはあとで作ります
        from .v_lobby import render_lobby
        #    --------        ------------
        #    1               2
        # 1. `host1/apps1/practice/views/v0o0o1/lobby/v_lobby.py`
        #                                             -------
        # 2. `1.` に含まれる関数

        return render_lobby(request, LobbyV._path_of_lobby_page)
