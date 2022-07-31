class PrefectureV(object):
    """都道府県のビュー"""

    from .v_list import render_list
    from .v_read import render_read
    from .v_delete import render_delete
    from .v_upsert import render_upsert
