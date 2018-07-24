from dxl.function.core.function import *


def test_args():
    assert args(1, 2, 3) == (1, 2, 3)


def test_call_as_args():
    def add(a, b):
        return a + b
    assert CallAsArgs(add)((1, 2)) == 3
