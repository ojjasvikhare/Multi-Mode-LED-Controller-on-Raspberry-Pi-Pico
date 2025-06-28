# Multi-Mode LED Controller on Raspberry Pi Pico

An advanced embedded systems project built on the RP2040 microcontroller (Raspberry Pi Pico), showcasing real-time peripheral control, finite state machine logic, and interactive input handling using minimal hardware.

## 🚀 Features
- 🔴 Tap button: Toggle red LED (digital output via GPIO)
- 🟡 Hold button (0.5–2s): Adjust yellow LED brightness with potentiometer (ADC + PWM)
- 🔁 Hold >2s: Cycle through LED modes — manual, blink, breathe, off
- ⚙️ Efficient use of GPIO, ADC, and PWM peripherals with time-based input conditioning
- 💡 Built entirely in MicroPython

## 🧩 Hardware Components
- Raspberry Pi Pico (RP2040)
- 1 push button
- 1 red LED
- 1 yellow LED
- 2 × 100Ω resistors
- 1 10kΩ potentiometer
- Breadboard and jumper wires

## 🔌 Circuit Diagram
![Circuit Diagram](circuit_diagram.png)

## 📜 Code
See [`multi_mode_led_controller.py`](multi_mode_led_controller.py)

## 🧠 Skills Demonstrated
- Embedded system design on Arm Cortex-M0+ SoC
- PWM and ADC peripheral interfacing
- Press-duration-based finite state machine logic
- Real-time signal control with power-efficient, resource-minimal hardware

## 🎥 Demo
*(Insert a photo or GIF of your setup in `/assets` folder)*

## 🛠️ Tools
- MicroPython
- Thonny IDE
- Raspberry Pi Pico
