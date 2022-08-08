import itertools
from unittest.mock import patch

"""
    Return successive r-length permutations of elements in the iterable.

    permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)
"""

name = 'some very long name'


#
# for i in itertools.permutations(name, 4):
#     print(i)


def real(name):
    if len(name) < 10:
        raise ValueError('String too short to calculate statistics.')
    y = 0
    for i in itertools.permutations(range(len(name)), 10):
        y += sum(i)
        print(y, i)
        if y == 18527432:
            break


real(name)
#
# with patch('itertools.permutations') as perm_mock:
#     perm_mock.return_value = [(10, 12, 14), (12, 14, 10)]
#     real(name)
#     perm_mock.assert_called_with(range(len(name)), 10)
