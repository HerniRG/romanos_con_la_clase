from roman_funcs import valors

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