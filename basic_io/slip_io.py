#!/usr/bin/python
# coding=UTF-8
import sys
import serial_io
import subprocess
import time
import net_io
sys.path.append("./util")
import util_lib


def start_if_serial_to_net(self):
    success, list = serial_io.get_serial_list()
    if success:
    #self.assertTrue(success)
        cmd = "slattach " + list.replace('\n', '').replace('\r', '') + \
            " -p slip -s 115200 &"
        success = util_lib.system_call_return(cmd)
        self.assertTrue(success)
        time.sleep(1)
        return True
    return False

def stop_if_serial_to_net(self):
    cmd = "sudo kill -9 $(ps -ef | grep slattach | " + \
        "grep -v grep | awk '{print $2}')"
    return util_lib.system_call_return(cmd)

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
    if success:
        success, slip_list = get_slip_if(self)
        for x in slip_list:
            print "slip list %s" % x
# start net if
        net_io.start_up_net_if(slip_list)
        return True, slip_list
    return False, None

def stop_testing_env_slip(self):
    stop_if_serial_to_net(self)
    return True