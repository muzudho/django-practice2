# BOF OA18o5o0g5o0

from django.shortcuts import get_object_or_404, redirect, render

# 部屋モデル
from apps1.practice_v1.models.room.v1o0 import Room
#          -----------             ----        ----
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 部屋フォーム
from apps1.practice_v1.forms.f_room import RoomForm
#          -----------       ------        --------
#          11                12            2
#    ------------------------------
#    10
# 10, 12. ディレクトリー名
# 11. アプリケーション名
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_upsert(request, id, room_upsert_tp):
    """OA18o5o0g5o0 新規作成または更新のページ

    Parameters
    ----------
    room_upsert_tp : str
        Template path
    """

    if id:  # idがあるとき（更新の時）
        # idで検索して、結果を戻すか、404エラー
        room = get_object_or_404(Room, pk=id)
    else:  # idが無いとき（作成の時）
        room = Room()

    # POSTの時（作成であれ更新であれ送信ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = RoomForm(request.POST, instance=room)

        # Valid なら保存して一覧画面へ
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('practice_v1_rooms')

        # Invalid ならフォームを引き継いで再び同じ画面表示へ

    else:  # GETの時（フォームを生成）
        form = RoomForm(instance=room)

    # 作成・更新画面を表示
    return render(request, room_upsert_tp, dict(form=form, id=id))

# EOF OA18o5o0g5o0
