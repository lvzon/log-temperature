#!/bin/sh

sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices

cat */w1_slave 
