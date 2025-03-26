#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 
    
def factorial_rangos(extremo1, extremo2):
    if (extremo1>extremo2):
        for i in range (extremo2, (extremo1+1)):
            print("Factorial ",i,"! es ", factorial(i)) 
    elif (extremo1==extremo2):
        print("Factorial ",extremo1,"! es ", factorial(extremo1))
    else:
        for i in range (extremo1, (extremo2+1)):
            print("Factorial ",i,"! es ", factorial(i)) 



print("Por favor indique el rango de numeros a calcular el factorial:")
entrada1 = input("Inferior (valdra 1 si se deja en blanco): ")
entrada2 = input("Superior (valdra 60 si se deja en blanco): ")
print("Ahora se calculara el factorial del rango")
if not entrada1:
    factorial_rangos(1, int(entrada2))
elif not entrada2:
    factorial_rangos(int(entrada1), 60)
else:
    factorial_rangos(int(entrada1), int(entrada2))
    
