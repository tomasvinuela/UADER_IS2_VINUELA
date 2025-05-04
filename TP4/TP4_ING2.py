#Consigna 1:
class Ping:
    def execute(dir_ping):
        for i in range (10):
            if (dir_ping[0] == "1") and (dir_ping[1] == "9") and (dir_ping[2] == "2"):
                try:
                    print("Ping a la direccion " + str(dir_ping) + " ha sido exitosa")
                except:
                    print("Ping a la direccion " + str(dir_ping) + " fallo")
    def executefree(dir_ping):
        for i in range (10):
            try:
                print("Ping a la direccion " + str(dir_ping) + " ha sido exitosa")
            except:
                print("Ping a la direccion " + str(dir_ping) + " fallo")

class PingProxy:
    def __init__(self):

        self.ping_proxy = None
        self.dir_ping = None
    
    def execute(self):
        self.ping_proxy = Ping()
        if (self.dir_ping == "192.168.0.254"):
            self.ping_proxy.executefree("www.google.com")
        else:
            self.ping_proxy.execute(self.dir_ping)

#Consigna 2:
class prod_lamina_5:
    def producir(metros = 5):
        print("La lamina que usted produjo es de una longitud de " + str(metros) + " metros")
        return int(metros)

class prod_lamina_10:
    def producir(metros = 10):
        print("La lamina que usted produjo es de una longitud de " + str(metros) + " metros")
        return int(metros)

class LaminaBridge:
    def __init__(self):
        self.espesor = 0.5
        self.ancho = 1.5
        self.largo = None

    def produce(self, tipo_prod):
        self.largo = tipo_prod.producir()
        
prueba = LaminaBridge()
prueba.produce(prod_lamina_5)

#Consigna 3:
class Pieza:
    def __init__(self, nombre_pieza):
        self.nombre = nombre_pieza

    def mostrar(self):
        print("Componente: " + str(self.nombre))

class Conjunto:
    def __init__(self, nombre_conj):
        self.nombre = nombre_conj
        self.componentes = []

    def agregar(self, pieza):
        self.componentes.append(pieza)
    
    def borrar(self, pieza):
        self.componentes.remove(pieza)

    def mostrar(self):
        print("Conjunto: " + str(self.nombre))
        for i in self.componentes:
            i.mostrar()

producto = Conjunto("Producto principal")
subconjunto_1 = Conjunto("Subconjunto 1")
for i in range(4):
    pieza = ("Pieza 1." + str(i))
    subconjunto_1.agregar(Pieza(str(pieza)))
producto.agregar(subconjunto_1)
subconjunto_2 = Conjunto("Subconjunto 2")
for i in range(4):
    pieza = ("Pieza 2." + str(i))
    subconjunto_2.agregar(Pieza(str(pieza)))
producto.agregar(subconjunto_1)
subconjunto_3 = Conjunto("Subconjunto 3")
for i in range(4):
    pieza = ("Pieza 3." + str(i))
    subconjunto_3.agregar(Pieza(str(pieza)))
producto.agregar(subconjunto_1)

producto.mostrar()

subconjunto_extra = Conjunto("Subconjunto extra")
for i in range(4):
    pieza = ("Pieza x." + str(i))
    subconjunto_extra.agregar(Pieza(str(pieza)))
producto.agregar(subconjunto_extra)

producto.mostrar()

#Consigna 4:

class NumeroBase:
    def __init__(self, numero):
        self.numero = numero

    def devolver(self):
        return self.numero

class Suma(NumeroBase):

    def __init__(self, a_transformar):
        self.a_transformar = a_transformar

    def devolver(self):
        return (self.a_transformar.devolver() + 2)
    
class Multiplicar(NumeroBase):

    def __init__(self, a_transformar):
        self.a_transformar = a_transformar

    def devolver(self):
        return (self.a_transformar.devolver() * 2)
    
class Dividir(NumeroBase):

    def __init__(self, a_transformar):
        self.a_transformar = a_transformar

    def devolver(self):
        return (self.a_transformar.devolver() / 3)
    
numero_antes = NumeroBase(5)
numero_despues = Dividir(Multiplicar(Suma(numero_antes)))
print("Antes del procesamiento: " + str(numero_antes.devolver()))
print("Despues del procesamiento: " + str(numero_despues.devolver()))

#Consigna 5:
'''
El patron flyweight podria ser util en la implementacion de juegos simples con multiples partes similares como
un juego de encontrar iguales. Cuando las cartas estan volteadas, todas tienen el mismo fondo, por lo que se podria
guardar memoria aplicando el patron flyweight para almacenar sus caracteristicas.
'''













