class LobbyV():
    """OA20o1o0g5o0 ロビー ビュー"""

    # 一覧ページ
    _path_of_lobby_page = "practice_v1/lobby/v1o0.html"
    #                      ---------------------------
    #                      1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/lobby/v1o0.html` を取得
    #                                      ---------------------------

    @staticmethod
    def render_lobby(request):
        """描画 - ロビー"""

        # 以下のファイルはあとで作ります
        from .v_lobby import render_lobby
        #    --------        ------------
        #    1               2
        # 1. `src1/apps1/practice_v1/views/lobby/v1o0/v_lobby.py`
        #                                             -------
        # 2. `1.` に含まれる関数

        return render_lobby(request, LobbyV._path_of_lobby_page)
