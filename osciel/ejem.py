print('SISTEMA VACACIONAL DE RAPPI\n')

nombre = input('Escribe tu nombre: ')
clave = int(input(nombre + ' escribe tu clave: '))
años = float(input(nombre + ' escribe tus años trabajados: '))

controlador = False

#Clave 1:





if clave == 1:
    if años == 1 and años < 2:
        print('\n'+ nombre + ' tienes 6 dias de vaciones.')
    elif años >= 2 and años <=6:
        print('\n'+ nombre + ' tienes 14 dias de vacaciones.')
    elif años >= 7:
        print('\n'+ nombre + ' tienes 20 dias de vacaciones.')
    else:
        print('\n'+ nombre + ' no tienes derecho a vaciones.')

#Clave 2:
elif clave == 2:
    if años == 1 and años < 2:
        print('\n'+ nombre + ' tienes 7 dias de vaciones.')
    if años >= 2 and años <=6:
        print('\n'+ nombre + ' tienes 15 dias de vacaciones.')
    elif años >= 7:
        print('\n'+ nombre + ' tienes 22 dias de vacaciones.')
    else:
        print('\n'+ nombre + ' no tienes derecho a vaciones.')

#Clave 3:
elif clave == 3:
    if años == 1 and años < 2:
        print('\n'+ nombre + ' tienes 10 dias de vaciones.')
    if años >= 2 and años <=6:
        print('\n'+ nombre + ' tienes 20 dias de vacaciones.')
    elif años >= 7:
        print('\n'+ nombre + ' tienes 30 dias de vacaciones.')
    else:
        print('\n'+ nombre + ' no tienes derecho a vaciones.')
else:
    print('\nLa clave no existe.')
    
print('\nFIN.')

