#blink.py
import time
import PRi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

#Blink the light 5 times.
count = 0
while count < 5:
  GPIO.output(4, True)
  time.sleep(1)
  GPIO.output(4, False)
  time.sleep(1)
  print(count)
  count += 1
  
print('End')
