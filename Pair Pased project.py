from machine import UART,Pin
import time 

uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1)
        
# Function to send a message
def send_message(message):
    uart.write(message)


while True:
    data = uart.readline()
    if data:
        print("Received: " + data.decode())


while True:
    message_to_send = "Hello, Pico 1!"  
    send_message(message_to_send)
    time.sleep(2)  # Send a message every 2 seconds
    if uart.any():
        received_message = uart.read()
        print("Recieved message: ",received_message)

rshell -p /dev/ttyUSB0  # Replace with your Pico's USB device
cp Pico1.py /pyboard
rshell -p /dev/ttyUSB1  # Replace with the other Pico's USB device
cp Pico2.py /pyboard