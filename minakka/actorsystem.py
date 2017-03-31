"""
A simple primitive actor system.

Author: Tang, Hoffman
"""
import gevent
import inspect

class ActorSystem:
    """ the reason we need system here is to provide a easy way to do life cycle management for actors
    """
    def __init__(self, name=None):
        self.__name = name
        self.__greenlets = []

    def actorOf(self, cls, *args, **kargs):
        if hasattr(cls, '__init__') and '_actorsystem' in (inspect.getargspec(cls.__init__))[0]:
            clone = kargs.copy()
            clone["_actorsystem"] = self
        else:
            clone = kargs
        actor = cls(*args, **clone)
        self.__greenlets.append(actor)
        actor.start()
        return actor

    def shutdown(self):
        for idx in xrange(len(self.__greenlets)):
            actor = self.__greenlets[-(idx + 1)]
            actor.stop()
        try:
            gevent.joinall(self.__greenlets)
        except Exception as e:
            pass