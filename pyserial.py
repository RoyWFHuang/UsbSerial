#!/usr/bin/python
# coding=UTF-8
import serial
import signal
import threading
import sys
from time import sleep
import subprocess
import time
###################################################
#
# 功 能: 將接收到的資料已hex顯示
# 參 數: 串列埠接受到的資料
# 返 回: 轉換後的資料
#
###################################################
exitflag = 0

def hexshow(data):
    hex_data = ''
    hLen = len(data)

    for i in xrange(hLen):
        hvol = ord(data[i])
        hhex = '%02x' % hvol
        hex_data += hhex+' '

    print 'hexshow:', hex_data

def read_data(serial):
    print "read data %d" % exitflag
    #try:
    alldata = ""
    while exitflag == 0:
        #data = serial.readline()
        count = serial.inWaiting()
        if count > 0:
            data = serial.read(count)
            if data == "\n":
                alldata += data
                print alldata,
                alldata = ""
            else:
                alldata += data
            #if data != b'':
            #print(data, end='')    #python3
            #print data,             #python2
                #serial.write(data)
            #else:
            #    serial.write(hexsend(data))

    #except KeyboardInterrupt:
    #    if serial != None:
    #        serial.close()

def write_data(serial):
    print 'write data'
    data = ""
    while exitflag == 0:
        data = raw_input()
        data += "\n"
        #time.sleep(3)
        #serial.write("g3test set_device_mode 0\n".encode())
        serial.write(data.encode())
###################################################
#
# 功 能: 將需要傳送的字串以hex形式傳送
# 參 數: 待發送的資料
# 返 回: 轉換後的資料
#
###################################################
def hexsend(string_data=''):
    hex_data = string_data.decode("hex")
    return hex_data

def sigint (signum, frame):
        print 'get exit'
        exitflag = 1
def sigterm (signum, frame):
    print "SIGTERM"

#class TestBasicIoSetting(unittest.TestCase):
#    def test_ping_msg(self):


if __name__ == '__main__':
    ##signal.signal(signal.SIGINT, sigint)
    #signal.signal(signal.SIGTERM, sigterm)
    answer = subprocess.check_output(['./getusblist.sh'])
    #print("the answer is {}".format(answer))
    serial_list = answer.split('\n')
    while("" in serial_list) :
        serial_list.remove("")
    print serial_list
    serial_io = []
    for x in serial_list:
        tmp = serial.Serial(x, 115200)
        serial_io.append(tmp)
    # /dev/ttyUSB0

    print serial_io

    thread_pool = []
    for x in serial_io:
        if x.isOpen():
            print("open success")
        else:
            print("open failed")
        read_thread = threading.Thread(target=read_data, args = (x,))
        write_thread = threading.Thread(target=write_data, args = (x,))
        read_thread.start()
        write_thread.start()
        thread_pool.append(read_thread)
        thread_pool.append(write_thread)
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print 'get exit'
        exitflag = 1

    for x in thread_pool:
        x.join()
    #print 'wait exit read'
    #read_thread.join()
    #print 'wait exit write'
    #write_thread.join()
    for x in serial_io:
        if x != None:
            x.close()



#import time

#print("---RUNOOB EXAMPLE ： Loading 效果---")

#print("Loading",end = "")
#for i in range(20):
#    print(".",end = '',flush = True)
#    time.sleep(0.5)