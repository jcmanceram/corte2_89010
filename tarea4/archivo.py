def main ():
    dic ={}
    n = ''
    arcivo = open('Alimentos.txt','r')
    for i in arcivo :
        if len(i.strip().split(','))>=3:
            codigo,descripcion,impuesto = i.strip().split(',')[-3:]
            dic [codigo] = [descripcion,impuesto]
    print(dic)

    while n != 'salir':
        n = input('ingrese un key de busqueda: ')

        if n == 'salir':
            break
        else:
            index_iva = dic [n][1]
            index_iva = float(index_iva)
            valor_neto = int(input('ingrese el valor neto del producto: '))
            valor_iva = valor_neto*index_iva
            valor_bruto = valor_neto - valor_iva
            print(f'el valor del iva del producto es : {valor_iva} \nel valor bruto del producto es: {valor_bruto}')

    arcivo.close()
if __name__=='__main__':
    main()