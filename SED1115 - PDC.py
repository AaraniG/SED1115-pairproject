'''
Project's requirement is to monitor the quality and accuracy of the
PWM output of another Pico device using serial communication.

This code is for the PWM Signal Generator and Sender
ChatGPT was used for guidance
'''
from machine import PWM,UART,Pin
import time

#Constant for PWM
PWM_PIN = Pin() # need to add the pin number
PWM_FREQ = 1000 #change to desired frequency

# Initialize PWM
pwm = PWM(PWM_PIN)
pwm.freq(PWM_FREQ)

# Initialize UART for serial communication
uart = UART(1, buadrate = 9600, tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1)

while True:
    
    desired_pwm_value = float(input("Enter desired PWM Value (0-100%): ")) # Read the desired PWM value from the user (0-100%)
    
    pwm.duty_u16(int((desired_pwm_value / 100)* 65535)) # Set the PWM duty cycle based on the desired value
    
    uart.write("Desired PWM Value : {:.2f} %\n".format(desired_pwm_value)) # Send the desired PWM value via UART
    '''
    -> uart.write(...): Writes the method of the UART object (uart). It's used to send data over the UART interface.

    -> "Desired PWM Value: {:.2f}%\n": This is a string that will be sent over UART.
        It's a message that indicates the desired PWM (Pulse Width Modulation) value.
        
        ->{:.2f}% is a placeholder for a floating-point number with two decimal places, followed by a percentage sign.
           This placeholder is later filled in with the value of desired_pwm_value.

    -> .format(desired_pwm_value): Takes the desired_pwm_value variable and inserts its value into the placeholder in the string.
                                   If desired_pwm_value is, for example, 75.25, the string will be formatted as "Desired PWM Value: 75.25%".

    -> "\n": This is a newline character, which adds a line break at the end of the message, making it easier to read and parse the received data.
    '''
    time.sleep(2) # Adds a 2-second delay before sending the next message