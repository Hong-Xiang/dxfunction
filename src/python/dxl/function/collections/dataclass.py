import numpy as np
from functools import singledispatch


def fields(dataclass_type):
    return dataclass_type.__slots__


def dtype_of(dataclass_type, type_hints=None):
    if type_hints is not None:
        dtype = [(f, t) for f, t in zip(fields(dataclass_type), type_hints)]
    else:
        raise NotImplementedError(
            "dtype inference without hint is not implemented yet.")
    return np.dtype(dtype, align=True)


def list_of_dataclass_to_numpy_structure_of_array(datas, types=None):
    return np.rec.array(list(datas.fmap(lambda c: c.astuple())),
                        dtype_of(type(datas[0]), types))

