import funciones as fn

while True:
    print(' =======Bienvenidos======= ')
    print('1. Registrar puntajes torneo')
    print('2. listar todos los puntajes')
    print('3. Imprimir por tipo')
    print('4. Salir del programa')

    opcion = int(input('seleccione una opción: '))

    if opcion == 1:
        fn.registro_puntaje()
    elif opcion == 2:
        fn.lis_puntajes()
    elif opcion == 3:
        fn.Imprimir_tipo()
    elif opcion == 4:
        break
    else:
        print('Opción no valido, intente nuevamente')
    

