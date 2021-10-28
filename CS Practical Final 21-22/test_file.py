import pytest
import DataStructuresPrograms


def test_longest_word():
    assert DataStructuresPrograms.longestWord(
        ['Apurba', 'Anindita', 'Himangshu', 'Arunodaya']
    ) == 'Himangshu' or 'Arunodaya'


def test_fibo_in_tuple():
    assert DataStructuresPrograms.FiboinTuple() == (0, 1, 1, 2, 3, 5, 8, 13, 21)


def test_Common_Elements():
    assert DataStructuresPrograms.commonElements([1, 3, 5, 7, 4, 9, 12, 15, 75, 2], [1, 44, 5, 15, 7, 9, 120]) == [1, 5, 7, 9, 15]
    assert DataStructuresPrograms.commonElements(
        [1, 44, 5, 15, 7, 9, 120], [1, 3, 5, 7, 4, 9, 12, 15, 75, 2]) == [1, 5, 15, 7, 9]


def test_dictDatas():
    assert DataStructuresPrograms.dictDatas(
        'January', 31, 
        'February', 28,
        'March', 31,
        'April', 30,
        'May', 31,
        'June', 30
    ) == {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30
    }
    
