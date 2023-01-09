from src.pythontest.functions import my_sum


def test_my_sum():
    result = my_sum(2, 5)
    assert result == 7
