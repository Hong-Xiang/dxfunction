from collections import UserList
from .control import Applicative
from functools import partial

__all__ = ['List']


class List(UserList, Applicative):
    def _inner(self):
        return self.data

    def fmap(self, f):
        return List([f(x) for x in self.data])

    def apply(self, x: 'List'):
        result = []
        for f in self.data:
            result += x.fmap(lambda x: partial(f, x))
        return List(result)
