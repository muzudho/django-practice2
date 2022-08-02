from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


class LoggingIn():
    """O8o2o0g3o0 ログイン中"""

    # * `lp_` - Local path
    lp_login_required = "practice_v1/login_required/v1o0.html"
    #                    ------------------------------------
    #                    1
    # 1. src1/apps1/practice_v1/templates/practice_v1/login_required/v1o0.html を取得
    #                                     ------------------------------------

    # 👇 このデコレーターを付けると、ログインしていないなら、 settings.py の LOGIN_URL で指定した URL に飛ばします。
    # インスタンスのメソッドや、クラスメソッドには付けられません。
    # 第一引数が self や clazz でないことに注意してください
    @login_required
    def render(request):
        """描画"""
        return loggingIn_render(request, LoggingIn.lp_login_required)


class LoggingOut():
    """O8o2o0g3o0 ログアウト中"""

    def render(request):
        """描画"""
        return loggingOut_render(request)


# 以下、関数


def loggingIn_render(request, lp_login_required):
    """O8o2o0g3o0 ログイン中 - 描画

    Parameters
    ----------
    request : object
        リクエスト
    lp_login_required : str
        ローカルパス
    """

    user = request.user
    context = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }
    return render(request, lp_login_required, context)


def loggingOut_render(request):
    """O8o2o0g3o0 ログアウト中 - 描画"""
    logout(request)  # Django の認証機能のログアウトを使う
    return redirect('home')  # ホームに戻る
