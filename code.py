import board
from digitalio import DigitalInOut, Direction
import time
#import _bleio
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
import microcontroller

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

led_pins = [
    board.IO21,
    #board.IO26, # type: ignore
    board.IO47,
    #board.IO33, # type: ignore
    #board.IO34, # type: ignore
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

pin = microcontroller.pin.GPIO34
d = DigitalInOut(pin)
d.direction = Direction.OUTPUT

# main loop
while True:
    ble.start_advertising(advertisement)
    print("Waiting to connect")
    while not ble.connected:
        print(dir(microcontroller.pin))
        for i, led in enumerate(leds):
            led.value = not led.value
            time.sleep(0.25)
        d.value = not d.value
        pass

    print("Connected")
    while ble.connected:
         print("mhm")
