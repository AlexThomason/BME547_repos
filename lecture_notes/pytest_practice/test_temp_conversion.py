# test_temp_conversion.py

def test_celsius_from_farhenheit():
    from temp_conversion import celcius_from_farhenheiit
    result = celcius_from_farhenheiit(20)
    expected = 68
    assert result == expected