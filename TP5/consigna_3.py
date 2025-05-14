class Expositor():
    def __init__(self):
        self.observadores = []

    def agregar(self, entrante):
        self.observadores.append(entrante)

    def eliminar(self, saliente):
        self.observadores.remove(saliente)

    def notificar(self, cambio):
        for observador in self.observadores:
            observador.update(cambio)

class Data(Expositor):
    def __init__(self, data):
        Expositor.__init__(self)
        self.data = data
    
    def cambio_data(self, nueva_data):
        self.data = nueva_data
        self.notificar(self.data)

class Observador():
    def __init__(self, ID):
        self.ID = ID
    
    def update(self, cambio):
        if cambio == self.ID:
            print("Se ha expuesto el ID del observador " + str(self.ID))

#Creo los observadores:
observa_1 = Observador(1111)
observa_2 = Observador(2222)
observa_3 = Observador(3333)
observa_4 = Observador(4444)

#Creo mis datos a ser observados
datos = Data(0000)

#Subscribo mis observadores a mis datos
datos.agregar(observa_1)
datos.agregar(observa_2)
datos.agregar(observa_3)
datos.agregar(observa_4)

#Hago cambios a mi data
datos.cambio_data(1111)
datos.cambio_data(8888)
datos.cambio_data(2222)
datos.cambio_data(7777)

datos.cambio_data(3333)
datos.cambio_data(4444)
datos.cambio_data(5555)
datos.cambio_data(1212)


