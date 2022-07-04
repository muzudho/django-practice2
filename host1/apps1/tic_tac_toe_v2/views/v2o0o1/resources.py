"""〇×ゲームの練習２．０．１"""
from django.shortcuts import render


class EngineManual():
    """エンジン手動"""

    _path_of_html = "tic_tac_toe_v2/o0o1/engine_manual.html"
    #                --------------------------------------
    #                1
    # 1. host1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/o0o1/engine_manual.html
    #                                         --------------------------------------

    @staticmethod
    def render(request):
        """描画"""
        return render_match_application(request, EngineManual._path_of_html)


# 以下、関数


def render_match_application(request, path_of_html):
    """対局申込 - 描画"""

    context = {}

    return render(request, path_of_html, context)
