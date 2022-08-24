# BOF OA16o3o_1o0g3o0

class C2sJsonGenView():
    """OA16o3o_1o0g3o0 C2S Json ジェネレーター ビュー"""

    template_path = "tic_tac_toe_vol2o0/msg/c2s_json_gen/ver1o0.html"
    #                               ^two
    #                -----------------------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_vol2o0/templates/tic_tac_toe_vol2o0/msg/c2s_json_gen/ver1o0.html
    #                                            -----------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_main
        #    ---------        -----------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/msg/c2s_json_gen/ver1o0/v_render.py`
        #                                                                 --------
        # 2. `1.` に含まれる関数

        return render_main(
            request,
            C2sJsonGenView.template_path)

# EOF OA16o3o_1o0g3o0
