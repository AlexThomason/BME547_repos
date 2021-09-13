def test_hdl_analysis_normal():
    from blood_calculator import check_HDL
    answer = check_HDL(65)
    expected = "Normal"
    assert answer ==expected


def test_hdl_analysis_borderline_low():
    from blood_calculator import check_HDL
    answer = check_HDL(50)
    expected = "Borderline Low"
    assert answer ==expected

def test_hdl_analysis_low():
    from blood_calculator import check_HDL
    answer = check_HDL(35)
    expected = "Low"
    assert answer ==expected


import pytest

# @pytest is a decorator - must be put before the test function. A decorator performs the function before and after the function runs.
@pytest.mark.parametrize("HDL_value, expected",[   
(65,"Normal"),
(45,"Borderline Low"),
(15,"Low"),
(70, "Normal")])
def test_hdl_analysis(HDL_value, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_value)
    assert answer ==expected
