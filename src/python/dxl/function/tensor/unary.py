from functools import singledispatch
from dxl.data.tensor import Tensor
import numpy as np

__all__ = ['abs_', 'unit', 'as_scalar']

@singledispatch
def abs_(t):
    raise TypeError()


@abs_.register(Tensor)
def _(t):
    return t.fmap(abs_)


@abs_.register(np.ndarray)
def _(t):
    return np.abs(t)


@singledispatch
def unit(t):
    raise TypeError


@unit.register(Tensor)
def _(t):
    return t.fmap(unit)


@unit.register(np.ndarray)
def _(t):
    return t / np.linalg.norm(t)

@singledispatch
def as_scalar(t):
    raise TypeError()

@as_scalar.register(Tensor)
def _(t):
    return as_scalar(t.join())

@as_scalar.register(np.ndarray)
def _(t):
    return np.asscalar(t)