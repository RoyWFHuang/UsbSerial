#!/usr/bin/python
# coding=UTF-8
import serial_io
import subprocess
import time
import net_io


def start_if_serial_to_net(self):
    success, list = serial_io.get_serial_list()
    self.assertTrue(success)
    cmd = "slattach " + list.replace('\n', '').replace('\r', '') +\
        " -p slip -s 115200 &"
    if subprocess.call(cmd, shell=True):
        print "Err: Tty to slip interface fail"
        self.assertTrue(False)
    else:
        self.assertTrue(True)
    time.sleep(1)
    return True

def stop_if_serial_to_net(self):
    return_code = subprocess.call("sudo kill -9 $(ps -ef | grep slattach | " +
        "grep -v grep | awk '{print $2}')", shell=True)
    #print return_code
    return True

def get_slip_if(self):
    cmd = "ifconfig -a | grep sl | awk '{print $1}' |  grep -P '\d'"
    slip_if = subprocess.check_output(cmd, shell=True).\
replace(':', '').split('\n')
    while("" in slip_if) :
        slip_if.remove("")
    return True, slip_if

def create_testing_env_slip(self):
# init slip
    success = start_if_serial_to_net(self)
    self.assertTrue(success)
    success, slip_list = get_slip_if(self)
    for x in slip_list:
        print "slip list %s" % x
# start net if
    net_io.start_up_net_if(slip_list)
    return True, slip_list

def stop_testing_env_slip(self):
    stop_if_serial_to_net(self)
    return True