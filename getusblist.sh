#!/bin/bash

for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev); do
    (
        syspath="${sysdevpath%/dev}"
        devname="$(udevadm info -q name -p $syspath)"
        [[ "$devname" == "bus/"* ]] && continue
        eval "$(udevadm info -q property --export -p $syspath)"
#       [[ -z "$ID_SERIAL" ]] && continue
#        echo "/dev/$devname - $ID_SERIAL"
	[[ -z "$SUBSYSTEM" ]] && continue
	echo "/dev/$devname - $SUBSYSTEM"
    )
done

#
#DEVLINKS='aaaaa'
#DEVNAME='/dev/ttyUSB0'
#DEVPATH='/devices/pci0000:00/0000:00:14.0/usb1/1-3/1-3:1.0/ttyUSB0/tty/ttyUSB0'
#ID_BUS='usb'
#ID_MM_CANDIDATE='1'
#ID_MODEL='USB-Serial_Controller_D'
#ID_MODEL_ENC='USB-Serial\x20Controller\x20D'
#ID_MODEL_FROM_DATABASE='PL2303 Serial Port'
#ID_MODEL_ID='2303'
#ID_PATH='pci-0000:00:14.0-usb-0:3:1.0'
#ID_PATH_TAG='pci-0000_00_14_0-usb-0_3_1_0'
#ID_PCI_CLASS_FROM_DATABASE='Serial bus controller'
#ID_PCI_INTERFACE_FROM_DATABASE='XHCI'
#ID_PCI_SUBCLASS_FROM_DATABASE='USB controller'
#ID_REVISION='0400'
#ID_SERIAL='xxxxxx'
#ID_TYPE='generic'
#ID_USB_DRIVER='pl2303'
#ID_USB_INTERFACES=':ff0000:'
#ID_USB_INTERFACE_NUM='00'
#ID_VENDOR='xxxxx'
#ID_VENDOR_ENC='xxxxxxx'
#ID_VENDOR_FROM_DATABASE='xxxxx'
#ID_VENDOR_ID='xxxx'
#MAJOR='188'
#MINOR='0'
#SUBSYSTEM='tty'
#TAGS=':systemd:'
#USEC_INITIALIZED='10544451603'
