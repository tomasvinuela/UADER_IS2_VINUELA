#Consigna 1:
class Superior():
    def __init__(self, siguiente = None):
        self.siguiente = siguiente

    def consumidor(self, numero):
        if self.siguiente:
            return self.siguiente.consumidor(numero)
        else:
            print("No se pudo consumir el numero " + str(numero))

class Primo(Superior):
    def consumidor(self, numero):
        if self.proceso_primo(numero):
            print("El numero " + str(numero) + " es primo")
            return numero
        else:
            return super().consumidor(numero)
        
    def proceso_primo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
    
class Par(Superior):
    def consumidor(self, numero):
        if self.proceso_par(numero):
            print("El numero " + str(numero) + " es par")
            return numero
        else:
            return super().consumidor(numero)
        
    def proceso_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False
        
class Procesador:
    def __init__(self):
        self.handler = Primo(Par())

    def proceso(self):
        resultados = []
        for i in range(1, (100+1)):
            resultados.append(self.handler.consumidor(i))
        return resultados

consigna_1 = Procesador()
resultados_c1 = consigna_1.proceso()
print(resultados_c1)

