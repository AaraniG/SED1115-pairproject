'''
ChatGPT was used for guidance in adding error handling
'''
from machine import PWM, UART, Pin
import time

# Constants for PWM
PWM_PIN = Pin(2)  # Set to the GPIO Pin number
PWM_FREQ = 1000   # Desired PWM frequency

# Initialize PWM
pwm = PWM(PWM_PIN)
pwm.freq(PWM_FREQ)

# Initialize UART for serial communication
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1)

while True:
    try:
        desired_pwm_value = float(input("Enter desired PWM Value (0-100%): "))
        if 0 <= desired_pwm_value <= 100:
            # Calculate the duty cycle for the PWM signal based on the desired PWM value
            pwm.duty_u16(int((desired_pwm_value / 100) * 65535))
            # Send the desired PWM value via UART
            uart.write("Desired PWM Value: {:.2f}%\n".format(desired_pwm_value))
        else:
            print("Error: Desired PWM value should be between 0 and 100%")
    except ValueError:
        # Handle the case where the user enters invalid input
        print("Error: Invalid input. Please enter a valid number.")
    except KeyboardInterrupt:
        # Handle the case where the user presses Ctrl+C to exit the program
        print("Exiting the program.")
        break

    time.sleep(2)
