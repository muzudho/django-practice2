from django.shortcuts import render, get_object_or_404, redirect

from apps1.practice.models.m_prefecture import Prefecture
#    ----- -------- ------ ------------        ----------
#    1     2        3      4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

from apps1.practice.forms.f_prefecture import PrefectureForm
#    ----- -------- ----- ------------        --------------
#    1     2        3     4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


class PrefectureUpsertV():
    """都道府県の新規作成または更新ビュー"""

    def render(request, id=None):
        """描画"""

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
        return render(request, 'practice/v0o0o1/prefecture/upsert.html', dict(form=form, id=id))
        #                       --------------------------------------
        #                       1
        # 1. `host1/apps1/practice/templates/practice/v0o0o1/prefecture/upsert.html` を取得
        #                                    --------------------------------------
