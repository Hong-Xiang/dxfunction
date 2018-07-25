from functools import singledispatch
import numpy as np
import tensorflow as tf
from dxl.data.tensor import Tensor

DEFAULT_CONSTRUCTOR = np.array

__all__ = ['to_tensor_like']


@singledispatch
def to_tensor_like(t):
    return DEFAULT_CONSTRUCTOR(t)


@to_tensor_like.register(np.ndarray)
@to_tensor_like.register(tf.Tensor)
def _(t):
    return t


@to_tensor_like.register(Tensor)
def _(t):
    return t.join()
