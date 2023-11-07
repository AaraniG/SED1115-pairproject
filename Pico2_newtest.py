# ... (previous code)

while True:
    if uart.any():
        received_message = uart.read().decode().strip()

        # Check if the received message contains the desired PWM value
        if "Desired PWM Value" in received_message:
            desired_pwm_value = float(received_message.split(":")[1].strip()[:-1])

            # Debugging: Print the raw PWM duty cycle value
            raw_pwm_duty_cycle = pwm_receiver.duty_u16()
            print("Raw PWM Duty Cycle:", raw_pwm_duty_cycle)

            # Calculate and print the measured PWM value
            measured_pwm_value = (raw_pwm_duty_cycle / 65535) * 100  # Convert to a percentage
            print("Measured PWM Value: {:.2f}%".format(measured_pwm_value))

            # Calculate the difference between desired and measured PWM values
            difference = desired_pwm_value - measured_pwm_value
            print("Difference: {:.2f}%".format(difference))
