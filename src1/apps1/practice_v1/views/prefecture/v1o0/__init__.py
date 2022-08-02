class PrefectureV(object):
    """OA11o1o0g4o0 都道府県のビュー"""

    # OA11o1o0g4o0 一覧
    from .v_list import render_list

    # OA11o2o0g4o0 詳細
    from .v_read import render_read

    from .v_delete import render_delete
    from .v_upsert import render_upsert
