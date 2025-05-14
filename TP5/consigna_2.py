class Iterador():
    def __init__(self, datos):
        self.datos = datos
        self.index = len(datos)

    def iterador_normal(self):
        for i in range (self.index):
            print(self.datos[i])

    
    def iterador_inverso(self):
        contador = self.index
        for i in range(self.index):
            if self.index <= 0:
                raise StopIteration
            else:
                contador = (contador - 1)
                print(self.datos[contador])
        

algo = [1,2,3,4,5]
prueba = Iterador(algo)
prueba.iterador_inverso()
prueba.iterador_normal()

        