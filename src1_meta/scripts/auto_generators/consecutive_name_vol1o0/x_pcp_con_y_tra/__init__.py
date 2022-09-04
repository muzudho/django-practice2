# BOF [OAAA1001o2o1o0g5o0]

import json


class XPcpConYTra:

    @staticmethod
    def convert_f(participant_filepath, consecutive_filepath):

        with open(participant_filepath, 'r', encoding="utf8") as f:
            print(f"Read... {participant_filepath}")
            pcp_jso = json.load(f)

        with open(consecutive_filepath, 'r', encoding="utf8") as f:
            print(f"Read... {consecutive_filepath}")
            consecutive_jso = json.load(f)

        return XPcpConYTra.convert(
            participant_js_object=pcp_jso,
            consecutive_js_object=consecutive_jso)

    @staticmethod
    def convert(participant_js_object, consecutive_js_object):

        pass

# EOF [OAAA1001o2o1o0g5o0]
