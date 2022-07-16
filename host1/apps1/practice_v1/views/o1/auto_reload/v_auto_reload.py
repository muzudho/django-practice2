from django.shortcuts import render


def render_auto_reload(request, path_of_reloader_page):
    """描画 - 自動再読込"""

    context = {
    }

    return render(request, path_of_reloader_page, context)
