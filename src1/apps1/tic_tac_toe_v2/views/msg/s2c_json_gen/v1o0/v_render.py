# BOF OA16o3o_2o0g3o0

import json
from django.shortcuts import render

# OA16o3o_2o0g1o0 S2C JSON ジェネレーター
from apps1.tic_tac_toe_v2.views.msg.s2c_json_gen.commands.v1o0 import S2cJsonGenCommands as CommandsGen
#          --------------                                 ----        ------------------    -----------
#          11                                             12          2                     3
#    ---------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス
# 3. `2.` の別名


def render_main(request, template_path):
    """OA16o3o_2o0g3o0 S2C JSON ジェネレーター - 描画

    Parameters
    ----------
    template_path : str
        Template path
    """

    if request.method == "POST":
        # 送信後

        messageType = request.POST.get("po_messageType")
        args = {
            "player1": request.POST.get("po_player1"),
            "sq1": request.POST.get("po_sq1"),
            "piece1": request.POST.get("po_piece1"),
        }
        # print(
        #     f'[render_main] messageType:{messageType} player1:{args["player1"]} sq1:{args["sq1"]} piece1:{args["piece1"]}')
        # TODO バリデーションチェックしたい

        json_gen = {
            "S2C_End": CommandsGen.create_end,
            "S2C_Moved": CommandsGen.create_moved,
            "S2C_Start": CommandsGen.create_start,
        }

        doc = json_gen.get(messageType)(args)
        dj_output_json = json.dumps(doc)

    else:
        # 空っぽのJSON文字列
        dj_output_json = "{}"

    context = {
        # `dj_` は Djangoでレンダーするパラメーター名の目印
        "dj_output_json": dj_output_json,
    }

    return render(request, template_path, context)

# EOF OA16o3o_2o0g3o0
