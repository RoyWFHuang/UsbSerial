
#!/usr/bin/python
# coding=UTF-8
import sys
import subprocess
sys.path.append("./util")
import util_lib

def start_up_net_if(net_if = []):
    #cmd = []
    for x in net_if:
        cmd_str = "sudo ifconfig " + x +" up"
        subprocess.call(cmd_str, shell=True)
        #cmd.append(cmd_str)
    return True

def setup_ipv6_ip(net_if = "", addr = "", prefix = ""):
    cmd = "sudo ifconfig " + net_if +" inet6 add " + addr + "/" + prefix
    return util_lib.system_call_return(cmd)

def setup_ipv4_ip(net_if = "", addr = "", prefix = ""):
    cmd = "sudo ifconfig " + net_if +" " + addr + "/" + prefix
    return util_lib.system_call_return(cmd)