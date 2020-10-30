from src.first import calc,sums

def test_calc():
    assert calc() == "Hello World!"

def test_sum():
    assert sums(3,4) == 7
    assert sums("a","b") == "ab"

def test_passes_but_bad_style():
    try:
        assert sums("a", 5) or sums(5, "b")
        assert False
    except TypeError:
        assert True

#if __name__ == '__main__':
#    test_calc()
