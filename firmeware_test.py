import inspect
import sys
import unittest
sys.path.append("./basic_io")
import slip_io
import net_io

def serial_upgrade():
    cmd = ""
    print cmd

def net_firmware_upgrade():
    cmd = "coap-client -m POST coap://[ff03::fc]:5683/vcSys/fwUpgrade \
-v 7 -b 512 -B 10 -a 2001:db8::2 -f \
/Daily_Build/Build_Image/Test/$(date +%Y%m%d)/node-vc7300BMTR/\
main/image_for_upgrade_vc7300BMTR_node.bin -N"
    print cmd

class test_upgrade(unittest.TestCase):
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
        print "Run: %s:%s" % (self.__class__.__name__, inspect.stack()[0][3])
        # setup env
        # start test
        net_firmware_upgrade()
        # de-init slip
        slip_io.stop_testing_env_slip(self)
        return True

    # define test unit
    def test_eth(self):
        print "Run: %s:%s" % (self.__class__.__name__, inspect.stack()[0][3])
        return True

    # define test unit
    def test_serial(self):
        print "Run: %s:%s" % (self.__class__.__name__, inspect.stack()[0][3])
        return True
