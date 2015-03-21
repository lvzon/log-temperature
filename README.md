# log-temperature

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
