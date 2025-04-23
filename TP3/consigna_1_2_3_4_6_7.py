import math


#Consigna 1
class Factorial:
    def __init__(self, numero):
        self.numero = numero
        self.factorial = math.factorial(numero)
    
    def __str__(self):
        return f"El factorial de {self.numero} es {self.factorial}"
    

#Consigna 2
class Impuestos:
    def __init__(self, importe_base):
        self.importe_base = importe_base
        self.IVA = (importe_base + ((21/100)*importe_base))
        self.IBB = (importe_base + ((5/100)*importe_base))
        self.cont_municipales = (importe_base + ((1.2/100)*importe_base))
    
    def __str__(self):
        return f"Impuesto original: {self.importe_base}\nImpuesto mas IVA: {self.IVA}\nImpuesto mas IBB: {self.IBB}\nImpuesto mas contribuciones municipales: {self.cont_municipales}\n"
    

#Consigna 3:
class Comida:
    def __init__(self, tipo, forma_entrega):
        self.tipo_comida = tipo
        self.forma_entrega = forma_entrega

    def __str__(self):
        if "Mostrador" in self.forma_entrega:
            return f"La comida debe entregarse en el mostrador"
        if "Cliente" in self.forma_entrega:
            return f"La comida sera retirada por el cliente"
        if "Delivery" in self.forma_entrega:
            return f"La comida debe entregarse por delivery"
        
    
hamburguesa_1 = Comida("Hamburguesa", "Mostrador")
print(hamburguesa_1)
hamburguesa_2 = Comida("Hamburguesa", "Cliente")
print(hamburguesa_2)
hamburguesa_3 = Comida("Hamburguesa", "Delivery")
print(hamburguesa_3)


#Consigna 4:
class Factura:
    def __init__(self, importe_total, tipo_cliente):
        self.importe_total = importe_total
        self.tipo_cliente = tipo_cliente

    def __str__(self):
        if "Responsable" in self.tipo_cliente:
            return f"El total de su factura es{self.importe_total} y es de tipo IVA Responsable"
        if "No inscripto" in self.tipo_cliente:
            return f"El total de su factura es{self.importe_total} y es de tipo IVA No Inscripto"
        if "Exento" in self.tipo_cliente:
            return f"El total de su factura es{self.importe_total} y es de tipo IVA Exento"
        

#Consigna 6:
class Fotocopiadora(object):

    def __init__(self, material):
        self.material = material

    def get(self):
        return self.material
    
    def __str__(self):
        return f"{self.material}"

    def clone(self):
        return Fotocopiadora(self.material)


original=Fotocopiadora("Nota a la FCyT")
print(original)
copia_1 = original.clone()
print(copia_1)
copia_2 = copia_1.clone()
print(copia_2)

#Consigna 7
#Una situacion donde factory_abstract sea util podria ser una sandwicheria. Aunque las hamburguesas, sanguches y sanguches de miga sean distintos
#Su base sigue siendo la de comida encerrada en 2 panes, por lo que abstractamente pertenecerian a la misma familia a pesar de tener sus otros elementos caracteristicos