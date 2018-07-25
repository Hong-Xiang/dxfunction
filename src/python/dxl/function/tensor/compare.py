from functools import singledispatch
from dxl.data.tensor import Tensor
import numpy as np


def all_close(x, y):
    return _all_close(Tensor(x).join(), Tensor(y).join())


@singledispatch
def _all_close(x, y):
    raise TypeError


@_all_close.register(np.ndarray)
def _(x, y):
    return np.allclose(x, y)
