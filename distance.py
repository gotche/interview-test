from pathlib import Path
import re
from typing import Generator


def find_shortest_distance(a: str, b: str, datafile: Path) -> int:
    '''
        Find the shortest amount of words between word a and word b
        if one or both of the words cannot be found, -1 is returned
    '''

    # We don't care about case, so every word should be treated as lowercase
    a, b = a.lower(), b.lower()

    # Prepare the data from datafile
    data = get_words_from_file(datafile)

    counter = -1

    for word in data:
        word = clean(word)

        if counter < 0:
            if word == a:
                counter = 0
                continue
        else:
            if word == b:
                break
            else:
                counter += 1

    else:
        counter = -1

    return counter


def clean(word: str) -> str:
    '''
        A word is compound of alpha numeric characters.
        Other characters are removed and lowercase is
        enforced
    '''
    return ''.join(letter.lower() for letter in word if letter.isalnum())


def get_words_from_file(datafile: Path) -> Generator[str, None, None]:
    with open(datafile) as f:
        for line in f:
            yield from split_iter(line)


def split_iter(string: str) -> Generator[str, None, None]:
    '''
        https://stackoverflow.com/questions/3862010/
        is-there-a-generator-version-of-string-split-in-python
    '''
    return (x.group(0) for x in re.finditer(r'\S+', string))
