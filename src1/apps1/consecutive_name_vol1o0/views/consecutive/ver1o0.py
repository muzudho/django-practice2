# BOF [OAAA1001o2o1o0g5o_2o0]

class Consecutive:
    """[OAAA1001o2o1o0g5o_2o0] 連続性"""

    def __init__(self, id, prev):
        self._id = id
        self._prev = prev
        self._originator = None

    @property
    def id(self):
        return self._id

    @property
    def prev(self):
        return self._prev

    @property
    def originator(self):
        return self._originator

    @originator.setter
    def originator(self, value):
        self._originator = value

# EOF [OAAA1001o2o1o0g5o_2o0]
