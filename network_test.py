import inspect
import sys
import unittest
import subprocess
sys.path.append("./basic_io")
import slip_io
import net_io
sys.path.append("./util")
import util_lib

_g_ping_packet_number = 2

def cmd_ping(net_if = "", ip_addr = ""):
    cmd = "ping -I " + net_if + " " + ip_addr + \
" -c " + str(_g_ping_packet_number)
    return util_lib.system_call_return(cmd)

def ipv6_cmd_ping(net_if = "", ip_addr = ""):
    cmd = "ping6 -I " + net_if + " " + ip_addr + \
" -c " + str(_g_ping_packet_number)
    return util_lib.system_call_return(cmd)


class test_net_cmd_ping(unittest.TestCase):
    slip_list = []
    # test class pre-init function
    def setUp(self):
        success, self.slip_list = slip_io.create_testing_env_slip(self)
        self.assertTrue(success);

    # test class termination function
    def tearDown(self):
        slip_io.stop_testing_env_slip(self)

    # define test unit
    def test_slip(self):
        # setup env
        # start test
        success = net_io.setup_ipv4_ip(self.slip_list[0], "127.0.0.2", "24")
        self.assertTrue(success)
        success = cmd_ping(self.slip_list[0], "127.0.0.2");
        self.assertTrue(success)
        # de-setp env
        return True

    # define test unit
    def test_eth(self):
        print "Run: %s:%s" % (self.__class__.__name__, inspect.stack()[0][3])
        # setup env
        # start test
        success = cmd_ping("lo", "127.0.0.1");
        self.assertTrue(success)
        # de-setp env
        return True