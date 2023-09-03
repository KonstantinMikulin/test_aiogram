print('This is file ', __name__)

from .file_12 import num


def some_func(n: int) -> float:
    return (n + n) / n ** n


result = some_func(num)
