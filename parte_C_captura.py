#Importamos las librerias
import serial
import time
#Definimos el puerto serial asignado a la conexion con la STM32, asi como los bits por segundo (bauds) que vamos a recibir
PORT = "COM11"      
BAUDRATE = 115200
#Definimos el nombre del archivo y el tiempo de muestreo
OUTPUT_FILE = "senal_1.txt"
CAPTURE_TIME = 10.0     # segundos de muestra
#definimos el puerto serial y lo abrimos
ser = serial.Serial(PORT, BAUDRATE, timeout=1)
time.sleep(2)  # Dar tiempo a que el STM32 reinicie
#Abrimos/creamos el archivo en donde vamos a guardar los datos leidos
with open(OUTPUT_FILE, "w") as f:
    #definimos el tiempo de inicio de la lectura
    start = time.time()
    while True:
        now = time.time()
        #calculamos el tiempo transcurrido desde el inicio de la lectura
        elapsed = now - start
        # Parar a los segundos determinados anteriormente
        if elapsed >= CAPTURE_TIME:
            print("\n Captura finalizada.")
            break
        #leemos los datos del puerto serial, eliminando espacios y convirtiendo en texto los datos obtenidos
        line = ser.readline().decode(errors="ignore").strip()
        #verificamos si el valor leido es un digito y lo escribimos tanto en el archivo como en la consola.
        if line.isdigit():
            adc_value = int(line)
            f.write(f"{adc_value}\n")
#cerramos el puerto serial
ser.close()