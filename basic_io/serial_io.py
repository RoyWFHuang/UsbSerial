#!/usr/bin/python
# coding=UTF-8
import inspect
import serial
import subprocess
#import slip.dbus.service

def get_serial_list():
    list = subprocess.check_output(['./getusblist.sh'])
    if list ==  "":
        return False, None
    return True, list

def serial_dev(self):
    success, list = get_serial_list()
    if success:
        self.assertTrue(success)
        serial = serial.Serial(list.replace('\n', '').replace('\r', ''), 115200)
        return True, serial
    return False, None








