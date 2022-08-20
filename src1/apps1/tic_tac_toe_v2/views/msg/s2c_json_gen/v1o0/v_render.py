# BOF OA16o3o_2o0g3o0

from django.shortcuts import render


def render_main(request, template_path):
    """OA16o3o_2o0g3o0 S2C JSON ジェネレーター - 描画

    Parameters
    ----------
    template_path : str
        Template path
    """

    if request.method == "POST":
        # 送信後
        player1 = request.POST.get("po_player1")
        sq1 = request.POST.get("po_sq1")
        piece1 = request.POST.get("po_piece1")
        print(f"[render_main] player1:{player1} sq1:{sq1} piece1:{piece1}")
        # TODO バリデーションチェックしたい

    context = {
        # `dj_` は Djangoでレンダーするパラメーター名の目印
        "dj_output_json": "W.I.P",
    }

    return render(request, template_path, context)

# EOF OA16o3o_2o0g3o0
