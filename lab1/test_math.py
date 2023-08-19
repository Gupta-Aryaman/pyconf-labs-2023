import pytest

products = [
            (2,3,1),
            (1,1,1),
            (1,2,2),
            (2,2,4),
            ]

@pytest.mark.parametrize('a,b,product', products)
def test_one_plus_one(a, b, product):
    assert a * b == product
