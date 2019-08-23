import pytest
from PyProjDemo.Bar import bar

def test_bar_single():
    assert bar.timesTwo(2) == 4


dataForTimesTwo = [
    {"input": 2, "expect": 4},
    {"input": 3, "expect": 6},
    {"input": "a", "expect": "aa"},
]
@pytest.fixture(params=dataForTimesTwo)
def testData(request):
    return request.param


def test_bar_fixture(testData):
    result = bar.timesTwo(testData["input"])
    assert result == testData["expect"]