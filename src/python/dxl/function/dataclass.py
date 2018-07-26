from functools import singledispatch
from dxl.data import DataClass



@singledispatch
def replace(o, **kwargs):
    raise TypeError



@replace.register(DataClass)
def _(o, **kwargs):
    return o.replace(**kwargs)
