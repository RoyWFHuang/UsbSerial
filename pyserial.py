#!/usr/bin/python 
# coding=UTF-8 
import serial 
################################################### 
# 
# 功 能: 將接收到的資料已hex顯示 
# 參 數: 串列埠接受到的資料 
# 返 回: 轉換後的資料 
# 
################################################### 
def hexshow(data): 
    hex_data = '' 
    hLen = len(data) 

    for i in xrange(hLen): 
        hvol = ord(data[i]) 
        hhex = '%02x' % hvol 
        hex_data += hhex+' '

    print 'hexshow:', hex_data 
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

if __name__ == '__main__': 
    serial = serial.Serial('/dev/ttyS0', 115200) 
    print serial 

    if serial.isOpen(): 
        print("open success") 
    else: 
        print("open failed") 


    try: 
        while True: 
            count = serial.inWaiting() 
            if count > 0: 
                data = serial.read(count) 
                if data != b'': 
                    print("receive:", data) 
                    serial.write(data) 
                else: 
                    serial.write(hexsend(data)) 

    except KeyboardInterrupt: 
        if serial != None: 
            serial.close() 
