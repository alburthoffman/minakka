"""
A simple primitive actor type.

Author: Tang, Hoffman
"""

import gevent
from gevent.queue import Queue

from . import message


class Actor(gevent.Greenlet):
    def __init__(self, _system=None):
        gevent.Greenlet.__init__(self)
        self.__inbox = Queue()
        self.__system = _system

    def send(self, msg):
        self.__inbox.put(msg)

    def stop(self):
        self.send(message.CtrlExit())

    def receive(self, msg):
        """
        receive a immutable message!!!!

        @param message:
        @return:
        """
        pass

    def onShutdown(self):
        pass

    def _run(self):
        while True:
            msg = self.__inbox.get()
            # handle framework control message first ....
            if isinstance(msg, message.CtrlExit):
                self.onShutdown()
                break

            self.receive(msg)
        self.kill()