// BOF OA16o3o_1o0g_1o__13o0

/**
 * イベント
 *
 * * 勝ったことに納得したとき
 */
class EvtWon {
    /**
     * メッセージ新規作成
     * @param {*} winner - 勝者。 "X" か "O"
     * @returns メッセージ
     */
    createMessage(winner) {
        return new MessageC2S({
            // `c2s_` は クライアントからサーバーへ送る変数の目印
            c2s_event: "C2S_End",
            c2s_winner: winner,
        });
    }
}

// EOF OA16o3o_1o0g_1o__13o0
