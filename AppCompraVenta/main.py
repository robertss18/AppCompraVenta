# ARCHIVOS IMPORTADOS PARA SU USO AQUÍ

import Administrador
import Usuario
import productos

# MENU PRINCIPAL Y MENU DEL CLIENTE

def menu():
    while True:
        seleccion = input("Seleccione las siguientes opciones en pantalla:\n1-> Entrar como administrador.\n2-> Soy cliente.\n3-> Nuevo cliente.\n0-> Salir.\n")

        if (seleccion == "1"):
            Administrador.menuAdministrador()
        elif (seleccion == "2"):
            if(Usuario.leerCliente() == True):
                menuCliente()          
        elif (seleccion == "3"):
            Usuario.nuevoCliente()
        elif (seleccion == "0"):
            print("Hasta pronto muchas gracias.")
            break
        else:
            print("Opción invalida seleccione otra vez una opción.")
            menu()

def menuCliente():
    while True:
        seleccion2 = input("¿Que desea hacer ahora?:\n1-> Ver productos.\n2-> Comprar productos.\n3-> Modificar mis datos.\n0-> Cerrar sesión.\n")

        if (seleccion2 == "1"):
            productos.verProductos()
        elif (seleccion2 == "2"):
            productos.comprarProducto()           
        elif (seleccion2 == "3"):
            Usuario.modificarDatos()
        elif (seleccion2 == "0"):
            print("Sesión cerrada....")
            break             
        else:
            print("Opción invalida seleccione otra vez una opción.")
            menuCliente()

menu()
        
    