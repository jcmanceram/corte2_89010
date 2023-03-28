def clases ():
    materias = ["calculo integral","fisica","programacion","dibujo de maquinas","fundamentos de investigacion","circuitos dc"]
    dias = ["Martes y Jueves","Martes y Jueves","Martes y Jueves","Miércoles","Viernes","Miercoles y Viernes"]
    horas = ["7:00-9:00","9:00-11:00","1:00-3:00","11:00-1:00","11:00-1:00","1:00-3:00"]
    salones = ["DB-406", "DB-404", "GO-303", "DB-305,GO-302", "DB-305","PS-204"]
    profesores = ["Jairo Lalinde","Roberto Bohorquez", "David Torres", "Elmer Cepeda", "Julian Cortes", "Hernan Pineda"]

    # Pedimos al usuario que ingrese la materia que desea consultar
    materia = input("Ingrese la materia que desea consultar: ")

    # Buscamos la información de la materia en las listas
    if materia in materias:
        index = materias.index(materia)
        dia = dias[index]
        hora = horas[index]
        salon = salones[index]
        profesor = profesores[index]
        print(f"La materia {materia} se dicta los {dia} de {hora} en el salón {salon} con el profesor {profesor}.")
    else:
        print("Lo siento, no se encontró información para la materia ingresada.")
print(clases())