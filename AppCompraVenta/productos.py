# ARCHIVO IMPORTADO PARA USAR LOS NOMBRES DE USUARIO EN FACTURAS..

import Usuario

# CLASE PRODUCTO Y SUS DIFERENTES FUNCIONES

class Productos():
    def __init__(self, id, nombre, precio):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

usuariosCopy = Usuario.usuariosLista

productosLista = {}
with open('productos.txt', 'a+') as archivo:
    archivo.seek(0)
    for linea in archivo:
        valores = linea.strip().split(',')
        id = valores[0]
        nombre = valores[1]
        precio = valores[2]
        productosLista[id] = (nombre, precio)


def nuevoProducto():
    id = input("Indique el ID del producto: ")
    nombre = input("Su nombre: ")
    precio = input("Introduzca el precio que tendra: ")
    productosLista[id] = (nombre, precio)
    objetos = Productos(id, nombre, precio)
    with open('productos.txt', 'a') as archivo:
        archivo.write(
            f"{objetos.get_id()},{objetos.get_nombre()},{objetos.get_precio()}\n")
    print("Se ha creado un nuevo producto. ¡¡Proceso guardado con exito!! ")


def modificarProducto():
    id = input("Indique el ID del producto que desea modificar: ")
    if id in productosLista:
        seleccion = input(
            "Selecciona que desea hacer...\n1. Modificar nombre.\n2. Modificar precio.\n")
        if seleccion == "1":
            nombre = input("Indique el nuevo nombre del producto: ")
            precio = productosLista[id][1]
            productosLista[id] = (nombre, precio)
            objetos = Productos(id, nombre, precio)
            procesoCambio(id,objetos)
        elif seleccion == "2":
            precio = input("Indique el nuevo precio del producto: ")
            nombre = productosLista[id][0]
            productosLista[id] = (nombre, precio)
            objetos = Productos(id, nombre, precio)
            procesoCambio(id,objetos)
        else:
            print("Opción no valida repita el proceso...")
    else:
        print("Opción no valida repita el proceso...")         
def procesoCambio(id, objetos):   
    with open('productos.txt', 'r+') as archivo:
        lineas = archivo.readlines()
        for i, linea in enumerate(lineas):
            partes = linea.strip().split(',')
            if partes[0] == id:
                lineas[i] = f"{objetos.get_id()},{objetos.get_nombre()},{objetos.get_precio()}\n"
                archivo.seek(0)
                archivo.writelines(lineas)
                print("Producto modificado con éxito.")
                return
    print("No se ha encontrado el producto que desea modificar.")


def verProductos():
    print("A continuación se mostrarán los productos disponibles: ")
    print(productosLista)

# A PARTIR DE AQUÍ ESTA EL APARTADO RELACIONADO CON LAS FACTURAS Y SU ARCHIVO TXT

def comprarProducto():
    seleccionProducto = input("A continuación escriba el id del producto que desea comprar: ")
    nombreFactura = input("Introduzca el usuario que tendra la factura: ")
    if nombreFactura in usuariosCopy:
        if seleccionProducto in productosLista:
            nombre = productosLista[seleccionProducto][0]
            precio = productosLista[seleccionProducto][1]
            productosLista[nombreFactura] = (nombre, precio)
            producto = Productos(nombreFactura, nombre, precio)
            procesoCompra(producto)
            
        else:
            print("El producto seleccionado no existe.")
    else:
        print("El nombre introducido no pertenece a ningún cliente, repita el proceso...")
def procesoCompra(producto):    
    with open('facturas.txt', 'a+') as archivo:
        archivo.write(
            f"{producto.get_id()},{producto.get_nombre()},{producto.get_precio()}\n")  #se puede escribir sin id
        archivo.seek(0)
    print("Compra exitosa!!\nSe ha creado una nueva factura. ¡¡Proceso guardado con exito!! ")
    
facturacionLista = {}
with open('facturas.txt', 'a+') as archivo:
    # lo de abajo hace que el puntero se mueva al inicio del archivo para leer los datos
    archivo.seek(0)
    for linea in archivo:
        valores = linea.strip().split(',')       
        usuario = valores[0]
        nombre = valores[1]
        precio = valores[2]       
        facturacionLista[usuario] = (nombre, precio) 

def facturacionTotal():
    tipoFacturación = input("Selecciona el tipo de facturación que desea ver: \n1. Para facturación total.\n2. Elegir por usuario.\n")
    if tipoFacturación == "1":
        total = sum(int(value[1]) for value in facturacionLista.values())
        print("La facturación total es de:",total,"€")
    elif tipoFacturación == "2":
        selectUsuario = input("Intoruzca el usuario para ver su facturación: ")
        if selectUsuario in facturacionLista:          
            totalUser = sum(int(value[1]) for key, value in facturacionLista.items() if key == selectUsuario)
            print("El usuario",selectUsuario,"tiene un total de:",totalUser,"€ facturados")           
    else:
        print("Repita el proceso...")