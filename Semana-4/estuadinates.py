def promedio_notas_dp(notas):
  
    n = len(notas)
    
    if n == 0:
        return 0

    # Tabla DP n x n para almacenar sumas de rangos
    dp = [[0] * n for _ in range(n)]

    # Casos base: diagonal principal (un solo elemento)
    for i in range(n):
        dp[i][i] = notas[i]

    # Llenado DP: calcula la suma acumulada para cada rango [i, j]
    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            # dp[i][j] = suma de notas[i] hasta notas[j]
            dp[i][j] = dp[i][j - 1] + notas[j]

    # El promedio es la suma total dividida por la cantidad de notas
    promedio = dp[0][n - 1] / n
    return promedio


def promedio_con_aprobados_dp(estudiantes_dict):

    
    # Convertir diccionario a lista de tuplas (nombre, nota)
    nombres = list(estudiantes_dict.keys())
    notas = list(estudiantes_dict.values())
    n = len(notas)

    if n == 0:
        return 0, []

    # Tabla DP para sumas
    dp = [[0] * n for _ in range(n)]

    # Casos base
    for i in range(n):
        dp[i][i] = notas[i]

    # Llenado DP
    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            dp[i][j] = dp[i][j - 1] + notas[j]

    # Calcular promedio
    promedio = dp[0][n - 1] / n

    # Identificar aprobados
    aprobados = [(nombres[i], notas[i]) for i in range(n) if notas[i] >= 3.0]

    return promedio, aprobados


# Ejemplo de uso
estudiantes = {
    "Alice": 4.5,
    "Bob": 2.8,
    "Charlie": 3.2,
    "Diana": 1.9
}
promedio, aprobados = promedio_con_aprobados_dp(estudiantes)
print(f"Promedio: {promedio:.2f}")
print("Aprobados:")
for nombre, nota in aprobados:
    print(f"{nombre}: {nota}")
    