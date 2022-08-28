// BOF OA16o3o_1o0g_1o__10o0

/**
 * クライアントからサーバーへ送るメッセージ
 *
 * * 自分のターンに駒を置いたら送ります
 */
class MsgDoMove {
    /**
     * 新規作成
     * @param {int} sq - 升番号
     * @param {string} pieceMoved - 駒を置いたプレイヤー。 X か O
     * @returns メッセージ
     */
    create(sq, pieceMoved) {
        // `c2s_` は クライアントからサーバーへ送る変数の目印
        console.log(`[CmdDoMove create] sq=${sq} pieceMoved=${pieceMoved}`);
        return {
            c2s_event: "C2S_Moved",
            c2s_sq: sq,
            c2s_pieceMoved: pieceMoved,
        };
    }
}

// EOF OA16o3o_1o0g_1o__10o0
