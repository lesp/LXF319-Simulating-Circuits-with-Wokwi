import time
from machine import Pin
led = Pin(16, Pin.OUT)
button = Pin(22, Pin.IN, Pin.PULL_DOWN)
print("Blinking an LED")

while True:
    if button.value():
        for i in range(10):
            print("Blink")
            led.toggle()
            time.sleep(0.2)
    else:
        pass

