# BOF OA24o1o0g3o0

from asgiref.sync import sync_to_async

# 部屋モデル
from apps1.practice_v1.models.room.v1o0 import Room
#          -----------             ----        ----
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 〇×ゲーム v2 コンシューマー v1.0
from apps1.tic_tac_toe_v2.websocks.gui.consumer.v1o0 import TicTacToeV2ConsumerBase
#                       ^two
#          --------------                       ----        -----------------------
#          11                                   12          2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれている __init__.py ファイルにさらに含まれるクラス

# 〇×ゲーム v2 Webソケット メッセージ駆動 v1.0
from apps1.tic_tac_toe_v2.websocks.gui.message_driven.v1o0 import TicTacToeV2MessageDriven
#          --------------                             ----        ------------------------
#          11                                         12          2
#    -----------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス

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


class TicTacToeV3o1o0ConsumerCustom(TicTacToeV2ConsumerBase):
    """OA24o1o0g3o0 Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()
        self._messageDriven = TicTacToeV2MessageDriven()
        #                               ^three

        self._messageDriven.addHandler('C2S_End', self.on_end)
        self._messageDriven.addHandler('C2S_Moved', self.on_move)
        self._messageDriven.addHandler('C2S_Start', self.on_start)

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """

        return await self._messageDriven.execute(self.scope, doc_received)

    async def on_end(self, scope, doc_received):
        """対局終了時"""
        # print("[TicTacToeV3o1o0ConsumerCustom on_end] ignored")
        # TODO 現状、クライアント側から勝者を送ってきているが、勝敗判定のロジックはサーバー側に置きたい
        winner = doc_received.get("c2s_winner", None)

        args = {
            "player1": winner
        }

        return CommandsGen.create_end(args)

    async def on_move(self, scope, doc_received):
        """駒を置いたとき"""

        # ログインしていなければ AnonymousUser
        user = scope["user"]
        # print(
        #     f"[TicTacToeV3o1o0ConsumerCustom on_move 1] user=[{user}] doc_received={doc_received}")
        if user.is_anonymous:
            # ログインしていないユーザーの操作は記録しません
            # print(
            #    f"[TicTacToeV3o1o0ConsumerCustom on_move 1.5] ログインしていないので操作の記録を省きます")
            pass

        else:

            # print(f"[TicTacToeV3o1o0ConsumerCustom on_move 1.75] ログインしています")

            # 部屋名
            #
            # * URLのパスに含まれている
            room_name = scope["url_route"]["kwargs"]["kw_room_name"]
            # print(f"[TicTacToeV3o1o0ConsumerCustom on_move 2] scope={scope}")

            # `c2s_` は クライアントからサーバーへ送られてきた変数の目印
            event = doc_received.get("c2s_event", None)
            # 駒を置いたマス番号
            sq = doc_received.get("c2s_sq", None)
            # 駒を置いた方の X か O
            piece_moved = doc_received.get("c2s_pieceMoved", None)
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 3] クライアントからのメッセージを受信しました room_name=[{room_name}] event=[{event}] piece_moved=[{piece_moved}] sq=[{sq}]")
            # クライアントからのメッセージを受信しました room_name=[Elephant] event=[C2S_Moved] piece_moved=[X] sq=[2]

            # 部屋取得
            room = await get_room_by_name(room_name)

            # （デバッグ）現状を出力
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 4] room=[{room}]")
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 5] now room.name=[{room.name}] room.board=[{room.board}] room.record=[{room.record}]")

            # 駒を置きます
            #
            # * 盤が9マスになるように右を '.' で埋めます
            room.board = room.board.ljust(9, '.')
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 6] now2 room.board=[{room.board}]")

            room.board = f"{room.board[:sq]}{piece_moved}{room.board[sq+1:]}"
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 7] now3 room.board=[{room.board}]")

            # 棋譜を書きます
            #
            # * 相手が AnonymousUser なら、相手の指し手が記録されていないものになります
            # * 9文字を超えるようなら、切り捨てます

            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 8] now4 room.record=[{room.record}]")
            room.record = f"{room.record}{sq}"[:9]
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 9] now5 room.record=[{room.record}]")

            # 部屋を上書きします
            await save_room(room)

            print(f"[TicTacToeV3o1o0ConsumerCustom on_move 10] saved")

        # `s2c_` は サーバーからクライアントへ送る変数の目印
        c2s_sq = doc_received.get("c2s_sq", None)
        piece_moved = doc_received.get("c2s_pieceMoved", None)
        # print(
        #     f"[TicTacToeV3o1o0ConsumerCustom on_move 11] C2S_Moved c2s_sq=[{c2s_sq}] piece_moved=[{piece_moved}]")

        args = {
            "sq1": c2s_sq,
            "piece1": piece_moved,
        }

        return CommandsGen.create_moved(args)

    async def on_start(self, scope, doc_received):
        """対局開始時"""

        # print(
        #     f"[TicTacToeV3o1o0ConsumerCustom on_start] ignored. doc_received={doc_received}")
        args = {}

        return CommandsGen.create_start(args)


@sync_to_async
def get_room_by_name(name):
    # FIXME 部屋名はIDではないので、先頭の要素を取得
    return Room.objects.filter(name=name)[0]


@sync_to_async
def save_room(room):
    room.save()

# EOF OA24o1o0g3o0
