from gevent.lock import RLock

class Map(object):
    def __init__(self):
        self.__cache = dict()
        self.__lock = RLock()

    def __contains__(self, k):
        v = False
        with self.__lock:
            if k in self.__cache:
                v = True
        return v

    def __setitem__(self, k, v):
        with self.__lock:
            self.__cache[k] = v

    def __getitem__(self, k):
        v = None
        with self.__lock:
            if k in self.__cache:
                v = self.__cache[k]
        return v

    def __delitem__(self, k):
        with self.__lock:
            if k in self.__cache:
                del self.__cache[k]

    def update(self, k, v):
        if not callable(v):
            self.__setitem__(k, v)
        else:
            with self.__lock:
                if k in self.__cache:
                    val = v(self.__cache[k])
                    self.__cache[k] = val

    def items(self):
        eles = []
        with self.__lock:
            for (k, v) in self.__cache.items():
                eles.append((k, v))
        return eles