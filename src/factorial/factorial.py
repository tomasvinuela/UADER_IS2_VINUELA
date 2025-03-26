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

if (len(sys.argv) == 0 or len(sys.argv) <3):
   print("Debe informar un set de números!")
   sys.exit()
else:
    extremo1=int(sys.argv[1])
    extremo2=int(sys.argv[2])
    if (extremo1>extremo2):
        for i in range (extremo2, (extremo1+1)):
            print("Factorial ",i,"! es ", factorial(i)) 
    elif (extremo1==extremo2):
        print("Factorial ",extremo1,"! es ", factorial(extremo1))
    else:
        for i in range (extremo1, (extremo2+1)):
            print("Factorial ",i,"! es ", factorial(i)) 

