from src.module import foo

def test_foo():
    assert foo(1, 2) == 3
    assert foo(-1, 1) == 0
    assert foo(0, 0) == 0
    assert foo(100, 200) == 300
    assert foo(-100, -200) == -300