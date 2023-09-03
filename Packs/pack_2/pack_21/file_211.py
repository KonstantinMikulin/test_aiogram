print('This is file ', __name__)

from ..file_21 import another_some_func

b: int = 4242

some_dict: dict[int, str] = {1: 'A',
                             2: 'B',
                             3: 'C'}

r = another_some_func(b)
