from roman_funcs import dividir_en_digitos, arabigo_a_romano, to_roman2


def test_romanos_simples():
    assert to_roman2(1) == "I"
    assert to_roman2(5) == "V"
    assert to_roman2(10) == "X"
    assert to_roman2(50) == "L"
    assert to_roman2(100) == "C"
    assert to_roman2(500) == "D"
    assert to_roman2(1000) == "M"

def test_romanos_complejos():
    assert arabigo_a_romano(4) == "IV"
    assert arabigo_a_romano(6) == "VI"
    assert arabigo_a_romano(9) == "IX"
    assert arabigo_a_romano(21) == "XXI"
    assert arabigo_a_romano(42) == "XLII"
    assert arabigo_a_romano(44) == "XLIV"
    assert arabigo_a_romano(78) == "LXXVIII"
    assert arabigo_a_romano(99) == "XCIX"
    assert arabigo_a_romano(125) == "CXXV"
    assert arabigo_a_romano(444) == "CDXLIV"
    assert arabigo_a_romano(890) == "DCCCXC"
    assert arabigo_a_romano(999) == "CMXCIX"
    assert arabigo_a_romano(1000) == "M"
    assert arabigo_a_romano(1987) == "MCMLXXXVII"
    assert arabigo_a_romano(2021) == "MMXXI"
    assert arabigo_a_romano(3999) == "MMMCMXCIX"
    assert arabigo_a_romano(4000) == "MV•"
    assert arabigo_a_romano(5000) == "V•"
    assert arabigo_a_romano(6000) == "V•M"
    assert arabigo_a_romano(9000) == "MX•"
    assert arabigo_a_romano(10000) == "X•"


def test_romanos_1_al_9():
    assert to_roman2(1) == 'I'
    assert to_roman2(2) == 'II'
    assert to_roman2(3) == 'III'
    assert to_roman2(4) == 'IV'
    assert to_roman2(5) == 'V'
    assert to_roman2(6) == "VI"
    assert to_roman2(7) == 'VII'
    assert to_roman2(8) == 'VIII'
    assert to_roman2(9) == 'IX'

def test_romanos_10_al_90():
    assert to_roman2(10) == 'X'
    assert to_roman2(20) == 'XX'
    assert to_roman2(30) == 'XXX'
    assert to_roman2(40) == 'XL'
    assert to_roman2(50) == 'L'
    assert to_roman2(60) == "LX"
    assert to_roman2(70) == 'LXX'
    assert to_roman2(80) == 'LXXX'
    assert to_roman2(90) == 'XC'


def test_dividir_en_digitos():
    assert dividir_en_digitos(34) == [30, 4]
    
    assert dividir_en_digitos(2024) == [2000, 0, 20, 4]
    assert dividir_en_digitos(100) == [100, 0, 0]

def test_cualquier_romano():
    assert arabigo_a_romano(1999) == "MCMXCIX"

def test_to_roman2():
    assert to_roman2(10) == 'X'
    assert to_roman2(40) == 'XL'
    assert to_roman2(90) == 'XC'
    assert to_roman2(20) == 'XX'
    assert to_roman2(400) == 'CD'
    assert to_roman2(500) == 'D'
    assert to_roman2(600) == 'DC'
    assert to_roman2(900) == 'CM'
    assert to_roman2(1000) == 'M'
    assert to_roman2(1) == 'I'
    assert to_roman2(5) == 'V'
    assert to_roman2(6) == 'VI'





assert dividir_en_digitos(34) == [30, 4]
assert dividir_en_digitos(2024) == [2000, 0, 20, 4]
assert dividir_en_digitos(100) == [100, 0, 0]