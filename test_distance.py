from pathlib import Path

import pytest

from distance import find_shortest_distance


"""
    file1 contains the example sentences of the exercise:

    'We do value and reward motivation in our development team. '
    'Development is a key skill for a DevOp'

    file2 contains the list of words that can be found in many
    linux distributions in /usr/share/dict/words
"""

datafile1 = Path('datafiles/file1')
datafile2 = Path('datafiles/file2')

test_cases = [
    ('motivation', 'development', datafile1, 2),
    ('we', 'do', datafile1, 0),
    ('we', 'we', datafile1, -1),
    ('we', 'devop', datafile1, 16),
    ('a', 'aol', datafile2, 3),
    ('a', 'études', datafile2, 100408),
]


@pytest.mark.parametrize('a, b, datafile, distance', test_cases)
def test_shortest_distance(a, b, datafile, distance):
    assert find_shortest_distance(a, b, datafile) == distance
