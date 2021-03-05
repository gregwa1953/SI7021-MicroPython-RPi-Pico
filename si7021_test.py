from machine import I2C
#from SI7021 import SI7021
from SI7021 import SI7021
import time

i2c = I2C(0)
si7021 = SI7021(i2c)

# si7021.reset()

humidity = si7021.humidity()
# print('Humidity: {0}'.format(humidity))
temperature = si7021.temperature()
print('Temperature: {0}F'.format(temperature))
print('Temperature: {0}F'.format(temperature*9/5+32))
humidity = si7021.humidity()
print('Humidity: {0}'.format(humidity))
dew_point = si7021.dew_point()
print('Dew Point: {0}'.format(dew_point))
serial = si7021.serialnumber
print(serial)
revision = si7021.revision
print(revision)
while True:
    temp = si7021.temperature()
    tempf = temp*9/5+32
    hum = si7021.humidity()
    dp = si7021.dew_point()
    # print('T: {0:.2f}C  {1:.2f}F  H: {2:.2f}  D: {3:.2f}'.format(temp,tempf,hum,dp))
    print('T: {0:.2f}F  H:{1:.2f}'.format(tempf,hum))
    time.sleep(5)