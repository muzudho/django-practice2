class EngineManual():
    """エンジン手動"""

    _path_of_html = "tic_tac_toe_v2/o0o1/engine_manual.html"
    #                --------------------------------------
    #                1
    # 1. host1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/o0o1/engine_manual.html
    #                                         --------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_engine_manual
        #    ---------        --------------------
        #    1                2
        # 1. `host1/apps1/tic_tac_toe_v2/views/v2o0o1/engine_manual/v_render.py`
        #                                                           --------
        # 2. `1.` に含まれる関数

        return render_engine_manual(request, EngineManual._path_of_html)
