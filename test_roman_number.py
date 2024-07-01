from roman_funcs import to_roman


def test_romanos_simples():
    assert to_roman(1) == "I"
    assert to_roman(5) == "V"
    assert to_roman(10) == "X"
    assert to_roman(50) == "L"
    assert to_roman(100) == "C"
    assert to_roman(500) == "D"
    assert to_roman(1000) == "M"