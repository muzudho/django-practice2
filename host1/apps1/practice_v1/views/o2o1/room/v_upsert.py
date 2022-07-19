from django.shortcuts import render, get_object_or_404, redirect

# 部屋モデル
from apps1.practice_v1.models.o2o1.m_room import Room
#    ----- ----------- ----------- ------        ----
#    1     2           3           4             5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

# 部屋フォーム
from apps1.practice_v1.forms.f_room import RoomForm
#    ----- ----------- ----- ------        --------
#    1     2           3     4             5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


@staticmethod
def render_upsert(request, id, path_of_upsert_page):
    """新規作成または更新のページ"""

    if id:  # idがあるとき（更新の時）
        # idで検索して、結果を戻すか、404エラー
        room = get_object_or_404(Room, pk=id)
    else:  # idが無いとき（作成の時）
        room = Room()

    # POSTの時（作成であれ更新であれ送信ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():  # バリデーションがOKなら保存
            room = form.save(commit=False)
            room.save()
            return redirect('practice_v1_rooms')
    else:  # GETの時（フォームを生成）
        form = RoomForm(instance=room)

    # 作成・更新画面を表示
    return render(request, path_of_upsert_page, dict(form=form, id=id))
