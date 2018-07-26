from dxl.function.tensor import project, all_close
from dxl.data.tensor import Vector


def test_project_withvalue():
    v1 = Vector([1.0, 0.0])
    v2 = Vector([1.0, 1.0])
    assert all_close(project(v1, v2), Vector([0.0, 1.0]))


def test_project_withoutvalue():
    v1 = Vector([1.0, 0.0])
    v2 = Vector([0.0, 1.0])
    assert all_close(project(v1, v2), Vector([0.0, 1.0]))


def test_project_keep_scale():
    v1 = Vector([3.0, 0.0])
    v2 = Vector([1.0, 1.0])
    assert all_close(project(v1, v2), Vector([0.0, 1.0]))
