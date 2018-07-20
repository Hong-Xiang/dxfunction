from dxl.function.core.control import Functor, fmap


def add_one(x):
    return x + 1


def test_fmap_on_list():
    assert fmap(add_one, [1, 2]) == [2, 3]
    assert fmap(add_one, []) == []


def test_fmap_on_tuple():
    assert fmap(add_one, (1, 2)) == (2, 3)
    assert fmap(add_one, tuple()) == tuple()


def test_fmap_on_dict():
    assert fmap(add_one, {'a': 1, 'b': 2}) == {'a': 2, 'b': 3}
    assert fmap(add_one, {}) == {}
