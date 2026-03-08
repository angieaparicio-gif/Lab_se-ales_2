import numpy as nmp
import matplotlib.pyplot as plt

Ts = 1.25e-3 #Periodo de muestreo
n = np.arange(0,9) #crea vector

x1 = np.cos(2*np.pi*100*n*Ts)  #definicion de señales
x2 = np.sin(2*np.pi*100*n*Ts)
  #si la señal se invierte se puede calcular la correlacion como una convolucion 
x2_inv = x2[::-1]
   # ya con la señal invertida, hallar correlación
R = np.convolve(x1, x2_inv)
print("Correlacion =", R)

k = np.arange(-8,9) #Desplazamientos de la señal
plt.stem(k,R) #grafica de correlacion

plt.title("Correlacion cruzada entre x1 y x2")
plt.xlabel("k")
plt.ylabel("R[k]")

plt.show()
