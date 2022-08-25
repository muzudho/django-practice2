# BOF OA20o1o0g5o0

class LobbyV():
    """OA20o1o0g5o0 ロビー ビュー"""

    # 一覧ページ
    _path_of_lobby_page = "practice_vol1o0/lobby/ver1o0.html"
    #                      ---------------------------------
    #                      1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/lobby/ver1o0.html` を取得
    #                                          ---------------------------------

    @staticmethod
    def render_lobby(request):
        """描画 - ロビー"""

        # 以下のファイルはあとで作ります
        from .v_lobby import render_lobby
        #    --------        ------------
        #    1               2
        # 1. `src1/apps1/practice_vol1o0/views/lobby/ver1o0/v_lobby.py`
        #                                                   -------
        # 2. `1.` に含まれる関数

        return render_lobby(request, LobbyV._path_of_lobby_page)

# EOF OA20o1o0g5o0
