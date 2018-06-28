import RPi.GPIO as GPIO            # import RPi.GPIO module  
import time
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output

if __name__ == '__main__':
	GPIO.output(24, False)
	time.sleep(0.2)
	GPIO.output(24, True)
	GPIO.cleanup()                 # resets all GPIO ports used by this program  
