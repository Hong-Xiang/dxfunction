from dxl.data.core import function, Function

__all__ = ['is_decay', 'AllIsInstance', 'MapIf',
           'Always', 'Filter', 'mono_decay', 'mono_increase']


@function
def is_decay(l):
    return all([x >= y for x, y in zip(l, l[1:])])


class AllIsInstance(Function):
    def __init__(self, target_type):
        self.target_type = target_type

    def __call__(self, it):
        return all(map(lambda o: isinstance(o, self.target_type), it))


class MapIf(Function):
    def __init__(self, cond, f):
        self.cond = cond
        self.f = f

    def __call__(self, x):
        if self.cond(x):
            return self.f(x)
        else:
            return x

from .base import func, identity

@func
def switch(predictor, f_true, f_false, x):
    return f_true(x) if predictor(x) else f_false(x)

@func
def map_if(f, predictor):
    return switch(predictor, f, identity)


class Filter(Function):
    def __init__(self, cond):
        self.cond = cond

    def __call__(self, it):
        def it_():
            for x in it:
                if self.cond(x):
                    yield x
        return it_()


@func
def is_none(x):
    return x is None

@func
def is_mono(predictor, xs):
    return 

@func
def mono_decay(x):
    for p, s in zip(x[:-1], x[1:]):
        if p < s:
            return False
    return True


@function
def mono_increase(x):
    for p, s in zip(x[:-1], x[1:]):
        if p > s:
            return False
    return True
