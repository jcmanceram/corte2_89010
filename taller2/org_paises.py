def paises (datos):
    pais = set()
    for fila in datos:
        pais.add(fila[4])
    return sorted(pais)