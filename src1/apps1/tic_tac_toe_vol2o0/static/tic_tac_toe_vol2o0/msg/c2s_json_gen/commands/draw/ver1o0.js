// BOF OA16o3o_1o0g_1o__11o0

/**
 * コマンド
 *
 * * 引き分けで対局終了したと納得したら送ります
 */
class CmdDraw {
    /**
     * @returns メッセージ
     */
    create() {
        // `c2s_` は クライアントからサーバーへ送る変数の目印
        return {
            c2s_event: "C2S_End",
            c2s_winner: PC_EMPTY_LABEL,
        };
    }
}

// EOF OA16o3o_1o0g_1o__11o0
