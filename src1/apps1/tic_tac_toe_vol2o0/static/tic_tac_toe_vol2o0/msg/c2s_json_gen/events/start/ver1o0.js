// BOF OA16o3o_1o0g_1o__12o0

/**
 * イベント
 *
 * * 対局開始に納得したとき
 */
class EvtStart {
    /**
     * メッセージ新規作成
     * @returns メッセージ
     */
    createMessage() {
        return new MessageC2S({
            // `c2s_` は クライアントからサーバーへ送る変数の目印
            c2s_type: "C2S_Start",
        });
    }
}

// EOF OA16o3o_1o0g_1o__12o0
