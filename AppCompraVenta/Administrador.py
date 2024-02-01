# ARCHIVOS IMPORTADOS PARA SU USO

import productos
import Usuario

# MENU ADMINISTRADOR CON SU USUARIO PREDEFINIDO

def menuAdministrador():
    usuario = "admin"
    contraseña = "admin"
    usuarioVerifica = input("Introduzca el nombre de administrador:")
    contraseñaVerifica = input("Introduzca la contraseña como administrador:")

    while True:
        if(usuario == usuarioVerifica and contraseña == contraseñaVerifica):           
            
            seleccion = input("Seleccione las siguientes opciones en pantalla como Administrador:\n1-> Crear productos.\n2-> Modificar producto.\n3-> Eliminar usuario.\n4-> Mostrar facturación total.\n0-> Salir.\n")

            if (seleccion == "1"):
                productos.nuevoProducto()
            elif (seleccion == "2"):
                productos.modificarProducto()          
            elif (seleccion == "3"):
                Usuario.eliminarUsuario()
            elif (seleccion == "4"):
                productos.facturacionTotal()
            elif (seleccion == "0"):
                print("Será redirigido al menu principal.")
                return False
            else:
                print("Opción invalida seleccione otra vez una opción.")
                continue
            
        else:
            print("Estas no son las credenciales del administrador, repita el proceso.")
            return False
