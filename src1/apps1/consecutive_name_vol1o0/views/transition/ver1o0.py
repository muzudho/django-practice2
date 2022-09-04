# BOF [OAAA1001o2o1o0g5o_3o0]

class Transition:
    """[OAAA1001o2o1o0g5o_3o0] 推移"""

    def __init__(self, id, last_pcp_id, pcp_id):
        self._id = id
        self._last_pcp_id = last_pcp_id
        self._pcp_id = pcp_id

    @property
    def id(self):
        return self._id

    @property
    def last_pcp_id(self):
        return self._last_pcp_id

    @property
    def pcp_id(self):
        return self._pcp_id

# EOF [OAAA1001o2o1o0g5o_3o0]
