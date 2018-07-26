from dxl.data import Function
from functools import wraps

__all__ = ['identity', 'func']

identity = Function(lambda a: a)


def func(f):
    return wraps(Function(f))
