class EngineManual():
    """OA16o2o0gA14o0 エンジン手動"""

    path_of_local_html = "tic_tac_toe_v2/think/engine_manual/v1o0.html"
    #                     --------------------------------------------
    #                     1
    # 1. src1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/think/engine_manual/v1o0.html
    #                                        --------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_engine_manual
        #    ---------        --------------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_v2/views/think/engine_manual/v1o0/v_render.py`
        #                                                              --------
        # 2. `1.` に含まれる関数

        return render_engine_manual(request, EngineManual.path_of_local_html)
