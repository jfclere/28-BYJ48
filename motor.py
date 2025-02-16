"""
This Raspberry Pi code was developed by newbiely.com
This Raspberry Pi code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-28byj-48-stepper-motor-uln2003-driver
"""


import RPi.GPIO as GPIO
import time

# Define GPIO pins for ULN2003 driver
# Red is a +5V always...
# Orange IN1
# Yellow IN2
# Pink IN3
# Blue IN4

IN1 = 23
IN2 = 24
IN3 = 25
IN4 = 8

# Set GPIO mode and configure pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Define constants
DEG_PER_STEP = 1.8
STEPS_PER_REVOLUTION = int(360 / DEG_PER_STEP)

# Define sequence for 28BYJ-48 stepper motor
# Try from https://components101.com/motors/28byj-48-stepper-motor
#   [O, Y, P, B]
se8 = [
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]
#   [O, Y, P, B]
se4 = [
    [0, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 1]
]

# Function to rotate the stepper motor one step
def step(delay, step_sequence):
    GPIO.output(IN1, step_sequence[0])
    GPIO.output(IN2, step_sequence[1])
    GPIO.output(IN3, step_sequence[2])
    GPIO.output(IN4, step_sequence[3])
    time.sleep(delay)
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 0)

# Function to move the stepper motor one step forward
def step_forward(delay, steps):
    for _ in range(steps):
        step(delay, se4[0])
        step(delay, se4[1])
        step(delay, se4[2])
        step(delay, se4[3])
    #    step(delay, seq[4])
    #    step(delay, seq[5])
    #    step(delay, seq[6])
    #    step(delay, seq[7])

# Function to move the stepper motor one step backward
def step_backward(delay, steps):
    for _ in range(steps):
    #    step(delay, seq[7])
    #    step(delay, seq[6])
    #    step(delay, seq[5])
    #    step(delay, seq[4])
        step(delay, se4[3])
        step(delay, se4[2])
        step(delay, se4[1])
        step(delay, se4[0])

try:
    # time the step command sequence is applied.
    delay = 0.005
    # delay = 1

    print(se4)
    print(STEPS_PER_REVOLUTION)

    while True:
        # Rotate one revolution forward (clockwise)
        step_forward(delay, STEPS_PER_REVOLUTION)
        # step_backward(delay, STEPS_PER_REVOLUTION)

        # Pause for 2 seconds
        time.sleep(2)

        # Rotate one revolution backward (anticlockwise)
        # step_backward(delay, STEPS_PER_REVOLUTION)

        # Pause for 2 seconds
        # time.sleep(2)

except KeyboardInterrupt:
    print("\nExiting the script.")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
