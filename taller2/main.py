import org_paises
import csv
import M_empresas
import menor_empresa
import prom_empleados
def main():
    with open('organization_data.csv') as archivo:
        lectura = csv.reader(archivo)
        datos = list(lectura)
        paises = org_paises.paises(datos)
        print_paises = paises
        p_p = int(input('Ingrese el número del país: '))
        n_p = paises[p_p-1]
        print(f'El país seleccionado es: {n_p}.')
        datos_pais = []
        for fila in datos:
            if fila[4].lower() == n_p.lower():
                datos_pais.append(fila)
        e_mayor_numero = M_empresas.mayor_empleados(datos_pais)
        e_menor_numero = menor_empresa.menor_empleados(datos_pais)
        empresa_mayor = []
        empresa_menor = []
        for fila in datos_pais:
            if int(fila [8]) == e_mayor_numero:
                empresa_mayor.append(fila)
        print(f'La empresa con mayor cantidad de empleados es:\n{empresa_mayor}')
        for fila in datos_pais:
            if int(fila [8]) == e_menor_numero:
                empresa_menor.append(fila)
        print(f'La empresa con menor cantidad de trabajadore es:\n{empresa_menor}')
        promedio = prom_empleados.prom(datos_pais)
        print(f'El promedio de empleados de {n_p} es: {prom_empleados.prom(datos_pais)}.')
        print(f'La cantidad de empresas de {n_p} es: {len(datos_pais)}.')




if __name__=='__main__':
    main()