import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

class Rfid:
    def __init__(self):
        # Inicialización de la conexión I2C
        i2c = busio.I2C(board.SCL, board.SDA)
        reset_pin = DigitalInOut(board.D6)
        req_pin = DigitalInOut(board.D12)
        self.pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin)

    # Método para leer el UID de la tarjeta continuamente
    def read_uid_continuously(self):
        # Configuración del PN532 para la lectura
        self.pn532.SAM_configuration()

        # Bucle para esperar y leer una tarjeta continuamente
        while True:
            # Check if a card is available to read
            uid = self.pn532.read_passive_target(timeout=0.5)
            print(".")  # Indicador de que está esperando una tarjeta

            if uid is not None:
                # Convertir el UID a formato hexadecimal en mayúsculas
                uid_hex = ''.join(format(x, '02X') for x in uid)
                print("UID:", uid_hex)
                break  # Salir del bucle una vez que se ha leído la tarjeta

if __name__ == "__main__":
    # Crear una instancia de la clase Rfid
    rf = Rfid()
    # Leer continuamente el UID de la tarjeta
    rf.read_uid_continuously()