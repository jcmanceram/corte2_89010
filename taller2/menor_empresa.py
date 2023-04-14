def menor_empleados (lectura):
    n_empleados = []
    for fila in lectura:
        n_empleados.append(int(fila[8]))
    return min(n_empleados)
