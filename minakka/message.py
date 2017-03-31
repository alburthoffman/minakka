"""
A simple message type.

Author: Tang, Hoffman
"""

class Message:
    def __init__(self, msg=None):
        self.__msg = msg

    def __repr__(self):
        return "%s : %s" % (self.__class__, self.__msg)

class CtrlExit(Message):
    def __init__(self):
        Message.__init__(self, msg="exit")