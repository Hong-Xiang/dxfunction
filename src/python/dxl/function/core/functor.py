__all__ = ['Functor', 'fmap']

from abc import ABCMeta, abstractmethod


class Functor(metaclass=ABCMeta):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def fmap(self, f):
        """
        Returns TypeOfFunctor(f(self.data)),
        mimics fmap :: (a -> b) -> a -> b by
        fmap( fa ) -> type(fmap)(f(a))
        """
        ...


def fmap(f, fa):
    if isinstance(fa, Functor):
        return fa.fmap(f)
    if isinstance(fa, (list, tuple)):
        return type(fa)(map(f, fa))
    if isinstance(fa, dict):
        return {k: f(v) for k, v in fa.items()}
