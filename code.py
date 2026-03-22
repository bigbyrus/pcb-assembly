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

def flash_all_leds(leds):
    for _ in range(2):
        for led in leds:
            led.value = True
        time.sleep(0.25)

        # Turn all LEDs OFF
        for led in leds:
            led.value = False
        time.sleep(0.5)

def update_leds(leds, num_leds):
    leds[0].value = True

    if num_leds < 1:
        num_leds = 1
    elif num_leds > len(leds):
        num_leds = len(leds)

    for i in range(1, len(leds)):
        leds[i].value = (i < num_leds)

#GPIO33 doesn't work sometimes as its not defined in the .uf2
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

ble.start_advertising(advertisement)

# main loop
while True:
    print("Waiting to connect")
    while not ble.connected:
        for i, led in enumerate(leds):
            led.value = not led.value
            time.sleep(0.25)
        pass

    print("Connected")
    flash_all_leds(leds)
    while ble.connected:
        data = uart.read(2)
        if len(data) == 2:
            adc_value = data[0] | (data[1] << 8)
            num_leds = max(1, (adc_value * len(leds)) // 4095)
            update_leds(leds, num_leds)
        # handshake 
        uart.write("Received ADC value")