import pytest
from PyProjDemo.Bar import bar

def test_bar_single():
    assert bar.timesTwo(2) == 4


def test_bar_fixture(testData):
    result = bar.timesTwo(testData["input"])
    assert result == testData["expect"]