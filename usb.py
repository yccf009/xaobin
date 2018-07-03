# -*- coding: utf-8 -*
import serial
import serial.tools.list_ports
from easygui import *

port_list = list(serial.tools.list_ports.comports())
if len(port_list) <= 0:
    print
    "The Serial port can't find!"

else:
    for i in list(port_list):
