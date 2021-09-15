from utils.math_utils import add
from utils.math_utils import multiply


def test_add():
    assert add(2, 2) == 4


def test_multiply():
    assert multiply(5, 5) == 25