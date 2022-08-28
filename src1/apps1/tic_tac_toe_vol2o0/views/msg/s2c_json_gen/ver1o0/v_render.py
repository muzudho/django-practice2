# BOF OA16o3o_2o0g3o0

import json
from django.shortcuts import render

# OA16o3o_2o0g1o_1o0 〇×ゲーム2.0巻 S2cメッセージ End 1.0版
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.end.ver1o0 import EndS2cMessage
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.moved.ver1o0 import MovedS2cMessage
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.start.ver1o0 import StartS2cMessage
#          ------------------                                       ------        ---------------
#          11                                                       12            2
#    ---------------------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス


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

        message_object_dict = {
            "S2C_End": EndS2cMessage(args),
            "S2C_Moved": MovedS2cMessage(args),
            "S2C_Start": StartS2cMessage(args),
        }

        if messageType in message_object_dict:
            doc = message_object_dict.get(messageType).asDict()
            dj_output_json = json.dumps(doc)
        else:
            # 空っぽのJSON文字列
            dj_output_json = "{}"

    else:
        # 空っぽのJSON文字列
        dj_output_json = "{}"

    context = {
        # `dj_` は Djangoでレンダーするパラメーター名の目印
        "dj_output_json": dj_output_json,
    }

    return render(request, template_path, context)

# EOF OA16o3o_2o0g3o0
