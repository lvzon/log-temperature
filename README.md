# log-temperature

Simple Linux script for logging temperature readings from one or more one-wire 
temperature sensors (DS18S20, DS1822, DS18B20), e.g. connected to a Raspberry Pi.

The python-scripts depend on the w1thermsensor module, so install that first: 
https://github.com/timofurrer/w1thermsensor

 - `init_sensors.sh` loads the neccessary kernel modules, and display the 
   temperature readings for all sensors found.

 - `read_sensors.sh` shows how to to read all sensors using shell-commands. 
   You'll need to run init_sensors first, or make sure that the `w1-gpio` 
   and `w1-therm` kernel modules are loaded.

 - `read_sensors.py` shows how to read all sensors using Python and the 
   w1thermsensor-module. You'll need to run this with sudo, run init_sensors 
   first, or make sure that the `w1-gpio` and `w1-therm` kernel modules are loaded.

 - `log_sensors.py` reads all sensors every ten seconds, calculates the mean 
   of six readings and stores this if it differs from the previous mean 
   temperature value. To reduce the number of writes to flash memory, the readings
   are stored in memory and are written to a file every six hours or so.

Author: Levien van Zon, levien AT zonnetjes.net

Note: This is my first attempt at Python, without properly learning it, 
so please excuse the somewhat messy style. I will clean this up as I learn 
more Python. :-)

The best choice for most people will be the DS18B20 sensor, which is easy to find, has a fair accuracy and also comes in a waterproofed version. It can be ordered cheaply from Ebay or your preferred electronics store. (For the differences between the DS18B20 and the DS18S20, see http://www.maximintegrated.com/en/app-notes/index.mvp/id/4377)

Connecting a sensor is very easy. You'll need a 4.7 kOhm pull-up resistor and three wires. A small breadboard may come in handy as well: http://www.reuk.co.uk/print.php?article=DS18B20-Temperature-Sensor-with-Raspberry-Pi.htm
Multiple sensors can simply be connected in series, e.g.: http://iot-projects.com/index.php?id=connect-ds18b20-sensors-to-raspberry-pi

When using long cable lengths, be sure to use a good quality cable (e.g. cat5 UTP), and avoid a star topology: http://www.maximintegrated.com/en/app-notes/index.mvp/id/148
