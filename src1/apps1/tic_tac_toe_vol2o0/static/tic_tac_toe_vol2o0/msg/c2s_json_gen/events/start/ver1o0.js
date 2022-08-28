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
        return new StartC2sMessage();
    }
}

// EOF OA16o3o_1o0g_1o__12o0
