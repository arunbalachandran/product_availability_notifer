from time import sleep
led_num = 13
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_num, GPIO.OUT)
GPIO.output(led_num, True)

try:
	while(True):
		sleep(0.5)
		GPIO.output(led_num,True);
		sleep(0.5)
		GPIO.output(led_num, False);
except:
	GPIO.cleanup()
