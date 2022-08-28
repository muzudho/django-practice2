// BOF OA16o3o_1o0g_1o0

/**
 * 送信JSONジェネレーター
 *
 * * クライアントからサーバーへ送る
 */
class C2sJsonGen {
    /**
     * 勝った方のプレイヤーが、サーバーに対局終了メッセージを送ります
     * @param {*} winner - 勝者。 "X" か "O"
     * @returns メッセージ
     */
    createWon(winner) {
        // `c2s_` は クライアントからサーバーへ送る変数の目印
        return {
            c2s_event: "C2S_End",
            c2s_winner: winner,
        };
    }
}

// EOF OA16o3o_1o0g_1o0
