from asgiref.sync import sync_to_async

from apps1.tic_tac_toe_v2.websocks.o1o0.gui.message_converter import TicTacToeV2MessageConverter
#    ----- -------------- ----------------- -----------------        ---------------------------
#    1     2              3                 4                        5
# 1,3. ディレクトリー名
# 1. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

# 部屋モデル
from apps1.practice_v1.models.o1o0.m_room import Room
#    ----- ----------- ----------- ------        ----
#    1     2           3           4             5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


class TicTacToeV3o1MessageConverter(TicTacToeV2MessageConverter):
    """サーバープロトコル"""

    def on_end(self, scope, doc_received):
        """対局終了時"""
        pass

    async def on_move(self, scope, doc_received):
        """駒を置いたとき"""

        # ログインしていなければ AnonymousUser
        user = scope["user"]
        print(
            f"[TicTacToeV3o1MessageConverter on_move] user=[{user}] doc_received={doc_received}")
        if user.is_anonymous:
            # ログインしていないユーザーの操作は記録しません
            return

        # 部屋名
        #
        # * URLのパスに含まれている
        room_name = scope["url_route"]["kwargs"]["kw_room_name"]
        # print(f"[TicTacToeV3o1MessageConverter on_move] scope={scope}")

        # `c2s_` は クライアントからサーバーへ送られてきた変数の目印
        event = doc_received.get("c2s_event", None)
        # 駒を置いたマス番号
        sq = doc_received.get("c2s_sq", None)
        # 駒を置いた方の X か O
        piece_moved = doc_received.get("c2s_pieceMoved", None)
        print(
            f"[TicTacToeV3o1MessageConverter on_move] クライアントからのメッセージを受信しました room_name=[{room_name}] event=[{event}] piece_moved=[{piece_moved}] sq=[{sq}]")
        # クライアントからのメッセージを受信しました room_name=[Elephant] event=[C2S_Moved] piece_moved=[X] sq=[2]

        # 部屋取得
        room = await get_room_by_name(room_name)

        # （デバッグ）現状を出力
        print(
            f"[TicTacToeV3o1MessageConverter on_move] room=[{room}]")
        print(
            f"[TicTacToeV3o1MessageConverter on_move] now room.name=[{room.name}] room.board=[{room.board}] room.record=[{room.record}]")

        # 駒を置きます
        #
        # * 盤が9マスになるように右を '.' で埋めます
        room.board = room.board.ljust(9, '.')
        print(
            f"[TicTacToeV3o1MessageConverter on_move] now2 room.board=[{room.board}]")

        room.board = f"{room.board[:sq]}{piece_moved}{room.board[sq+1:]}"
        print(
            f"[TicTacToeV3o1MessageConverter on_move] now3 room.board=[{room.board}]")

        # 棋譜を書きます
        #
        # * 相手が AnonymousUser なら、相手の指し手が記録されていないものになります
        # * 9文字を超えるようなら、切り捨てます

        print(
            f"[TicTacToeV3o1MessageConverter on_move] now4 room.record=[{room.record}]")
        room.record = f"{room.record}{sq}"[:9]
        print(
            f"[TicTacToeV3o1MessageConverter on_move] now5 room.record=[{room.record}]")

        # 部屋を上書きします
        await save_room(room)

        print(f"[TicTacToeV3o1MessageConverter on_move] saved")

    def on_start(self, scope, doc_received):
        """対局開始時"""

        print(
            f"[TicTacToeV3o1MessageConverter on_start] ignored. doc_received={doc_received}")
        pass


@sync_to_async
def get_room_by_name(name):
    # FIXME 部屋名はIDではないので、先頭の要素を取得
    return Room.objects.filter(name=name)[0]


@sync_to_async
def save_room(room):
    room.save()
