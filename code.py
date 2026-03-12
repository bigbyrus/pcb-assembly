import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
import time
import pwmio

    #led = DigitalInOut(pin)
    #led.direction = Direction.OUTPUT
    #leds.append(led)


# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26,
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

# stores PWMOut objects for each pin, in the same 
leds = []


# iterate through led_pins to set each LED as PWM Output 
#   (this might not work if pins aren't allowed to output pwm)
for pin in led_pins:
    pwm = pwmio.PWMOut(pin)
    pwm.duty_cycle = 2 ** 15
    leds.append(pwm)
    time.sleep(0.1)



# main loop
while True:
    # read and print microphone data
    volume = microphone.value
    print(volume)
    
    # increase i [0,11) and iterate through LED pins
    for i, led in enumerate(leds):
        j = range(11)
        print("LED: ", j)

        led.duty_cycle = 2 ** j
        time.sleep(0.5)