# -*- coding: utf-8 -*-

class Producto:
    precio = 0
    calidad = "buena"
    origen = ""
    sku = ""
    nombre = ""
    imagen = ""

    # constructor
    def __init__(self, nombre="", sku="", precio=0):
        self.nombre = nombre
        self.sku = sku
        self.precio = precio

    def establecer_imagen(self, imagen):
        # ir por la imagena internet
        # guradarla con un nombre relacionado al producto
        self.imagen = imagen



class ProductoFisico(Producto):
    fecha_de_caducidad = ""

    def esta_caduco(self):
        return True


class ProductoVirtual(Producto):
    tamano_mb = 0.0


tele = ProductoFisico(nombre="TV Sony", sku="19000928", precio=100.90)
# print(tele.nombre)
# print(tele.sku)
# print(tele.precio)
tele.fecha_de_caducidad = "10/12/2034"



pagina_web = ProductoVirtual("Pagina WEb", "1000", 5000)

# print(tele.calidad)


class Persona:
    nombre = ""
    edad = 0

    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    area = ""
    antiguedad = 0

class Directivo(Empleado):
    supervisa_area = ""
    n_supervisados = 0
