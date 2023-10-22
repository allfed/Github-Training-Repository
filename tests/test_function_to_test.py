from src.numerical import fibonacci_sum

def test_fibonacci_sum():
    assert fibonacci_sum(0) == 0
    assert fibonacci_sum(1) == 1
    assert fibonacci_sum(2) == 2
    

def test_fibonacci_sum_more():
    assert fibonacci_sum(5) == 12
    assert fibonacci_sum(10) == 143
