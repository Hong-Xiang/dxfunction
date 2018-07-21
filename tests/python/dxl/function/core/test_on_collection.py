from dxl.function.core.on_collection import *
import collections.abc

def test_take_list():
    assert Take(2)([1,2,3]) == [1, 2]

def test_take_iterator():
    result = Take(2)(range(3))
    assert isinstance(result, collections.abc.Iterable)
    assert list(result) == [0, 1]

def test_head_list():
    assert head([1,2,3]) == 1