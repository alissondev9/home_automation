import serial
import time
from config import PORTA_SERIAL, BAUD_RATE
from processor import ouvir_voz

try:
    arduino = serial.Serial(PORTA_SERIAL, BAUD_RATE)
    time.sleep(2)
    print("Conexão com Arduino estabelecida!")
except:
    print("Erro: Arduino não conectado.")
    arduino = None

while True:
    comando = ouvir_voz()
    if comando:
        print(f"Você disse: {comando}")
        
        if "ligar luz" in comando:
            if arduino: arduino.write(b'L')
        elif "desligar luz" in comando:
            if arduino: arduino.write(b'D')
        elif "ligar sirene" in comando:
            if arduino: arduino.write(b'S')
        elif "sair" in comando:
            break