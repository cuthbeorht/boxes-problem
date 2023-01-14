import pytest
from main import max_number_of_units


@pytest.mark.parametrize("box_descriptions, truck_capacity, expected_units", [
    ([(1, 3), (2,2)], 4, 7), 
    ([(1, 3), (2,2), (3,1)], 4, 8), 
    ([(5, 10), (2, 5), (4, 7), (3, 9)], 10, 91)
])
def test_given_box_description_input_expect_correct_unit_output(
    box_descriptions, truck_capacity, expected_units
):
    actual_number_of_units = max_number_of_units(box_descriptions, truck_capacity)
    
    assert expected_units == actual_number_of_units
    