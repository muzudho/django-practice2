class VuetifyV(object):
    """OA12o1o0g4o0 ビューティファイの練習のビュー"""

    # OA12o1o0g4o0 こんにちわ
    from .hello.ver1o0 import render_hello1

    # OA12o2o0g4o0 データテーブル１
    from .data_table1.ver1o0 import render_data_table1

    # OA12o3o0g4o0 バリデーション１
    from .validation1.ver1o0 import render_validation1

    # OA13o1o0g5o0 デザート１
    from .dessert1.ver1o0 import render_desserts1

    # OA13o2o0g6o0 テキストエリア１
    from .textarea1.ver1o0 import render_textarea1, render_desserts1_from_textarea1

    # OA13o3o0g4o0 JSONでデザート１
    from .desserts1_as_json.ver1o0 import render_desserts1_as_json

    # OA13o4o0gA12o0 テキストエリア入力から保存まで
    from .textarea1_to_model.ver1o0 import render_textarea1_to_model, render_save_result_of_desserts1_from_textarea1
