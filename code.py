from digitalio import DigitalInOut, Direction
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
import microcontroller
import board
import time

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

try:
    microcontroller.pin.GPIO33.deinit()
except:
    pass

led_pins = [
    board.IO21,
    board.IO47,
    microcontroller.pin.GPIO33,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = []

for pin in led_pins:
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    leds.append(led)

# main loop
while True:
    ble.start_advertising(advertisement)
    print("Waiting to connect")
    while not ble.connected:
        for i, led in enumerate(leds):
            led.value = not led.value
            time.sleep(0.25)
        pass

    print("Connected")
    while ble.connected:
         print("mhm")
