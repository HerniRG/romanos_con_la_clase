from diccionarios_romanos import valors, roman_to_arabic

def digito_orden(n: int):
    """
    Determina el primer dígito de un número y su orden.
    
    Parámetros:
    n (int): El número a analizar.
    
    Retorna:
    tuple: Una tupla con el primer dígito y su orden.
    
    Ejemplo:
    digito_orden(4321)
    (4, 1000)
    """
    
    orden = 10 ** (len(str(n)) - 1)
    primer_digito = n // orden
    return (primer_digito, orden)

def to_roman2(n):   
    """
    Convierte un número individual en su representación romana teniendo en cuenta su orden.
    
    Parámetros:
    n (int): El número a convertir.
    
    Retorna:
    str: Representación romana del número.
    
    Ejemplo:
    to_roman2(4000)
    'MV•'
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

def divide_en_miles(n: int):
   
    lista = []
    modulo = n % 1000
    paluego = n // 1000
    
    while paluego >= 1000:
        lista.append(modulo)
        n = paluego
        modulo = n % 1000
        paluego = n // 1000
    
    if paluego <= 3:
        lista.append(n)
    else:
        lista.append(modulo)
        lista.append(paluego)
    
    return lista  

def dividir_en_digitos(n: int):
    """
    Divide un número entero en sus dígitos y los multiplica por su valor posicional.
    
    Parámetros:
    n (int): El número a dividir.
    
    Retorna:
    List[int]: Lista de los dígitos multiplicados por su valor posicional.
    
    Ejemplo:
    dividir_en_digitos(4321)
    [4000, 300, 20, 1]
    """
    n_string = str(n)
    longitud = len(n_string)
    digitos = []

    for caracter in n_string:
        digitos.append(int(caracter))
    
    resultado = []
    for i, digito in enumerate(digitos):
        orden = 10 ** (longitud - i - 1)
        resultado.append(digito * orden)
    
    print(resultado)
    return resultado

def digitos_a_roman(lista):
    """
    Convierte una lista de números en su representación romana.
    
    Parámetros:
    lista (List[int]): Lista de números a convertir.
    
    Retorna:
    str: Representación romana concatenada de los números.
    
    Ejemplo:
    digitos_a_roman([4000, 300, 20, 1])
    'MV•CCCXXI'
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
    
    Ejemplo:
    arabigo_a_romano(4127)
    'IV•CXXVII'
    """
    lista = divide_en_miles(n) # [4, 123, 135, 465]
    romano_miles = "" # str que devolveremos al final en romano
    
    for indice, miles in enumerate(lista):
        lista_miles = dividir_en_digitos(miles) # cada miles devuelve [300, 20, 1]
        romano = digitos_a_roman(lista_miles)
        
        if romano != "":
            romano_miles = romano + (indice * "•") + romano_miles # los miles los pasa a romanos, añade "•" segun el indice y añade lo que tenía ya romano

    return romano_miles

print(arabigo_a_romano(int(6.022e23)))