def numero_primo(numero):
    if numero > 1:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return "no es primo"
        return "es primo"
    elif  numero >= 0: 
        return "es positivo pero no es primo"
    elif numero < 0:
        return "es negativo"
    else:
        return "entrada no válida"

def serie_fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = []
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b 
    return fibonacci_sequence

def main ():
    numero = int(input("Ingrese un número para verificar si es primo: "))
    resultado_primo = numero_primo(numero)
    print(f"El número {numero} {resultado_primo}.")
    n = int(input("Ingrese la cantidad de términos de la serie Fibonacci que desea generar: "))
    fibonacci_sequence = serie_fibonacci(n)
    print(f"Los primeros {n} términos de la serie Fibonacci son: {fibonacci_sequence}")
main ()