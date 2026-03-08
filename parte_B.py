import numpy as nmp
import matplotlib.pyplot as plt

Ts = 1.25e-3 #Periodo de muestreo
n = nmp.arange(0,9) #crea vector

x1 = nmp.cos(2*nmp.pi*100*n*Ts)  #definicion de señales
x2 = nmp.sin(2*nmp.pi*100*n*Ts)

R = nmp.convolve(x1, x2)
print("Correlacion =", R)

k = nmp.arange(-8,9) #Desplazamientos de la señal
plt.stem(k,R) #grafica de correlacion

plt.title("Correlacion cruzada entre x1 y x2")
plt.xlabel("k")
plt.ylabel("R[k]")

plt.show()
