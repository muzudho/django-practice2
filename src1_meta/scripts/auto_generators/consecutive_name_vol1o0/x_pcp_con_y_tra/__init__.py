# BOF [OAAA1001o2o1o0g5o0]

import json

# [OAAA1001o2o1o0g5o_1o0] 連続名1.0巻 参加者1.0版
from src1.apps1.consecutive_name_vol1o0.views.participant.ver1o0 import Participant

# [OAAA1001o2o1o0g5o_2o0] 連続名1.0巻 連続性1.0版
from src1.apps1.consecutive_name_vol1o0.views.consecutive.ver1o0 import Consecutive

# [OAAA1001o2o1o0g5o_3o0] 連続名1.0巻 推移1.0版
from src1.apps1.consecutive_name_vol1o0.views.transition.ver1o0 import Transition


class XPcpConYTra:

    @staticmethod
    def convert_filepath_to_js_object(filepath):
        with open(filepath, 'r', encoding="utf8") as f:
            print(f"Read... {filepath}")
            js_object = json.load(f)
        return js_object

    @staticmethod
    def convert_js_object_to_participant(js_object):
        return Participant(
            id=js_object.id,
            event_id=js_object.event_id,
            volume_id=js_object.volume_id,
            name=js_object.name)

    @staticmethod
    def convert_js_object_to_participant(js_object):
        return Consecutive(
            id=js_object.id,
            prev=js_object.prev)

    def __init__(self, participant_filepath, consecutive_filepath):
        self._participant_id_dict = dict()
        self._consecutive_id_dict = dict()

        self.load_participant_file(participant_filepath)
        self.load_consecutive_file(consecutive_filepath)

        # 愚直に、全ての Consecutive オブジェクトの originator を算出
        for con_obj in self._consecutive_id_dict.values():
            originator = self.find_originator(con_obj)

            # 上書き
            con_obj.originator = originator

    def load_participant_file(self, filepath):
        pcp_jso = XPcpConYTra.convert_filepath_to_js_object(filepath)
        pcp_obj = XPcpConYTra.convert_js_object_to_participant(pcp_jso)
        self._participant_id_dict[pcp_obj.id] = pcp_obj

    def load_consecutive_file(self, filepath):
        con_jso = XPcpConYTra.convert_filepath_to_js_object(filepath)
        con_obj = XPcpConYTra.convert_js_object_to_participant(con_jso)
        self._consecutive_id_dict[con_obj.id] = con_obj

    def find_originator(self, con_obj):
        if not con_obj.prev in self._consecutive_id_dict.keys():
            # 自分が始祖だ
            return con_obj

        prev_obj = self._consecutive_id_dict[con_obj.prev]

        if not prev_obj.originator is None:
            return prev_obj.originator

        # 再起
        return self.find_originator(prev_obj)

# EOF [OAAA1001o2o1o0g5o0]
