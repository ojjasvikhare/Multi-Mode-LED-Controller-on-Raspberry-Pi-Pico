from machine import Pin, ADC, PWM
import utime

# Setup
button = Pin(15, Pin.IN, Pin.PULL_UP)
red_led = Pin(16, Pin.OUT)
yellow_pwm = PWM(Pin(18))
yellow_pwm.freq(1000)

pot = ADC(26)

# States
red_state = False
mode = 0  # 0 = manual brightness, 1 = blink, 2 = breathe, 3 = off

# Breathing parameters
breath_direction = 1
breath_level = 0

print("Tap = Toggle red LED | Hold = Brightness | Long Hold = Change Mode")

while True:
    # Handle button
    if button.value() == 0:
        start = utime.ticks_ms()
        while button.value() == 0:
            utime.sleep(0.01)
        duration = utime.ticks_diff(utime.ticks_ms(), start)

        if duration < 500:
            # Short press: toggle red LED
            red_state = not red_state
            red_led.value(red_state)
            print("Red LED:", "ON" if red_state else "OFF")

        elif duration < 2000:
            # Medium press: read pot and set yellow LED brightness
            if mode == 0:
                pot_val = pot.read_u16()
                yellow_pwm.duty_u16(pot_val)
                brightness = int(pot_val / 655.35)
                print(f"Manual Brightness: {brightness}%")

        else:
            # Long press: change mode
            mode = (mode + 1) % 4
            print("Yellow LED Mode →", ["Manual", "Blink", "Breathe", "Off"][mode])

        utime.sleep(0.2)  # debounce

    # Mode logic for yellow LED
    if mode == 1:
        # Blink
        yellow_pwm.duty_u16(65535 if utime.ticks_ms() // 500 % 2 == 0 else 0)

    elif mode == 2:
        # Breathe (fade in/out)
        yellow_pwm.duty_u16(breath_level)
        breath_level += 1000 * breath_direction
        if breath_level >= 65000:
            breath_level = 65000
            breath_direction = -1
        elif breath_level <= 0:
            breath_level = 0
            breath_direction = 1
        utime.sleep(0.02)

    elif mode == 3:
        # Off
        yellow_pwm.duty_u16(0)

    else:
        utime.sleep(0.01)  
