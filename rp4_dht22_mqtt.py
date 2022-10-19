import sys
import urllib.request as urllib2
import time
import adafruit_dht
from board import *
        
# Enter Your API key here
myWriteAPI = 'your own api' 
# URL where we will send the data, Don't change it
WriteURL = 'https://api.thingspeak.com/update?api_key=%s' % myWriteAPI 
dht = adafruit_dht.DHT22(D23,use_pulseio=False)
while True:
    try:
        temp = dht.temperature
        humi = dht.humidity
        # Print what we got to the REPL
        print("Temp: {:.1f} *C \t Humidity: {}%".format(temp, humi))
        conn = urllib2.urlopen(WriteURL + '&field1=%s&field2=%s' % (temp, humi))                    
        conn.close()    
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)
    time.sleep(15)
