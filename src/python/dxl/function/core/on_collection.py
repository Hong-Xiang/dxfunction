import collections.abc
from functools import singledispatch
from .function import Function

@singledispatch
def _take(xs, n):
    raise TypeError(f"Can't Take on {type(x)}")

@_take.register(collections.abc.Sequence)
def _(xs, n):
    return xs[:n]

class Take(Function):
    def __init__(self, n):
        self.n  = n
    
    def __call__(self, x):
        return _take(xs, self.n)
    
head = Take(1)