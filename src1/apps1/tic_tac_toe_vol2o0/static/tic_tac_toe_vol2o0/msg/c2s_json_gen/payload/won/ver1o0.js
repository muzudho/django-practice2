// BOF OA16o3o_1o0g_1o__13o0

/**
 * クライアントからサーバーへ送るメッセージ
 *
 * * 勝ったことに納得したら送ります
 */
class MsgWon {
    /**
     * 新規作成
     * @param {*} winner - 勝者。 "X" か "O"
     * @returns メッセージ
     */
    create(winner) {
        // `c2s_` は クライアントからサーバーへ送る変数の目印
        return {
            c2s_event: "C2S_End",
            c2s_winner: winner,
        };
    }
}

// EOF OA16o3o_1o0g_1o__13o0
