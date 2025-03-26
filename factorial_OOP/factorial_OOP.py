#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

class Factorial:
    def __init__(self, argumento1=1, argumento2=60):
        self.extremo1 = int(argumento1)
        self.extremo2 = int(argumento2)
        pass
    def calculo_factorial(self, num):
        if num < 0: 
            print("Factorial de un número negativo no existe")
            return
        if num == 0: 
            print("Factorial de 0 es 1")
            return
        else: 
            fact = 1
            contador = num
            while(contador > 1): 
                fact *= contador
                contador -= 1
            print("Factorial de "+ str(num) + " es: " + str(fact))
            return
    def calculo_de_rangos(self):
        for i in range (self.extremo1, (self.extremo2 + 1)):
            self.calculo_factorial(i)
        print("Fin del calculo de factoriales")

print("Por favor indique el rango de numeros a calcular el factorial:")
entrada1 = input("Inferior (valdra 1 si se deja en blanco): ")
entrada2 = input("Superior (valdra 60 si se deja en blanco): ")
print("Ahora se calculara el factorial del rango")
entrada = Factorial(entrada1, entrada2)
entrada.calculo_de_rangos()