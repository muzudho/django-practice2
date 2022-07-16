class ButtonForMember():
    """会員にだけ見えるボタンを説明するページ"""

    # そのページ
    _path_of_this_page = "practice_v1/o1/button_for_member.html"
    #                     --------------------------------------
    #                     1
    # 1. host1/apps1/portal/templates/practice_v1/o1/button_for_member.html を取得
    #                                 --------------------------------------

    # 既存のポータルページ
    _path_of_portal = "/"
    #                  -
    #                  1
    # 1. http://example.com:8000/ を取得
    #                           -

    # 既存のログイン必須ページ
    _path_of_login_required = "/practice/login-required"
    #                          ------------------------
    #                          1
    # 1. http://example.com/practice/login-required
    #                      ------------------------

    # 既存のログイン ページ
    _path_of_login = "/accounts/v1/login/"
    #                  -------------------
    #                  1
    # 1. http://example.com/accounts/v1/login/
    #                      -------------------

    # 既存のログアウト ページ
    _path_of_logout = "/accounts/v1/logout/"
    #                  --------------------
    #                  1
    # 1. http://example.com/accounts/v1/logout/
    #                      -------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_button_for_member
        #    ---------        ------------------------
        #    1                2
        # 1. `host1/apps1/portal/views/v0o0o1/button_for_member/v_render.py`
        #                                                       --------
        # 2. `1.` に含まれる関数

        return render_button_for_member(request, ButtonForMember._path_of_this_page, ButtonForMember._path_of_portal, ButtonForMember._path_of_login_required, ButtonForMember._path_of_login, ButtonForMember._path_of_logout)
