def registro_puntaje():
    id_jugador = input('Ingrese el id del jugador: ')
    nombre = input('Ingrese nombre y apellido del jugador: ')
    juego = input('Ingrese juego (Fornite/Valorant/Fifa): ')
    puntajeFo = int(input('Ingrese putaje en Fornite: '))
    puntajeVa = int(input('Ingrese putaje en Valorant: '))
    puntajeFi = int(input('Ingrese putaje en Fifa: '))
    tipo = input('Ingrese su categoria (Principiante--Avanzado--Experto): ')
    try:
        with open('registro.txt','a') as file:
            file.write(f'{id_jugador}--{nombre}--{juego}--{puntajeFo}--{puntajeVa}--{puntajeFi}--{tipo},')
            print('Registro con exito...')
    except:
        print()

def lis_puntajes():
    try:
        with open('puntajes.txt','r') as file:
            puntajes = file.readlines()
            for puntaje in puntajes:
                print(puntaje.strip())
    except FileNotFoundError:
        print('aún no registra puntaje')


def Imprimir_tipo():
    tipo = input('Ingrese el tipo para imprimir (Principiante-Avanzado-Experto): ')
    try:
        with open('tipo.txt', 'r') as file:
            tipo = file.readlines()
    except FileNotFoundError:
        print('Aún no registran puntaje')