comentarios = [
    {'comentario': 'lorem imsump'},
    {'comentario': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'},
    {'comentario': 'tercer comentario'},
    {'comentario' : 'Dada una lista de entradas de un blog (donde cada entrada es un diccionario con campos como título,contenido y etiquetas), se debe filtrar y devolver solo las entradas que contengan una determinada palabra clave en el título.'},
    {'comentario' : 'no se muestra esta corto'}
]


# filtro = [notaNueva for notaNueva in notaNueva if clave in notaNueva['título']]
comentarios50 = [comentarios for comentarios in comentarios if len(comentarios['comentario']) >= 50]

print(comentarios50)