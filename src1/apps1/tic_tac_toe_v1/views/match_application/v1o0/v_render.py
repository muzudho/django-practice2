from django.shortcuts import render, redirect


def render_match_application(request, upf_playing, lp_match_application):
    """OA16o1o0gA14o0 描画 - 対局申込

    Parameters
    ----------
    upf_playing : str
        Url Path Format
    lp_match_application : str
        Local Path
    """

    if request.method == "POST":
        # 送信後
        room_name = request.POST.get("room_name")
        myPiece = request.POST.get("my_piece")
        # TODO バリデーションチェックしたい
        return redirect(upf_playing.format(room_name, myPiece))

    # 訪問後
    return render(request, lp_match_application, {})
