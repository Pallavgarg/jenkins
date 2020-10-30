from src.first import calc,sums

def test_calc():
    assert calc() == "Hello World!"

def test_sum():
    assert sums(3,4) == 7
    assert sums("a","b") == "ab"

#if __name__ == '__main__':
#    test_calc()
