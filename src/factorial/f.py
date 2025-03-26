print("Por favor indique el rango de numeros a calcular el factorial:")
entrada1 = input("Inferior (valdra 1 si se deja en blanco): ")
entrada2 = input("Superior (valdra 60 si se deja en blanco): ")
print(entrada1, entrada2)
print("Ahora se calculara el factorial del rango")
if not entrada1:
    print("no hubo entrada 1")
    