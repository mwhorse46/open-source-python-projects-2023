import RPi.GPIO as GPIO
import time
import keyboard
from picamera import PiCamera
import threading

m1 = 19
m2 = 16
m3 = 26
m4 = 20
servo = 13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
GPIO.setwarnings(False)
pwm = GPIO.PWM(servo, 50)
pwm.start(0)

GPIO.setup(m1, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)
GPIO.setup(m3, GPIO.OUT)
GPIO.setup(m4, GPIO.OUT)

GPIO.output(m1, 0)
GPIO.output(m2, 0)
GPIO.output(m3, 0)
GPIO.output(m4, 0)


def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo, False)
    pwm.ChangeDutyCycle(0)


def forward():
    GPIO.output(m1, 1)
    GPIO.output(m4, 1)
    GPIO.output(m2, 0)
    GPIO.output(m3, 0)


def backward():
    GPIO.output(m3, 1)
    GPIO.output(m2, 1)
    GPIO.output(m1, 0)
    GPIO.output(m4, 0)


def leftward():
    GPIO.output(m4, 1)
    GPIO.output(m2, 1)
    GPIO.output(m3, 0)
    GPIO.output(m1, 0)


def rightward():
    GPIO.output(m1, 1)
    GPIO.output(m3, 1)
    GPIO.output(m2, 0)
    GPIO.output(m4, 0)


def stop():
    GPIO.output(m1, 0)
    GPIO.output(m2, 0)
    GPIO.output(m3, 0)
    GPIO.output(m4, 0)


def car():
    while True:
        if keyboard.is_pressed('w'):
            forward()
            print("forward")
            time.sleep(0.3)
        if keyboard.is_pressed('s'):
            backward()
            print("back")
            time.sleep(0.3)
        if keyboard.is_pressed('d'):
            rightward()
            time.sleep(0.3)
            print("rightward")
        if keyboard.is_pressed('a'):
            leftward()
            print("leftward")
            time.sleep(0.3)

        else:
            stop()
            print("Stop")


def cam():
    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
    if keyboard.is_pressed('c'):
        camera.stop_preview()


t1 = threading.Thread(target=cam)
t2 = threading.Thread(target=car)
t1.start()
t2.start()
t1.join()
t2.join()
pwm.stop()
GPIO.cleanup()
