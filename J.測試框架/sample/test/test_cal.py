import sys
sys.path.append("..") 
from sample.calculator import *

def test_add():
    result_value = add(1,2)
    except_value=3 
    assert result_value == except_value


def test_minus():
    result_value = minus(1,2)
    except_value=-1
    assert result_value == except_value

def test_devide():
    result_value = devide(10,2)
    except_value=5
    assert result_value == except_value


def test_multiple():
    result_value = multiple(10,2)
    except_value=20
    assert result_value == except_value