import RPI.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

frequencyHertz = 50
pwm = GPIO.PWM(21,frequencyHertz)
pwm.start(0)

leftPosition = 0.75
RightPosition = 2.5
middlePosition - (rightPosition - leftPosition) / 2 + leftPosition

positionList = [leftPosition, middlePosition, rightPosition, middlePosition]


msPerCycle = 1000/frequencyHertz
 

for i in range(3):
	for position in positionList:
		dutyCyclePercentage = position * 100 / float(msPerCycle)
		print "position:" + srt(position)
		print "Duty Cycle:" + str(str(dutyCyclePercentage) + "%"
		pwm.ChangeDutyCycle(int(dutyCyclePercentage))
		time.sleep(.5)
pwm.stop()

GPIO.clenup()
