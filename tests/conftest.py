import pytest

dataForTimesTwo = [
    {"input": 2, "expect": 4},
    {"input": 3, "expect": 6},
    {"input": "a", "expect": "aa"},
]
@pytest.fixture(params=dataForTimesTwo)
def testData(request):
    return request.param
