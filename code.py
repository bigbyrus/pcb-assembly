from digitalio import DigitalInOut, Direction
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
import microcontroller
import board
import time

## initialize GPIO pins and BLE objects
status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

## notify the user that the device has connected to a BLE Central device
def flash_all_leds(leds):
    for _ in range(2):
        for led in leds:
            led.value = True
        time.sleep(0.25)

        for led in leds:
            led.value = False
        time.sleep(0.5)

## update the leds to reflect the ADC value received
def update_leds(leds, num_leds):
    leds[0].value = True

    if num_leds < 1:
        num_leds = 1
    elif num_leds > len(leds):
        num_leds = len(leds)

    # LEDs reflect 12-bit unsigned int, if ADC value == 4095
    # all LEDs are on
    for i in range(1, len(leds)):
        leds[i].value = (i < num_leds)


## GPIO33 doesn't work sometimes as its not defined in the .uf2
try:
    microcontroller.pin.GPIO33.deinit()
except:
    pass

## initialize LED pins as GPIO outputs
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

## start advertising connectability and NUS
ble.start_advertising(advertisement)

## main task 
while True:
    # trigger LED sequence while waiting to connect
    print("Waiting to connect")
    while not ble.connected:
        for i, led in enumerate(leds):
            led.value = not led.value
            time.sleep(0.25)
        pass

    # visually notify user that device has connected
    print("Connected")
    flash_all_leds(leds)

    # parse the data and display ADC level on LEDs
    while ble.connected:
        data = uart.read(2)
        if len(data) == 2:
            adc_value = data[0] | (data[1] << 8)
            num_leds = max(1, (adc_value * len(leds)) // 4095)
            update_leds(leds, num_leds)
        # handshake 
        uart.write("Received ADC value")