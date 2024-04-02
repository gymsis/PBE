import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

class puzzle_1:
    def __init__(self):
        # Inicialización de la conexión I2C
        i2c = busio.I2C(board.SCL, board.SDA)
        reset_pin = DigitalInOut(board.D6)
        req_pin = DigitalInOut(board.D12)
        self.pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin)

        ic, ver, rev, support = self.pn532.firmware_version
        print("Found PN532 with firmware version: {0}.{1}".format(ver,rev))

        # Configurar PN532
        self.pn532.SAM_configuration()

    def read_card(self):
        uid_anterior = None
        print("Waiting for RFID/NFC card...")
        while True:
            # Check if a card is available to read
            uid = self.pn532.read_passive_target(timeout=1)
            # Try again if no card is available
            if uid is None:
                print(".")
                continue
            elif uid==uid_anterior:
                break
            #print("Found card with UID:", [hex(i) for i un uid])
            uid_anterior = uid
            uid_hex = uid.hex().upper()
        return uid_hex
    
    
