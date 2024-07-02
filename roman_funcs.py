
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

def to_roman_9_or_more(n):
    result = "" 
    multiplicador = 10 ** (len(str(n)) - 1)  # si n es 850, len seria 3, 3-1 = 2, 10 * 10 = 100
    
    while n > 0:  # Bucle para procesar cada dígito del número
        digit = n // multiplicador  # Obtiene el dígito más grande 850 // 100 = 8
        n = n % multiplicador  # Actualiza el número eliminando más grande 850 % 100 = 50
        
        
        if digit <= 3:
            result += digit * arabic_to_roman[multiplicador]
        elif digit == 4:
            result += arabic_to_roman[multiplicador] + arabic_to_roman[5 * multiplicador]
        elif digit < 9:
            result += arabic_to_roman[5 * multiplicador] + (digit - 5) * arabic_to_roman[multiplicador]
        elif digit == 9:
            result += arabic_to_roman[multiplicador] + arabic_to_roman[10 * multiplicador]
        
        multiplicador = multiplicador // 10 # Reduce el multiplicador 100 // 10 = 10

    return result

to_roman_9_or_more(890)

# def to_roman(n):
#     arab = n
#     roman = ""
#     for key, value in arabic_to_roman.items():
#         while arab >= key:
#             roman += value
#             arab -= key
#     return roman
            
