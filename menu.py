
#Menu
def menu():
    global opcion, salir
    print('¿Que juego quieres jugar?');
    print('1. Tres en Raya')
    print('2. Salir');
    opcion = input('Elige una opcion: ');

    if opcion == '1':
        from Juego2 import inicio_juego;
        inicio_juego();

    elif opcion == '2':
        print('Hasta luego!');
        exit();

    salir = opcion

menu()
