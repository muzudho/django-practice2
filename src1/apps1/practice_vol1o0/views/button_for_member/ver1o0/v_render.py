# BOF O8o3o0g4o0

from django.shortcuts import render


def render_button_for_member(request, button_for_member_page_tp, path_of_portal, path_of_login_required, path_of_login, path_of_logout):
    """O8o3o0g4o0 描画 - 会員にだけ見えるボタンを説明するページ

    Parameters
    ----------
    button_for_member_page_tp : str
        Template path
    """

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        'dj_user': request.user,
        'dj_path_of_portal': path_of_portal,
        'dj_path_of_login_required': path_of_login_required,
        'dj_path_of_login': path_of_login,
        'dj_path_of_logout': path_of_logout,
    }
    return render(request, button_for_member_page_tp, context)

# EOF O8o3o0g4o0
