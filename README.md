# SED1115-pairproject
FINAL CODES ARE NAMED:
Pico1_code_FINAL.py AND 
Pico_receiver_V3_FINAL.py


Overview:
This project involves two Raspberry Pi Pico devices (let's call them Pico 1 and Pico 2), and it's all about checking the accuracy of a special type of electrical signal called PWM (Pulse Width Modulation).

PWM - What's That?:
Imagine you have a light dimmer in your room. When you turn the knob to change the brightness of the light, you're effectively using a form of PWM. The light turns on and off very quickly, and the percentage of time it's on versus off determines the brightness.

What Pico 1 Does:
Pico 1 is like the controller. You can tell it how bright the light should be (in this case, set the PWM signal), and it sends that information to Pico 2. It's like telling your light dimmer to make the room 70% bright.

What Pico 2 Does:
Pico 2 is like the observer. It receives the "brightness" instructions from Pico 1 and then measures the actual brightness, similar to checking if the light is really 70% bright as instructed.

Communication Between Pico 1 and Pico 2:
Pico 1 and Pico 2 talk to each other using invisible "wires" (these are actually wires used for sending data), and they share information this way.

The Goal:
The main goal of this project is to make sure that when you tell Pico 1 to make the light 70% bright, Pico 2 should measure it and say, "Yes, the light is indeed 70% bright." This project helps us ensure that what we ask for (the desired PWM value) is what we actually get (the measured PWM value).

So, in simple terms, it's like having two devices talking to each other to make sure they're both on the same page about how bright the light should be (or, in technical terms, what the PWM signal should look like). This way, you can be sure that your instructions are working correctly.

*From ChatGPT
