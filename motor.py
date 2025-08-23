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

# Like
#IN1 = 23
#IN2 = 24
#IN3 = 25
#IN4 = 8

# Define constants
# the specs say:
# Steps/revolution 	32
# Gears 	64:1 reduction
STEPS_PER_REVOLUTION = 512
#DEG_PER_STEP = 1.8
#STEPS_PER_REVOLUTION = int(360 / DEG_PER_STEP)

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

class motor():
  def __init__(self, IN1 = 23, IN2 = 24, IN3 = 25, IN4 = 8):
    self.IN1 = IN1
    self.IN2 = IN2
    self.IN3 = IN3
    self.IN4 = IN4

    # Set GPIO mode and configure pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.IN1, GPIO.OUT)
    GPIO.setup(self.IN2, GPIO.OUT)
    GPIO.setup(self.IN3, GPIO.OUT)
    GPIO.setup(self.IN4, GPIO.OUT)


# Function to rotate the stepper motor one step
  def step(self, delay, step_sequence):
    GPIO.output(self.IN1, step_sequence[0])
    GPIO.output(self.IN2, step_sequence[1])
    GPIO.output(self.IN3, step_sequence[2])
    GPIO.output(self.IN4, step_sequence[3])
    time.sleep(delay)
    GPIO.output(self.IN1, 0)
    GPIO.output(self.IN2, 0)
    GPIO.output(self.IN3, 0)
    GPIO.output(self.IN4, 0)

# Functions to move the stepper motor one step forward
  def step_forward(self, delay, steps):
    for _ in range(steps):
        self.step(delay, se4[0])
        self.step(delay, se4[1])
        self.step(delay, se4[2])
        self.step(delay, se4[3])

  def step_forward8(self, delay, steps):
    for _ in range(steps):
        self.step(delay, se8[0])
        self.step(delay, se8[1])
        self.step(delay, se8[2])
        self.step(delay, se8[3])
        self.step(delay, se8[4])
        self.step(delay, se8[5])
        self.step(delay, se8[6])
        self.step(delay, se8[7])

# Functions to move the stepper motor one step backward
  def step_backward(self, delay, steps):
    for _ in range(steps):
        self.step(delay, se4[3])
        self.step(delay, se4[2])
        self.step(delay, se4[1])
        self.step(delay, se4[0])
  def step_backward8(self, delay, steps):
    for _ in range(steps):
        self.step(delay, se8[7])
        self.step(delay, se8[6])
        self.step(delay, se8[5])
        self.step(delay, se8[4])
        self.step(delay, se8[3])
        self.step(delay, se8[2])
        self.step(delay, se8[1])

  def reset(self, ):
     delay = 0.005
     for _ in range(12):
        self.step_backward8(delay, STEPS_PER_REVOLUTION)

if __name__ == "__main__":
    try:
        # time the step command sequence is applied.
        delay = 0.005
        # delay = 1

        mymotor = motor(IN1 = 26, IN2 = 19, IN3 = 13, IN4 = 6)
        print(se4)
        print(STEPS_PER_REVOLUTION)
        mymotor.step_forward8(delay, 1)

        while True:
            # Rotate one revolution forward (clockwise)
            mymotor.step_forward8(delay, STEPS_PER_REVOLUTION)
            # step_backward(delay, STEPS_PER_REVOLUTION)

            # Pause for 2 seconds
            time.sleep(2)

            # Rotate one revolution backward (anticlockwise)
            mymotor.step_backward8(delay, STEPS_PER_REVOLUTION)

            # Pause for 2 seconds
            # time.sleep(2)

    except KeyboardInterrupt:
        print("\nExiting the script.")

    finally:
        # Clean up GPIO settings
        GPIO.cleanup()
