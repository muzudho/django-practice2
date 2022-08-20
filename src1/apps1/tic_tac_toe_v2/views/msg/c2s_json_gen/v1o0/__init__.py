# BOF OA16o3o_1o0g3o0

class TesterV():
    """OA16o3o_1o0g3o0 テスター ビュー"""

    template_path = "tic_tac_toe_v2/msg/c2s_json_gen/v1o0.html"
    #                             ^two
    #                -----------------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/msg/c2s_json_gen/v1o0.html
    #                                        -----------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_main
        #    ---------        -----------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_v2/views/msg/c2s_json_gen/v1o0/v_render.py`
        #                                                           --------
        # 2. `1.` に含まれる関数

        return render_main(
            request,
            TesterV.template_path)

# EOF OA16o3o_1o0g3o0
