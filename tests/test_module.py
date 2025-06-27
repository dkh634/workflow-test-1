from src.module import foo

def test_foo():
    assert foo(1, 2 ,3) == 6
    assert foo(-1, 1 , 1) == 1