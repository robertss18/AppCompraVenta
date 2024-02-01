# CLASE CLIENTE Y SUS DIFERENTES FUNCIONES

class Usuario():
    def __init__(self, nombre, apellido, usuario, password):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__password = password

    def get_nombre(self):
        return self.__nombre 
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def get_usuario(self):
        return self.__usuario
    def set_usuario(self,usuario):
        self.__usuario = usuario
    def get_password(self):
        return self.__password
    def set_password(self,password):
        self.__password = password    


usuariosLista = {}
with open('usuarios.txt', 'a+') as archivo:
    archivo.seek(0)
    for linea in archivo:
        valores = linea.strip().split(',')       
        nombre = valores[0]
        apellido = valores[1]
        usuario = valores[2]
        contraseña = valores[3]
        usuariosLista[usuario] = (nombre, apellido, contraseña)

def nuevoCliente():
    nombre = input("Indique su nombre: ")
    apellido = input("Su apellido: ")
    usuario = input("Introduzca su nombre de usuario: ")
    contraseña = input("Cree una contraseña: ")
    objetos = Usuario(nombre, apellido, usuario, contraseña)
    with open('usuarios.txt', 'a') as archivo:
        archivo.write(f"{objetos.get_nombre()},{objetos.get_apellido()},{objetos.get_usuario()},{objetos.get_password()}\n")
    print("Bienvenido, has sido registrado como nuevo cliente!!\nYa puede iniciar sesión como cliente...")

def leerCliente():
    enterusuario = input("Escriba su usuario: ")
    enterpassword = input("Escriba su contraseña: ")
    objetos = Usuario("","",enterusuario, enterpassword)
    if buscar_usuario(objetos):
        print("¡¡Bienvenido a la zona clientes!!")
        return True
    else:
        print("Usuario o contraseña incorrectos, vuelva a intentarlo.")
def buscar_usuario(objetos):
    with open('usuarios.txt', 'r') as archivo:
        for linea in archivo:
            campos = linea.strip().split(',')   
            if campos[2] == objetos.get_usuario() and campos[3] == objetos.get_password():
                return True
    return False

def eliminarUsuario():
    print("A continucación se mostrarán los usuarios y sus datos: ")
    print(usuariosLista)
    usuarioEliminar = input("Ya puede introducir el usuario que quiere eliminar: ")
    if usuarioEliminar in usuariosLista:
        del usuariosLista[usuarioEliminar]
        with open('usuarios.txt', 'r+') as archivo:
            lineas = archivo.readlines()   
            archivo.seek(0) 
            for linea in lineas:
                partes = linea.strip().split(',')
                if partes[2] != usuarioEliminar:
                    archivo.write(linea)
            archivo.truncate() 
        print("¡¡Usuario eliminado con exito!!")  
    else:
        print("No se ha encontrado el usuario que desea eliminar.")

def modificarDatos():
    usuario = input("Indique el usuario que desea modificar: ")
    if usuario in usuariosLista:
        seleccion = input(
            "Selecciona que desea hacer...\n1. Modificar nombre.\n2. Modificar apellido.\n3. Modificar contraseña.\n4. Modificar usuario.\n")
        if seleccion == "1":
            nombre = input("Indique el nuevo nombre: ")
            apellido = usuariosLista[usuario][1]            
            contraseña = usuariosLista[usuario][2]
            usuariosLista[usuario] = (nombre,apellido, contraseña)
            objetos = Usuario(nombre, apellido, usuario, contraseña)
            procesoCambio(usuario,objetos)
        elif seleccion == "2":
            apellido = input("Indique el nuevo apellido: ")
            nombre = usuariosLista[usuario][0]
            contraseña = usuariosLista[usuario][2]
            usuariosLista[usuario] = (nombre,apellido, contraseña)
            objetos = Usuario(nombre, apellido, usuario, contraseña)
            procesoCambio(usuario,objetos)
        elif seleccion == "3":
            contraseña = input("Indique la nueva contraseña: ")
            nombre = usuariosLista[usuario][0]
            apellido = usuariosLista[usuario][1]
            usuariosLista[usuario] = (nombre,apellido, contraseña)
            objetos = Usuario(nombre, apellido, usuario, contraseña)
            procesoCambio(usuario,objetos)
        elif seleccion == "4":
            newUser = input("Indique el nuevo usuario: ")
            nombre = usuariosLista[usuario][0]
            apellido = usuariosLista[usuario][1]
            contraseña = usuariosLista[usuario][2]
            usuariosLista[usuario] = (nombre,apellido, contraseña)
            objetos = Usuario(nombre, apellido, newUser, contraseña)
            procesoCambio(usuario,objetos)
        else:
            print("Opción no valida repita el proceso...")
    else:
        print("Opción no valida repita el proceso...")         
def procesoCambio(usuario, objetos):   
    with open('usuarios.txt', 'r+') as archivo:
        lineas = archivo.readlines()
        for i, linea in enumerate(lineas):
            partes = linea.strip().split(',')
            if partes[2] == usuario:
                lineas[i] = f"{objetos.get_nombre()},{objetos.get_apellido()},{objetos.get_usuario()},{objetos.get_password()}\n"
                archivo.seek(0)
                archivo.writelines(lineas)
                print("Usuario modificado con éxito.")
                return
    print("No se ha encontrado el usuario que desea modificar.")



