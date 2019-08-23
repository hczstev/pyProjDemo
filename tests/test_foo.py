import pytest
from unittest.mock import patch
from PyProjDemo.Foo import foo

@patch("PyProjDemo.Bar.bar.timesTwo", return_value=5)
def test_foo_getDouble(mockBar):
    result = foo.getDouble(2)
    assert result == 5
    assert mockBar.called
    assert mockBar.call_args == ((2,),)

@patch("PyProjDemo.Bar.bar.timesTwo", side_effect=OSError("mock error"))
def test_foo_mockException(mockBar):
    with pytest.raises(OSError) as e:
        foo.getDouble(2)
    
    assert "mock error" in str(e)
