# BOF [OAAA1001o2o1o0g5o_1o0]

class Participant:
    """[OAAA1001o2o1o0g5o_1o0] 参加者"""

    def __init__(self, id, event_id, volume_id, name):
        self._id = id
        self._event_id = event_id
        self._volume_id = volume_id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def event_id(self):
        return self._event_id

    @property
    def volume_id(self):
        return self._volume_id

    @property
    def name(self):
        return self._name

# EOF [OAAA1001o2o1o0g5o_1o0]
