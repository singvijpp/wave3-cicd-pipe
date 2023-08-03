import pytest
from area import calculate_area_square
import sys
 
# adding Folder_2 to the system path
sys.path.insert(0, '/src/main/')

def test_calculate_area_square():
    assert calculate_area_square(2) == 4
    assert calculate_area_square(2.5) == 6.25

def test_calculate_area_square_negative():
    with pytest.raises(TypeError):
        calculate_area_square(-2)

def test_calculate_area_square_string():
    with pytest.raises(TypeError):
        calculate_area_square("2")

def test_calculate_area_square_list():
    with pytest.raises(TypeError):
        calculate_area_square([2])
        