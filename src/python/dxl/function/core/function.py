from functools import wraps, partial
from contextlib import contextmanager
from .control import Applicative, fmap
from abc import ABCMeta, abstractmethod


__all__ = ['Function', 'function', 'identity',
           'FMapOf', 'CallAsArgs', 'args', 'kwargs']


class CallContext:
    def __init__(self, f, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.f = f
        self.prev = None

    def __enter__(self):
        self.prev = self.f._call_ctx()


class Function(Applicative):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

    def __rshift__(self, f):
        return self.fmap(f)

    def fmap(self, f):
        return Function(lambda x: f(self.__call__(x)))

    def apply(self, x):
        return Function(partial(self.__call__, x))

    @classmethod
    def from_(self, f):
        @wraps(f)
        class Function_(Function):
            def __call__(self, *args, **kwargs):
                return f(*args, **kwargs)
        return Function_


def function(f):
    return wraps(f)(Function(f))


identity = Function(lambda _: _)


class FMapOf(Function):
    def __call__(self, x):
        return fmap(self.f, x)


args = Function(lambda *args, **kwargs: args)


kwargs = Function(lambda *args, **kwargs: kwargs)


class GetAttr(Function):
    def __init__(self, name):
        self.name = name

    def __call__(self, x):
        return getattr(x, self.name)


class CallAsArgs(Function):
    def __call__(self, x):
        print(x)
        return self.f(*x)
