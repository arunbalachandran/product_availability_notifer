
import httplib2, urllib, os
from BeautifulSoup import BeautifulSoup, SoupStrainer
from time import sleep

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, True)

http = httplib2.Http()
status, response = http.request('https://smile.amazon.com/i7-6700HQ-Geforce-Windows-Notebook-Computer/dp/B01K80ZQ6O/ref=sr_1_4?m=A1N2XT8FJ93CRC&s=merchant-items&ie=UTF8&qid=1479768971&sr=1-4&keywords=asus')
try:
    while (True):
        sleep(1)
        span_text = ''.join([i for i in BeautifulSoup(response,
                                            parseOnlyThese=SoupStrainer('span'))])
        if not 'Currently unavailable.' in span_text:
            while(True):
                sleep(0.5)
                GPIO.output(12, False)
                sleep(0.5)
                GPIO.output(12, True)

except:
    GPIO.cleanup()
