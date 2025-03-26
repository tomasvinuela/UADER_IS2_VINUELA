import matplotlib.pyplot as plt

def collatz(n):
    resultado = 0
    while n != 1:
        if n % 2 == 0: # Si el número es par, se divide entre 2
            n = (n/2)
            resultado = (resultado + 1)
        else: # Si el número es impar, se multiplica por 3 y se suma 1
            n = ((3 * n) + 1)
            resultado = (resultado + 1)
    return resultado

#creador_de_axis
ordenadas = []
absisas = []
for i in range (1, (10000+1)):
    ordenadas.append(i)
    absisas.append(collatz(i))

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(ordenadas, absisas)  # Plot some data on the Axes.
plt.show()  


#resultado absicas, n ordenadas