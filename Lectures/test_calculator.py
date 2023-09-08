from calculator import square
import pytest

#def main():
#    test_square()

### Testing using try, assert, except and AssertionError

#def test_square():
#    try:
#        assert square(2) == 4
#    except AssertionError:
#        print("2 square is not 4")
#    try:
#        assert square(3) == 9
#    except AssertionError:
#        print("3 square is not 9")
#    try:
#        assert square(-2) == 4
#    except AssertionError:
#        print("-2 square is not 4")
#    try:
#        assert square(-3) == 9
#    except AssertionError:
#        print("-3 square is not 9")
#    try:
#        assert square(0) == 0
#    except AssertionError:
#        print("0 square is not 0")

### Try unit testing with pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

#if __name__ == "__main__":
#    main()