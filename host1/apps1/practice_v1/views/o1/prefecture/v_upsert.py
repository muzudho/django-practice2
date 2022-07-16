from django.shortcuts import render, get_object_or_404, redirect

# 都道府県モデル
from apps1.practice_v1.models.o1.m_prefecture import Prefecture
#    ----- ----------- --------- ------------        ----------
#    1     2           3         4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

# 都道府県フォーム
from apps1.practice_v1.forms.f_prefecture import PrefectureForm
#    ----- ----------- ----- ------------        --------------
#    1     2           3     4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


def render_upsert(request, id=None):
    """新規作成または更新の画面の描画"""

    if id:  # idがあるとき（更新の時）
        # idで検索して、結果を戻すか、404エラー
        prefecture = get_object_or_404(Prefecture, pk=id)
    else:  # idが無いとき（作成の時）
        prefecture = Prefecture()

    # POSTの時（作成であれ更新であれ送信ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = PrefectureForm(request.POST, instance=prefecture)
        if form.is_valid():  # バリデーションがOKなら保存
            prefecture = form.save(commit=False)
            prefecture.save()
            return redirect('prefecture_list')
    else:  # GETの時（フォームを生成）
        form = PrefectureForm(instance=prefecture)

    # 作成・更新画面を表示
    return render(request, 'practice_v1/o1/prefecture/upsert.html', dict(form=form, id=id))
    #                       --------------------------------------
    #                       1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1/prefecture/upsert.html` を取得
    #                                    --------------------------------------
