
roman_to_arabic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'V•': 5000,
    'X•': 10000
}

arabic_to_roman = {
    10000: 'X•',
    9000: 'MX•',
    5000: 'V•',
    4000: 'IV•',
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

def to_roman(n):
    arab = n
    roman = ""
    for key, value in arabic_to_roman.items():
        while arab >= key:
            roman += value
            arab -= key
    return roman
            
