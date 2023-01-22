# BOF [OA16o3o0gA16o0]

# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# [OA16o3o0gA16o0] 〇×ゲーム2.0巻 ウェブソケットGUIコンシューマー ver1.1.0
from apps1.tic_tac_toe_vol2o0.websocks.gui.consumer.ver1o1o0 import ConsumerCustom
#          ------------------                       --------        --------------
#          11                                       12              2
#    -------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス


websocket_urlpatterns = [

    # [OA16o3o0gA16o0] 〇×ゲーム v2
    url(r'^tic-tac-toe/v2/playing/(?P<kw_room_name>\w+)/$',
        # -----------------------------------------------
        # 1
        ConsumerCustom.as_asgi()),
    #   ------------------------
    #   2
    # 1. 例えば `ws://example.com/tic-tac-toe/v2/playing/Elephant/` のようなURLのパスの部分
    #                            --------------------------------
    #    kw_room_name は変数として渡される
    # 2. クラス名とメソッド。 URL を ASGI形式にする
]

# EOF [OA16o3o0gA16o0]
