def mayor_empleados (lectura):
    n_empleados = []
    for fila in lectura:
        n_empleados.append(int(fila[8]))
    return max(n_empleados)


