from functools import singledispatch
from dxl.data import DataClass
import numpy as np


@singledispatch
def replace(o, **kwargs):
    raise TypeError


@replace.register(DataClass)
def _(o, **kwargs):
    return o.replace(**kwargs)


@replace.register(np.recarray)
def _(o, **kwargs):
    result = np.rec.array(o)
    for k, v in kwargs.items():
        result[k] = v
    return result
