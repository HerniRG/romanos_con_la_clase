from roman_funcs import to_roman_9_or_more


def test_romanos_simples():
    assert to_roman_9_or_more(1) == "I"
    assert to_roman_9_or_more(5) == "V"
    assert to_roman_9_or_more(10) == "X"
    assert to_roman_9_or_more(50) == "L"
    assert to_roman_9_or_more(100) == "C"
    assert to_roman_9_or_more(500) == "D"
    assert to_roman_9_or_more(1000) == "M"

def test_romanos_complejos():
    assert to_roman_9_or_more(4) == "IV"
    assert to_roman_9_or_more(6) == "VI"
    assert to_roman_9_or_more(9) == "IX"
    assert to_roman_9_or_more(21) == "XXI"
    assert to_roman_9_or_more(42) == "XLII"
    assert to_roman_9_or_more(78) == "LXXVIII"
    assert to_roman_9_or_more(99) == "XCIX"
    assert to_roman_9_or_more(125) == "CXXV"
    assert to_roman_9_or_more(444) == "CDXLIV"
    assert to_roman_9_or_more(890) == "DCCCXC"
    assert to_roman_9_or_more(999) == "CMXCIX"

from roman_funcs import to_roman_9_or_more

def test_romanos_simples():
    assert to_roman_9_or_more(1) == 'I'
    assert to_roman_9_or_more(5) == 'V'
    assert to_roman_9_or_more(10) == 'X'
    assert to_roman_9_or_more(50) == 'L'
    assert to_roman_9_or_more(100) == 'C'
    assert to_roman_9_or_more(500) == 'D'
    assert to_roman_9_or_more(1000) == 'M'

def test_romanos_1_al_9():
    assert to_roman_9_or_more(1) == 'I'
    assert to_roman_9_or_more(2) == 'II'
    assert to_roman_9_or_more(3) == 'III'
    assert to_roman_9_or_more(4) == 'IV'
    assert to_roman_9_or_more(5) == 'V'
    assert to_roman_9_or_more(6) == "VI"
    assert to_roman_9_or_more(7) == 'VII'
    assert to_roman_9_or_more(8) == 'VIII'
    assert to_roman_9_or_more(9) == 'IX'

def test_romanos_10_al_90():
    assert to_roman_9_or_more(10) == 'X'
    assert to_roman_9_or_more(20) == 'XX'
    assert to_roman_9_or_more(30) == 'XXX'
    assert to_roman_9_or_more(40) == 'XL'
    assert to_roman_9_or_more(50) == 'L'
    assert to_roman_9_or_more(60) == "LX"
    assert to_roman_9_or_more(70) == 'LXX'
    assert to_roman_9_or_more(80) == 'LXXX'
    assert to_roman_9_or_more(90) == 'XC'