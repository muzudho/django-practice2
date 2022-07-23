from django.shortcuts import render, get_object_or_404, redirect

# 都道府県モデル
from apps1.practice_v1.models.o1o0.m_prefecture import Prefecture
#          -----------             ------------        ----------
#          11                      12                  2
#    ------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 都道府県フォーム
from apps1.practice_v1.forms.f_prefecture import PrefectureForm
#          -----------       ------------        ----------
#          11                12                  2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


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
            return redirect('practice_v1_prefectures')
    else:  # GETの時（フォームを生成）
        form = PrefectureForm(instance=prefecture)

    # 作成・更新画面を表示
    return render(request, 'practice_v1/o1o0/prefecture/upsert.html', dict(form=form, id=id))
    #                       ---------------------------------------
    #                       1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1o0/prefecture/upsert.html` を取得
    #                                       ---------------------------------------
