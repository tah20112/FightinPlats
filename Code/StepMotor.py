#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
RightStepPins = [17,18,27,22]
LeftStepPins = [23, 24, 25, 5]
 
# Set all pins as output
for pin in RightStepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
 
# Set all pins as output
for pin in LeftStepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
        
StepCount = len(Seq)
StepDir = 2 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise
 
# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)
 
# Initialise variables
StepCounter = 0
 

def leftMotorTurn(steps):
      StepCounter = 0
      print StepCounter,
      print Seq[StepCounter]
 
      for pin in range(0,4):
        xpin=RightStepPins[pin]# Get GPIO

        if Seq[StepCounter][pin]!=0:
          print " Enable GPIO %i" %(xpin)
          GPIO.output(xpin, True)
        else:
      GPIO.output(xpin, False)

 
      StepCounter += StepDir
 
      # If we reach the end of the sequence
      # start again
      if (StepCounter>steps):
          return
      else:
 

def rightMotorTurn(steps)"
    # Start main loop
 
      print StepCounter,
      print Seq[StepCounter]
 
      for pin in range(0,4):
        xpin=RightStepPins[pin]# Get GPIO
        ypin=LeftStepPins[pin]# Get GPIO
        if Seq[StepCounter][pin]!=0:
          print " Enable GPIO %i" %(ypin))
          GPIO.output(ypin, True)
        else:
          GPIO.output(ypin, False)
 
      StepCounter += StepDir
 
      # If we reach the end of the sequence
      # start again
      if (StepCounter=steps):
          return
      else:

