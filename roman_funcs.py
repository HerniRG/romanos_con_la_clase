from diccionarios_romanos import valors, roman_to_arabic

def digito_orden(n: int):
    """
    Determina el primer dígito de un número y su orden.
    
    Parámetros:
    n (int): El número a analizar.
    
    Retorna:
    tuple: Una tupla con el primer dígito y su orden.
    """
    primer_digito = int(str(n)[0])
    orden = 10 ** (len(str(n)) - 1)
    return (primer_digito, orden)

def to_roman2(n):   
    """
    Convierte un número individual en su representación romana teniendo en cuenta su orden.
    
    Parámetros:
    n (int): El número a convertir.
    
    Retorna:
    str: Representación romana del número.
    """
    if n == 0:
        return ""
    
    primer_digito, orden = digito_orden(n)

    if primer_digito <= 3:
        result = primer_digito * valors[orden]
    elif primer_digito == 4:
        result = valors[orden] + valors[5 * orden]
    elif primer_digito < 9:
        result = valors[5 * orden] + (primer_digito - 5) * valors[orden]
    elif primer_digito == 9:
        result = valors[orden] + valors[10 * orden]

    return result

def dividir_en_digitos(n: int):
    """
    Divide un número entero en sus dígitos y los multiplica por su valor posicional.
    
    Parámetros:
    n (int): El número a dividir.
    
    Retorna:
    List[int]: Lista de los dígitos multiplicados por su valor posicional.
    """
    n_string = str(n)
    digitos = []
    for caracter in n_string:
        digitos.append(int(caracter))
    
    while len(digitos) < 4:
        digitos.insert(0, 0)
        
    resultado = [digitos[0] * 1000, digitos[1] * 100, digitos[2] * 10, digitos[3] * 1]
    print(resultado)
    return resultado

def digitos_a_roman(lista):
    """
    Convierte una lista de números en su representación romana.
    
    Parámetros:
    lista (List[int]): Lista de números a convertir.
    
    Retorna:
    str: Representación romana concatenada de los números.
    """
    result = ""
    for numero in lista:
        result += to_roman2(numero)
    return result

def arabigo_a_romano(n: int):
    """
    Convierte un número arábigo en su representación romana.
    
    Parámetros:
    n (int): El número arábigo a convertir.
    
    Retorna:
    str: Representación romana del número.
    """
    lista = dividir_en_digitos(n)
    return digitos_a_roman(lista)