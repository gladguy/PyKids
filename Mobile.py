import usb.core
import usb.util
import sys
 
# find our device
dev = usb.core.find(idVendor=0x17EF, idProduct=0x7921)

# was it found?
if dev is None:
    raise ValueError('Device not found')


# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

cfg = dev.get_active_configuration()
intf = cfg[(0,0)]




print(intf)
ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('# Lets fuzz around!# Lets fuzz around!')

if usb.core.find(bDeviceClass=7) is None:
    print('No printer found')

# Let's fuzz around!
# Lets start by Reading 1 byte from the Device using different Requests
# bRequest is a byte so there are 255 different values
#usb.bmRequestType==0x82
msg = [0x04,0x03]
#ret = dev.ctrl_transfer(0x80, 6, 0x04, 0x0401, 34)

try:
    send = dev.ctrl_transfer(0x80,6,0x0000,0x00,0000) 
    #send = dev.ctrl_transfer(0x81,0,0x0000,0x00,0000) 
    #send = dev.ctrl_transfer(0x82,0,0x0000,0x00,0000) 
    print("Received: " + str(send))
except:
        pass
        print("There was an error")


for bReq in range(0,0):

    try:
        ret = dev.ctrl_transfer(0x80, bReq, 0, 0, 1)
    except:
        print(bReq)
        pass

print(hex(6))

#for bRequest in range(0,255):
 #   for cRequest in range(0,1):
  #      try:
            #ret = dev.ctrl_transfer(0x80, hex(cRequest), 100, 0, ffff)
            #ret = dev.ctrl_transfer(0x82, 0x6, 0, 0, 0)
            #ret = dev.ctrl_transfer(0x82, 0, 3, 2, 1000)
            #ret = dev.ctrl_transfer(bRequest, bRequest, bRequest, 10, 1)
            #ret = dev.ctrl_transfer(bRequest, 8, 20, 10, 1)
            #ret = dev.ctrl_transfer(0x83, 8, 1, 20, 10)
            #ret = dev.ctrl_transfer(0x83, 9, 1, 10, 10)
            #print(hex(cRequest) + " B Request -->" + hex(bRequest) + ret)
            #print (str(0x80) + "bRequest =" + str(bRequest))
            
        
   #     except:
            # failed to get data for this request
            #print ("Failed for " )
            #print (hex(cRequest))
    #        pass
