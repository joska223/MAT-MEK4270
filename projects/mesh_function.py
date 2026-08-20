from collections.abc import Callable

import numpy as np
from matplotlib import pyplot


def mesh_function(f: Callable[[float], float], t: np.ndarray) -> np.ndarray:
    func_array = np.zeros(len(t))
    for i in range(len(t)):
        func_array[i] = f(t[i])

    return func_array

def func(t: float) -> float:
    if 0<=t and t<= 3:
        return np.exp(-t)
    elif 3<t and t<=4:
        return np.exp(-3*t)
    else:
        raise ValueError



def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)

if __name__ == "__main__":
    test_mesh_function()
