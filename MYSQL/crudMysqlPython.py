import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error

import sys

         
         
''' 

Creare clases  para creacion eliminacion consulta y eliminacion de datos y tambien como se requiere crear tablas y eliminarlas

'''



class BaseDeDatos:
    
    def __init__(self, nombre):
        self._nombre = nombre
    
    
    
    def crearTabla(self, mysql):
    #with mysql:
        try:
            cursor=mysql.cursor()
            cursor.execute("DROP TABLE IF EXISTS usuario1")
            cursor.execute("CREATE TABLE usuario1 (Idusuario INT PRIMARY KEY AUTO_INCREMENT, \
                     nombres VARCHAR(25), apellidoPaterno varchar (25),apellidoMaterno varchar (25), user varchar (10), pwd varchar (10))")
            print("La tabla ha sido creada");
        except Error as err:
            print("Something went wrong: {}".format(err))
            mysql.close()
            sys.exit(1)
            
    
    def insertarDatos(self, mysql):
   
        idusuario = int(input("Dame id del usuario:"))
        nombres = str(input("Dame los nombres del usuario:"))
        ap = str(input("Dame los ap  del usuario:"))
        am = str(input("Dame los am del usuario:"))
        user = str(input("Dama el user del usuario:"))
        pwd = str(input("Dame el pwd del usuario:"))
        try:

            cursor=mysql.cursor()
            sql='INSERT INTO usuario1 VALUES("%i", "%s","%s","%s","%s","%s")'%(idusuario,nombres,ap,am,user,pwd)       
            cursor.execute(sql)
            mysql.commit()
            print ("registrado correctamente")
        except Error as err:
            print("Something went wrong: {}".format(err))
    
    def eliminarDatos(self, mysql):
        idEliminado = int(input("Dame id del usuario:"))
    
        #with mysql:
        try:
            cursor=mysql.cursor()
            sql='DELETE FROM usuario1 WHERE idusuario=("%i")'%(idEliminado)
            cursor.execute(sql)
            mysql.commit()
            print ("eliminado correctamente")
        except Error as err:
            print ("error %s" %err )
            
    def actualizaDatos(self, mysql):
        idActualizado = int(input("Dame id del usuario:"))
        nombres = str(input("Dame los nombres del usuario:"))
        ap = str(input("Dame el apellido paterno del usuario:"))
        am = str(input("Dame el apellido materno del usuario :"))
        user = str(input("Dame el usuario:"))
        pwd = str(input("Dame la contraseña:"))
    
        #with mysql:
        try:
            cursor=mysql.cursor()
            sql= 'update usuario1 set nombres= "%s", apellidoPaterno ="%s", apellidoMaterno ="%s", user= "%s", pwd="%s" where idusuario = "%i"' % (nombres,ap,am,user,pwd,idActualizado)
            cursor.execute(sql)
            mysql.commit()
            print ("ACTUALIZADO correctamente")
        except Error as err:
            print ("error %s" %err )

    def listarDatos(self, mysql):
        idlista = int(input("Dame id del usuario:"))
        try:
                cursor=mysql.cursor()
                sql= 'select * from usuario1 Where idusuario="%i"'%(idlista)
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:
                        print (rows)
        except Error as err:
                print ("error %s" %err )


def menu():
        print("Elija la Opccion que necesite")
        print("1 - Crear Tabla")
        print("2 - Insertar Datos")
        print("3 - Eliminar Datos")
        print("4 - Actualizar Datos")
        print("5 - Mostrar Datos")
        print()
        eleccion = int(input("Eleccion: "))
        if eleccion == 1:
            DB.crearTabla(mysql)
        elif eleccion == 2:
            DB.insertarDatos(mysql) 
        elif eleccion == 3:
            DB.eliminarDatos(mysql)
        elif eleccion == 4:
            DB.actualizaDatos(mysql)
        elif eleccion == 5:
            DB.listarDatos(mysql)
        else:
            print("Opcion no valida")
            

if __name__ == "__main__":
    estado = False
    print("Bienvenido: Sistema de CRUD Basico")
    print("Para continuar necesitamos el nombre de la base de datos")
    baseName = str(input("Nombre: "))
    DB = BaseDeDatos(baseName)
    print("Intentando Conectarse a la base de datos: ", end="")

    try:
        mysql = mysql.connector.connect(user='root', password='', host='localhost', database=baseName)
        print("Conexion Exitosa a la base de datos: {} !!!!".format(baseName))
    except Error as err:
        print("Error al conectar:", err)
        sys.exit()
        
    while estado == False:
        menu()
        eleccion = str(input("Instruccion concluida, ¿Desea continuar? SI ,NO: s"))
        if eleccion.upper() == "NO":
            estado = True
        print()
    
        
        
        
