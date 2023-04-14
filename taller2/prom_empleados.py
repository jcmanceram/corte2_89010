def prom (datos_pais):
    n_empleados = []
    for fila in datos_pais:
        n_empleados.append(int(fila[8]))
    n_empleados=sum(n_empleados)
    promedio = n_empleados / len(datos_pais)
    return round(promedio,2)
