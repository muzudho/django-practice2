from django.shortcuts import render, redirect


def render_match_application(request, path_of_http_playing, path_of_html, on_sent, open):
    """対局申込 - 描画"""
    if request.method == "POST":
        # 送信後
        on_sent(request)

        # `po_` は POST送信するパラメーター名の目印
        po_room_name = request.POST.get("po_room_name")
        # 自分の番。 "X" か "O"。 機能拡張も想定
        my_turn = request.POST.get("po_my_turn")

        # TODO バリデーションチェックしたい

        return redirect(path_of_http_playing.format(po_room_name, my_turn))

    # 訪問後
    context = open(request)

    return render(request, path_of_html, context)
