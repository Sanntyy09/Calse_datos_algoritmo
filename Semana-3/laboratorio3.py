## codigo de estudiantes con dividir y conquistar
def suma_y_cantidad(notas, inicio, fin):
    if inicio == fin:
        return notas[inicio], 1

    medio = (inicio + fin) // 2

    suma_izq, cant_izq = suma_y_cantidad(notas, inicio, medio)
    suma_der, cant_der = suma_y_cantidad(notas, medio + 1, fin)

    return suma_izq + suma_der, cant_izq + cant_der


def promedio_notas_estudiantes():
    estudiantes = {
        "Juan": 3.5,
        "Ana": 4.2,
        "Luis": 2.8,
        "Maria": 3.0
    }

    nombres = list(estudiantes.keys())
    notas = list(estudiantes.values())

    suma, cantidad = suma_y_cantidad(notas, 0, len(notas) - 1)
    promedio = suma / cantidad

    print(f"Promedio del grupo: {promedio:.2f}")
    print("Aprobados:")

    for nombre, nota in estudiantes.items():
        if nota >= 3.0:
            print(f"- {nombre} ({nota})")


promedio_notas_estudiantes()
