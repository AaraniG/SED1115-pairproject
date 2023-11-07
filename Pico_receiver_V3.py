'''
Project's requirement is to monitor the quality and accuracy of the
PWM output of another Pico device using serial communication.
This code is for the PWM Signal Receiver and Analyzer (Pico 2)
ChatGPT was used for guidance
'''
from machine import UART, Pin, PWM, ADC
import time

# Constants for PWM
PWM_PIN = Pin(28)  # PWM pin number
PWM_FREQ = 1000   # PWM frequency

# Initialize PWM for measuring the PWM signal
pwm_receiver = ADC(PWM_PIN) #lab 3


# Initialize UART for serial communication
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))  # Replace tx and rx pins with actual pin numbers

while True:
    if uart.any():
        received_message = uart.read().decode().strip()
        print("Recieved Message from Pico 1 -> {}".format(received_message)) #prints the received message from Pico 1

        # Check if the received message contains the desired PWM value
        if "Desired PWM Value" in received_message:
            desired_pwm_value = float(received_message.split(":")[1].strip()[:-1])
            
            # Read and measure the actual PWM value
            measured_pwm_value = (pwm_receiver.read_u16() / 65535) * 100  # Convert to a percentage

            # Calculate the difference between desired and measured PWM values
            difference = desired_pwm_value - measured_pwm_value
            print("Measured PWM Value (Duty Cycle) : {:.2f}%".format(measured_pwm_value)) #The acutal duty cycle of the PWM signal that Pico 2 has measured
            print("Difference: {:.2f}%".format(difference)) #How much the measured PWM value differs from the desired PWM value in Pico 1