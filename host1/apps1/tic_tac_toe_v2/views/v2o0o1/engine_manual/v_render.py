from django.shortcuts import render


def render_engine_manual(request, path_of_html):
    """描画 - エンジン手動"""

    context = {}

    return render(request, path_of_html, context)
