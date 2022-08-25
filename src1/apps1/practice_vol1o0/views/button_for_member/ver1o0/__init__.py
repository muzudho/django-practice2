# BOF O8o3o0g3o0

class ButtonForMember():
    """O8o3o0g3o0 会員にだけ見えるボタンを説明するページ"""

    # そのページ
    _path_of_this_page = "practice_vol1o0/button_for_member/ver1o0.html"
    #                     ---------------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/button_for_member/ver1o0.html` を取得
    #                                          ---------------------------------------------

    # 既存のポータルページ
    _path_of_portal = "/"
    #                  -
    #                  1
    # 1. http://example.com:8000/ を取得
    #                           -

    # 既存のログイン必須ページ
    _path_of_login_required = "/practice/vol1o0/login-required/ver1o0/"
    #                          ---------------------------------------
    #                          1
    # 1. `http://example.com/practice/vol1o0/login-required/ver1o0/`
    #                       ---------------------------

    # 既存のログイン ページ
    _path_of_login = "/accounts/vol1.0/login/"
    #                 -----------------------
    #                 1
    # 1. http://example.com/accounts/vol1.0/login/
    #                      -----------------------

    # 既存のログアウト ページ
    _path_of_logout = "/accounts/vol1.0/logout/"
    #                  ------------------------
    #                  1
    # 1. http://example.com/accounts/vol1.0/logout/
    #                      ------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_button_for_member
        #    ---------        ------------------------
        #    1                2
        # 1. `src1/apps1/practice_vol1o0/views/button_for_member/ver1o0/v_render.py`
        #                                                               --------
        # 2. `1.` に含まれる関数

        return render_button_for_member(request, ButtonForMember._path_of_this_page, ButtonForMember._path_of_portal, ButtonForMember._path_of_login_required, ButtonForMember._path_of_login, ButtonForMember._path_of_logout)

# EOF O8o3o0g3o0
