# BOF [OAAA1001o2o1o0g5o0]

import json

# [OAAA1001o2o1o0g5o_2o0] 連続名1.0巻 連続性1.0版
from src1.apps1.consecutive_name_vol1o0.views.consecutive.ver1o0 import Consecutive

# [OAAA1001o2o1o0g5o_3o0] 連続名1.0巻 推移1.0版
from src1.apps1.consecutive_name_vol1o0.views.transition.ver1o0 import Transition


class XPcpConYTra:

    @staticmethod
    def convert(consecutive_filepath):
        con_jso = XPcpConYTra.convert_filepath_to_js_object(
            consecutive_filepath)

        con_dict = XPcpConYTra.convert_js_object_to_consecutive_dict(con_jso)

        # 愚直に、全ての Consecutive オブジェクトの originator を算出
        for con_obj in con_dict.values():
            originator = XPcpConYTra.find_originator(con_obj)

            # 上書き（in place）
            con_obj.originator = originator

        # Transition の dict に変換する
        tra_dict = dict()
        for con_obj in con_dict.values():
            # tra_dict
            pass

        return XPcpConYTra(con_dict)

    @staticmethod
    def convert_filepath_to_js_object(filepath):
        with open(filepath, 'r', encoding="utf8") as f:
            print(f"Read... {filepath}")
            js_object = json.load(f)
        return js_object

    @staticmethod
    def convert_js_object_to_consecutive_dict(js_object):
        con_dict = dict()
        for con_jso in js_object:
            con_obj = Consecutive(
                id=con_jso.id,
                prev=con_jso.prev)
            con_dict[con_obj.id] = con_obj
        return con_dict

    def __init__(self, consecutive_dict):
        self._consecutive_dict = consecutive_dict

    @property
    def consecutive_dict(self):
        return self._consecutive_dict

    @staticmethod
    def find_originator(con_obj, con_dict):
        if not con_obj.prev in con_dict.keys():
            # 自分が始祖だ
            return con_obj

        prev_obj = con_dict[con_obj.prev]

        if not prev_obj.originator is None:
            return prev_obj.originator

        # 再起
        return XPcpConYTra.find_originator(prev_obj)

# EOF [OAAA1001o2o1o0g5o0]
