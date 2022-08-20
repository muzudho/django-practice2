# BOF OA16o3o_1o0g2o0

from django.shortcuts import render, redirect


def render_tester(request, room_name, template_path, on_open, on_sent):
    """OA16o3o_1o0g2o0 テスター - 描画

    Parameters
    ----------
    tester_tp : str
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

        return redirect(template_path.format(po_room_name, my_turn))

    # 訪問後
    context = on_open(request)

    turn = request.GET.get("myturn")

    return render(request, template_path.format(room_name, turn), context)

# EOF OA16o3o_1o0g2o0
