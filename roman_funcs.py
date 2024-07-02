
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

valors = {
    10000: 'X•',
    5000: 'V•',
    1000: 'M',
    500: 'D',
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I'
}

def to_roman_9_or_more(n):
    result = "" 
    multiplicador = 10 ** (len(str(n)) - 1)  # si n es 850, len seria 3, 3-1 = 2, 10 * 10 = 100
    
    while n > 0:  # Bucle para procesar cada dígito del número
        digit = n // multiplicador  # Obtiene el dígito más grande 850 // 100 = 8
        n = n % multiplicador  # Actualiza el número eliminando más grande 850 % 100 = 50
        
        
        if digit <= 3:
            result += digit * valors[multiplicador]
        elif digit == 4:
            result += valors[multiplicador] + valors[5 * multiplicador]
        elif digit < 9:
            result += valors[5 * multiplicador] + (digit - 5) * valors[multiplicador]
        elif digit == 9:
            result += valors[multiplicador] + valors[10 * multiplicador]
        
        multiplicador = multiplicador // 10 # Reduce el multiplicador 100 // 10 = 10

    return result

def to_roman(n):
    
    if n <= 3:
        result = n * valors[1]
    elif n == 4:
        result = valors[1] + valors[5]
    elif n < 9:
        result = valors[5] + (n - 5) * valors[1]
    elif n == 9:
        result = valors[1] + valors[10]
    elif n <= 30:
        result = n//10 * valors[10]
    elif n == 40:
        result = valors[10] + valors[50]
    elif n < 90:
        result = valors[50] +  (n - 50) // 10 * valors[10]
    elif n == 90: 
        result = valors[10] + valors[100]
    elif n <= 300:
        result = n // 100 * valors[100]
    elif n == 400:
        result = valors[100] + valors[500]
    elif n < 900:
        result = valors[500] + (n - 500) // 100 * valors[100]
    elif n == 900:
        result = valors[100] + valors[1000]
    elif n <= 3000:
        result = n // 1000 * valors[1000]
    else:
        result = valors[n]
        

    return result


def dividir_en_digitos(n: int):
    n_string = str(n)  
    digitos = []          
    for caracter in n_string:
        digitos.append(int(caracter)) 

    while len(digitos) < 4:
        digitos.insert(0,0)

    resultado = [digitos[0] * 1000, digitos[1] * 100, digitos[2] * 10, digitos[3] * 1]

    print(resultado)

    return resultado

print(dividir_en_digitos(12))


def digitos_a_roman(lista):
    result = ""
    for numero in lista:
        result += to_roman(numero)
    return result


def arabigo_a_romano(n: int):
    lista = dividir_en_digitos(n)
    return digitos_a_roman(lista)

# def to_roman(n):
#     arab = n
#     roman = ""
#     for key, value in arabic_to_roman.items():
#         while arab >= key:
#             roman += value
#             arab -= key
#     return roman
            
