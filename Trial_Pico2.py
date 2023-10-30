'''
Project's requirement is to monitor the quality and accuracy of the
PWM output of another Pico device using serial communication.

This code is for the PWM Signal Receiver and Analyzer (Pico 2)
ChatGPT was used for guidance
'''
from machine import UART, Pin, PWM
import time

# Constants for PWM
PWM_PIN = Pin()  # Replace with the actual PWM pin number
PWM_FREQ = 1000   # Change to your desired PWM frequency

# Initialize PWM for measuring the PWM signal
pwm_receiver = PWM(PWM_PIN)
pwm_receiver.freq(PWM_FREQ)

# Initialize UART for serial communication
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))  # Replace tx and rx pins with actual pin numbers

while True:
    if uart.any():
        received_message = uart.read().decode().strip()

        # Check if the received message contains the desired PWM value
        if "Desired PWM Value" in received_message:
            desired_pwm_value = float(received_message.split(":")[1].strip()[:-1])
            
            # Read and measure the actual PWM value
            measured_pwm_value = (pwm_receiver.duty_u16() / 65535) * 100  # Convert to a percentage

            # Calculate the difference between desired and measured PWM values
            difference = desired_pwm_value - measured_pwm_value
            print("Measured PWM Value: {:.2f}%".format(measured_pwm_value))
            print("Difference: {:.2f}%".format(difference))
