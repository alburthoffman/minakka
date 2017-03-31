"""
Route is a type of actor which can do message routing to backend actors.

Author: Tang, Hoffman
"""

from minakka.core import actor


class Route(actor.Actor):
    def __init__(self, actors=[], _system=None):
        self.__actors = actors
        self.__index = 0
        super(Route, self).__init__()

    def receive(self, message):
        """
        this is a very simple route algorithm.
        basically it just distribute all messages to backend actors equanlly.
        @param message:
        @return:
        """
        if (len(self.__actors) <= 0):
            return

        target = self.__actors[self.__index]

        # move the index to next one
        self.__index = (self.__index + 1) % len(self.__actors)

        # distribute the message to target actor
        target.send(message)