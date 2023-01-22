# BOF [OA24o1o0g3o_1o0]

from asgiref.sync import sync_to_async

# 部屋モデル
from apps1.practice_vol1o0.models.room.ver1o0 import Room
#          ---------------             ------        ----
#          11                          12            2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# [OA16o3o_2o0g1o_2o0] Movedメッセージ
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.moved.ver1o0 import MovedS2cMessage


class MoveC2sHandler:
    """駒を置いたとき"""

    async def on_message_received(self, scope, doc_received):
        """メッセージ受信"""

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

            # イベント名 (Client to server)
            event = doc_received.get("event", None)
            # 駒を置いたマス番号
            sq = doc_received.get("sq", None)
            # 駒を置いた方の X か O
            piece_moved = doc_received.get("piece", None)
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

        # Client to server
        sq = doc_received.get("sq", None)
        piece_moved = doc_received.get("piece", None)
        # print(
        #     f"[TicTacToeV3o1o0ConsumerCustom on_move 11] C2S_Moved sq=[{sq}] piece_moved=[{piece_moved}]")

        args = {
            "sq1": sq,
            "piece1": piece_moved,
        }

        return MovedS2cMessage(args).asDict()


@sync_to_async
def get_room_by_name(name):
    # FIXME 部屋名はIDではないので、先頭の要素を取得
    return Room.objects.filter(name=name)[0]


@sync_to_async
def save_room(room):
    room.save()

# EOF [OA24o1o0g3o_1o0]
