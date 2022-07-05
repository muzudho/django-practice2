from django.http import HttpResponse
from django.template import loader


def render_button_for_member(request, path_of_this_page, path_of_portal, path_of_login_required, path_of_login, path_of_logout):
    """描画 - 会員にだけ見えるボタンを説明するページ"""

    template = loader.get_template(path_of_this_page)

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        'dj_user': request.user,
        'dj_path_of_portal': path_of_portal,
        'dj_path_of_login_required': path_of_login_required,
        'dj_path_of_login': path_of_login,
        'dj_path_of_logout': path_of_logout,
    }
    return HttpResponse(template.render(context, request))
