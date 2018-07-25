from typing import Callable
from functools import singledispatch
from dxl.data import Functor

FunctorB = Union[List, Tuple, Dict, Functor[a]]


def fmap(f: Callable, fct: FunctorB) -> FunctorB:
    return _fmap(fct, f)


@singledispatch
def _fmap(fct, f):
    raise TypeError(
        f"Can't {type(f)} is not Functor or built-in Functor likes.")


@_fmap.register(Functor)
def _(fct, f):
    return fct.fmap(f)


@_fmap.register(list)
def _(xs, f):
    return [f(x) for x in xs]


@_fmap.register(tuple)
def _(xs, f):
    return tuple([f(x) for x in xs])


@_fmap.register(dict)
def _(dct, f):
    return {k: f(v) for k, v in dct.items()}
