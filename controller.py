from RPi import GPIO

GPIO.setmode(GPIO.BOARD)
class Controller:
    def __init__(self, in1: int, in2: int):

        self.in2 = in2
        self.in1 = in1
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)

    def forward(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)

    def back(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
