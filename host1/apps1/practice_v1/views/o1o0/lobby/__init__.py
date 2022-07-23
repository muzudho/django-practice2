class LobbyV():
    """ロビー ビュー"""

    # 一覧ページ
    _path_of_lobby_page = "practice_v1/o1o0/lobby.html"
    #                      ---------------------------
    #                      1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1o0/lobby.html` を取得
    #                                       ---------------------------

    @staticmethod
    def render_lobby(request):
        """描画 - ロビー"""

        # 以下のファイルはあとで作ります
        from .v_lobby import render_lobby
        #    --------        ------------
        #    1               2
        # 1. `host1/apps1/practice_v1/views/o1o0/lobby/v_lobby.py`
        #                                              -------
        # 2. `1.` に含まれる関数

        return render_lobby(request, LobbyV._path_of_lobby_page)
