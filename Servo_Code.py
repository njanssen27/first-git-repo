import RPi.GPIO as GPIO
import time

# Define GPIO pins for servos
servo1_pin = 17  # GPIO 17 (Pin 11)
servo2_pin = 18  # GPIO 18 (Pin 12)
servo3_pin = 27  # GPIO 27 (Pin 13)# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1_pin, GPIO.OUT)
GPIO.setup(servo2_pin, GPIO.OUT)
GPIO.setup(servo3_pin, GPIO.OUT)
    # Set up PWM (50Hz for servos)
servo1 = GPIO.PWM(servo1_pin, 50)
servo2 = GPIO.PWM(servo2_pin, 50)
servo3 = GPIO.PWM(servo3_pin, 50)

# Start PWM with 0 degree position
servo1.start(2.5)  # 0 degrees
servo2.start(2.5)  # 0 degrees
servo3.start(2.5)  # 0 degrees

time.sleep(1)  # Initial stabilization delay

# Function to convert angle to duty cycle
def angle_to_duty_cycle(angle):
    return 2.5 + (angle / 18.0)  # Converts angle (0-180) to PWM duty cycle

# Function to move servo gradually
def move_servo_slowly(servo, start_angle, end_angle, step_delay=0.05, step_size=2):
    """ Moves the servo from start_angle to end_angle slowly in small steps """
    if start_angle < end_angle:
        step = step_size  # Increase angle
    else:
        step = -step_size  # Decrease angle

    for angle in range(start_angle, end_angle + step, step):  # Gradual movement
        duty = angle_to_duty_cycle(angle)
        servo.ChangeDutyCycle(duty)
        time.sleep(step_delay)  # Small delay for smooth motion

    # Ensure the final position is reached
    servo.ChangeDutyCycle(angle_to_duty_cycle(end_angle))
    time.sleep(0.5)  # Final hold
def set_angle(servo, angle):
    duty = 2.5 + (angle / 18.0)  # Convert angle to duty cycle
    servo.ChangeDutyCycle(duty)
    time.sleep(1)  # Wait for servo to reach position
# Move Servos in Sequence (Slowly)
move_servo_slowly(servo1, 0, 130)  # Step 1: Move Servo 1 to 135 degrees
time.sleep(1)

set_angle(servo3, 90)  # Step 2: Move Servo 3 to 90 degreessss
set_angle(servo2, 90)  # Step 2: Move Servo 2 to 90 degrees
time.sleep(.1)

set_angle(servo2, 0)  # Step 3: Move Servo 2 back to 0 degrees
set_angle(servo3, 0)  # Step 3: Move Servo 3 back to 0 degrees
time.sleep(1)

move_servo_slowly(servo1, 130, 0)  # Step 4: Move Servo 1 back to 0 degrees
time.sleep(1)

# Cleanup
servo1.stop()
servo2.stop()
servo3.stop()
GPIO.cleanup()  # Release GPIO pins 
