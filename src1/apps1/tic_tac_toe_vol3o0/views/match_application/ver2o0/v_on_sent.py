# 部屋モデル
from apps1.practice_v1.models.room.v1o0 import Room
#          -----------             ----        ----
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# ユーザー拡張
from apps1.practice_v1.models.user_profile.v1o0 import Profile
#          -----------                     ----        -------
#          11                              12          2
#    ------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def match_application_on_sent(request):
    """OA23o1o0g3o0 対局申込 - 送信後

    * ログインしていないユーザーが部屋に入っても 何も記録しません
    * ログインしているユーザーが部屋に入ってくると、以下のものを記録します（チェックイン）
    * Room.sente_id または Room.gote_id の空いている方に user.pk を上書き
    * user.profile.match_state を 3 （対局中）に上書き
    """

    # `po_` は POST送信するパラメーター名の目印
    # 部屋名
    po_room_name = request.POST.get("po_room_name")
    # 自分の番。 "X" か "O"。 機能拡張も想定
    my_turn = request.POST.get("po_my_turn")

    # 部屋の取得 または 新規作成
    #
    # * ID ではなく、部屋名から行う
    room_table_qs = Room.objects.filter(name=po_room_name)

    if 1 <= len(room_table_qs):
        # （名前被りがあったなら）先頭の１つを取得
        room = room_table_qs[0]
    else:
        # 新規作成
        room = Room()
        room.name = po_room_name

    if request.user.is_authenticated:
        # ログインしたユーザーだった

        user_pk = request.user.pk

        # 自分の Profile レコード 取得
        profile = Profile.objects.get(user__pk=user_pk)
        #                             --------
        #                             1
        # 1. Profile テーブルと 1対1 で紐づいている親テーブル User の pk フィールド

        if my_turn == "X":
            # X を取った方は先手とします
            room.sente_id = user_pk
            # ユーザーの状態を対局中（3）にします
            profile.match_state = 3

        elif my_turn == "O":
            # O を取った方は後手とします
            #
            # * 先手と後手が同じユーザーでも構わないものとします
            room.gote_id = user_pk
            # ユーザーの状態を対局中（3）にします
            profile.match_state = 3

        else:
            # それ以外は観戦者として扱う
            # ユーザーの状態を観戦中（4）にします
            profile.match_state = 4

        # 先手と後手の両方が埋まったなら
        if not(room.sente_id is None or room.sente_id == 0 or room.gote_id is None or room.gote_id == 0):
            # 盤と棋譜を空っぽにする
            room.board = ""
            room.record = ""

        # TODO バリデーションチェック
        room.save()

        # TODO バリデーションチェック
        profile.save()

        # print(f"[match_application_on_sent] ★ 更新終わり")
    else:
        # ゲストだった
        # print(f"[match_application_on_sent] ★ ゲスト")
        pass
