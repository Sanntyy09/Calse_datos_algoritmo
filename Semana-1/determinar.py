def numero_positivo_o_negativo(numero): 
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo" 
    elif numero == 0:
        return "cero"
    else:
        return "entrada no válida"  
# Ejemplos de uso
print(numero_positivo_o_negativo(10))   # Salida: positivo
print(numero_positivo_o_negativo(-9)) # salidad : negativa 
print (numero_positivo_o_negativo(2.44)) # salida : entrada no valida. 
