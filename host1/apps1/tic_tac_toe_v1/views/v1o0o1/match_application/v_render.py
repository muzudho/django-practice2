from django.shortcuts import render, redirect


def render_match_application(request, path_of_http_playing, path_of_html):
    """描画 - 対局申込"""

    if request.method == "POST":
        # 送信後
        room_name = request.POST.get("room_name")
        myPiece = request.POST.get("my_piece")
        # TODO バリデーションチェックしたい
        return redirect(path_of_http_playing.format(room_name, myPiece))

    # 訪問後
    return render(request, path_of_html, {})
