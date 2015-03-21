#! /usr/bin/python

from w1thermsensor import W1ThermSensor

import sys	# The module sys contains system functions
import time     # The module time contains timing functions
import pdb
import datetime
    
mean_temps = {};
timestamps = {};

measurements = {};

date = time.strftime("%Y%m%d")
loop = 0

write_interval = 60 * 6

try:
    while True:
      
      prev_date = date
      date = time.strftime("%Y%m%d")
      #print "Loop:", loop, "Date:", date
      

      for sensor in W1ThermSensor.get_available_sensors():
          measurements[str(sensor.id)] = []
              
      for idx in range(6):
          for sensor in W1ThermSensor.get_available_sensors():
              #if str(sensor.id) not in measurements:
              temp = sensor.get_temperature()
              measurements[str(sensor.id)].append(temp)
              #print "Measurement", idx + 1, "of", sensor.id, "gives", temp 
          time.sleep(10)
                          
      for sensor, temps in measurements.items():
          timestamp = int(time.time())
          mean_temp = round(sum(temps) / len(temps), 1)
          #print sensor + '\t' + str(timestamp) + '\t' + str(mean_temp)
          if sensor not in mean_temps:
              mean_temps[sensor] = []        
          if sensor not in timestamps:
              timestamps[sensor] = []
          if (loop <= 1 or mean_temp != mean_temps[sensor][-1]):
              mean_temps[sensor].append(mean_temp)
              timestamps[sensor].append(timestamp)
          #else:
              #print "Temperature", mean_temp, "is the same as last reading at", timestamps[sensor][-1]
              
      if date != prev_date:
          print "Date", date, "does not match previous date", prev_date

      if date != prev_date or loop > write_interval:
          loop = 0
          for sensor, list in timestamps.items():
              nvals = len(list)
              out = open(sensor + "-" + date + "-" + str(timestamps[sensor][0]) + ".dat", "w")
              for idx in range(nvals):
                  unixtime = timestamps[sensor][idx]
                  timeobj = datetime.datetime.fromtimestamp(unixtime)
                  out.write(str(unixtime) + '\t' + str(mean_temps[sensor][idx]) + timeobj.strftime("\t%Y\t%j\t%H\t%M\t%S") + "\n")
              out.close
              timestamps[sensor] = []
              mean_temps[sensor] = []

      loop += 1
      
except:

    pdb.post_mortem()
    for sensor, list in timestamps.items():
        nvals = len(list)
        out = open(sensor + "-" + date + "-" + str(timestamps[sensor][0]) + ".dat", "w")
        for idx in range(nvals):
            unixtime = timestamps[sensor][idx]
            timeobj = datetime.datetime.fromtimestamp(unixtime)
            out.write(str(unixtime) + '\t' + str(mean_temps[sensor][idx]) + timeobj.strftime("\t%Y\t%j\t%H\t%M\t%S") + "\n")
        out.close

    sys.exit()                                          
                                          
                                                  
                                                  