// BOF OA16o3o_1o0g_1o__12o0

/**
 * コマンド
 *
 * * 対局開始に納得したとき送ります
 */
class CmdStart {
    /**
     * @returns メッセージ
     */
    create() {
        // `c2s_` は クライアントからサーバーへ送る変数の目印
        return {
            c2s_event: "C2S_Start",
        };
    }
}

// EOF OA16o3o_1o0g_1o__12o0
