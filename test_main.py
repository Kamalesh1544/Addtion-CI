import pytest
from main import add

@pytest.mark.parametrize("a,b,expected",[
    (1,1,2),
    (1,2,3),
    (2,2,4)
])
def test_add(a,b,expected):
    assert a+b == expected























