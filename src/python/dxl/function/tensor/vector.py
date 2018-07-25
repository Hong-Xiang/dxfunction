from dxl.data.tensor import Vector


def project(v: Vector, n: Vector) -> Vector:
    """
    Project Vector v onto plane with normal vector n.
    """
    return v - v @ n * n / n @ n


