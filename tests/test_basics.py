import pytest
import src.basics


numList = [1, 2, 3, 4, 5, 6, 7]

def test_square():
    assert basics.squareList(numList) == [1,4,9,16,25,36,49]

def test_maths():
    assert basics.basicMaths()== 60

def test_selection():
    assert basics.basicSelection(17)=="Old enough to drive"
