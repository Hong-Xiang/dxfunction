from functools import singledispatch
from dxl.data.tensor import Tensor
import numpy as np


@singledispatch
def abs_(t):
    raise TypeError()


@abs_.register(Tensor)
def _(t):
    return abs(t.join())


@abs_.register(np.ndarray)
def _(t):
    return np.abs(t)
