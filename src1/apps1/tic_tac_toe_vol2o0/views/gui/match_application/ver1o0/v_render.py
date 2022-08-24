# BOF OA16o3o0gA12o0

from django.shortcuts import render, redirect


def render_match_application(request, playing_web_path, match_application_tp, on_sent, on_open):
    """OA16o3o0gA12o0 対局申込 - 描画

    Parameters
    ----------
    match_application_tp : str
        Template path
    """
    if request.method == "POST":
        # 送信後
        on_sent(request)

        # `po_` は POST送信するパラメーター名の目印
        po_room_name = request.POST.get("po_room_name")
        # 自分の番。 "X" か "O"。 機能拡張も想定
        my_turn = request.POST.get("po_my_turn")

        # TODO バリデーションチェックしたい

        return redirect(playing_web_path.format(po_room_name, my_turn))

    # 訪問後
    context = on_open(request)

    return render(request, match_application_tp, context)

# EOF OA16o3o0gA12o0
