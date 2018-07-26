from functools import singledispatch, partial
import numpy as np
from dxl.data.tensor import Tensor


@singledispatch
def transpose(t, perm=None):
    raise TypeError


@transpose.register(np.ndarray)
def _(t, perm=None):
    return np.transpose(t, perm)


@transpose.register(Tensor)
def _(t, perm=None):
    return t.fmap(lambda t: transpose(t, perm))
