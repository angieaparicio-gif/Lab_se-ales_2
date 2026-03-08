import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
fs = 5000 #para una frecuencia de maxima de ecg de 100 Hz
Ts = 1/fs
suma_frecuencias = 0
suma_psd = 0
cont = 0
datos = np.loadtxt('senal_1.txt')
N = len (datos)
tiempo = np.arange(N) * Ts

#Media, mediana, desviación estándar, máximo, mínimo de la senal
media = np.mean(datos)
mediana = np.median(datos)
desviacion = np.std(datos)
maximo = np.max(datos)
minimo = np.min(datos)


#Transformada de Fourier
datos = datos - np.mean(datos)
Xf = fft(datos) #manda indices, no frecuencias -> fk = kfs/N
frec = fftfreq(N, Ts) #numero de puntos en espectro, intervalo entre muestras
magnitud = np.abs(Xf)/N #Magnitud normalizada
#Densidad espectral de potencia S = |Xf|^2 / Nfs
PSD = (np.abs(Xf)**2) / (N*fs)

#Media, mediana, desviación estándar de frecuencias
media_f = np.sum(frec [:N//2] * PSD[:N//2]) / np.sum(PSD[:N//2])
sum_frec2 = np.sum(((frec [:N//2]-media_f)**2) * PSD[:N//2])
desviacion_f = np.sqrt(sum_frec2 / np.sum(PSD[:N//2]))    
potencia_acum = np.cumsum(PSD[:N//2])
potencia_total = potencia_acum[-1] #Selecciona el ultimo elemento para saber la sumatoria total
mediana_pos = np.where(potencia_acum>=potencia_total/2)[0][0]
mediana_f = frec[:N//2][mediana_pos]

#Mostrar estadisticos
print (f"Media en dominio del tiempo: {media}\n")
print (f"Mediana en dominio del tiempo: {mediana}\n")
print (f"Desviacion estandar en dominio del tiempo: {desviacion}\n")
print (f"Maximo en dominio del tiempo: {maximo}\n")
print (f"Minimo en dominio del tiempo: {minimo}\n")
print (f"Media en dominio de frecuencia: {media_f}\n")
print (f"Mediana en dominio de frecuencia: {mediana_f}\n")
print (f"Desviacion estandar en dominio de frecuencia: {desviacion_f}\n")

#graficas
plt.figure(figsize=(12,6))
plt.plot(frec[:N//2], magnitud[:N//2])
plt.title('Transformada de Fourier')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True, alpha=0.3)

plt.figure(figsize=(12,6))
plt.semilogy(frec[:N//2], PSD[:N//2])
plt.title('Densidad espectral de potencia (DEP)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('DEP (V^2 / Hz)')
plt.grid(True, alpha=0.3)

plt.figure(figsize=(10,6))                                    
plt.hist(frec[:N//2], bins=50, weights=PSD[:N//2], density=True) #Se pesa cada frecuencia segun su energia
plt.title('Histograma de frecuencias')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad de probabilidad ')  
plt.grid(True, alpha=0.3)
plt.axvline(media_f, linestyle='--')
plt.show()



    