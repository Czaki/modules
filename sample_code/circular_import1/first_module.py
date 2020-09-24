from .second_module import simple_fun2


def simple_fun1(n: int):
    return 2 * simple_fun2(n - 1)
