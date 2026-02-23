def promedio_notas_estudiantes():
    estudiantes = {
        "Juan": 3.5,
        "Ana": 4.2,
        "Luis": 2.8,
        "Maria": 3.0
    }

    suma = 0
    cantidad = 0

    for nombre in estudiantes:
        suma += estudiantes[nombre]
        cantidad += 1

    promedio = suma / cantidad

    print(f"Promedio del grupo: {promedio}", end=" | ")

    print("Aprobados:", end=" ")

    for nombre in estudiantes:
        nota = estudiantes[nombre]
        if nota >= 3.0:
            print(f"{nombre} ({nota})", end=" | ")

promedio_notas_estudiantes()
