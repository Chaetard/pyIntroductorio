#generando el diccionario:

notaNueva = [
    {'título': 'El blog de los estudiantes de cuvalles', 'Tema': 'La vida bella de lic de TI del grupo septimo semestre!!!'},
    {'título': 'El blog del chismografo del CUVALLES', 'Tema': 'Los chismes que a casi nadie le interasan... SOLO ESTUDIANTS DEL CUVALLES'},
    
]

#definimos la clave
clave = 'cuvalles'

#hacemos la iteración y la conformación de la lista por comprensión
filtro = [notaNueva for notaNueva in notaNueva if clave in notaNueva['título']]
for notaNueva in filtro:
    print("Título:", notaNueva['título'])
    print("Tema:", notaNueva['Tema'])