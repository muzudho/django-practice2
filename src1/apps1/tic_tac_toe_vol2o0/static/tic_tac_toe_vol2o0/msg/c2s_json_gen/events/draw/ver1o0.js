// BOF OA16o3o_1o0g_1o__11o0

/**
 * イベント
 *
 * * 引き分けで対局終了したと納得したとき
 */
class EvtDraw {
    /**
     * メッセージ新規作成
     * @returns メッセージ
     */
    createMessage() {
        return new EndC2sMessage(PC_EMPTY_LABEL);
    }
}

// EOF OA16o3o_1o0g_1o__11o0
