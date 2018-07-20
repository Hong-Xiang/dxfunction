from dxl.function.core.builtin import List, ListFunc

def test_applicative():
    def add_two(x, y):
        return x + y

    def mul_two(x, y):
        return x * y
    result = ListFunc([add_two, mul_two]).apply(
        List([1, 2, 3])).apply(List([3, 4, 5])).run()
    assert result == [4, 5, 6, 5, 6, 7, 6, 7, 8, 3, 4, 5, 6, 8, 10, 9, 12, 15]


def test_construct():
    result = List([1, 2, 3])
    assert isinstance(result, List)
    assert result == [1, 2, 3]
