from unittest.mock import patch
from PyProjDemo.Foo import foo

def test_foo_foofunc():
    assert foo.foofunc() == 0

@patch("PyProjDemo.Bar.bar.barfunc", return_value=5)
def test_foo_callBar(barfunc):
    result = foo.callBar()
    assert result == 5
