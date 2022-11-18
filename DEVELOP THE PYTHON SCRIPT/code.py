import ibmiotf.application
import ibmiot.device
import time
import random
import sys
# ibm watson device credentials
organization="rj0Qwb"
deviceType="RivwatQulity"
deviceid="RivwatQulatiy"
authmethod="token"
authtoken="uft_pb+dha3k)0_pa7"
def mycommandcallback(cmd):
  print("command received: %s" % cmd.date['command'])
  status=cmd.data['command']
  if status == "motorON"
  print("motor in on")
  else:
  print("motor is off")
 #generate random values for pH and turbidity
 def myCommandCallback(cmd):
 print ("command received: " cmd.data['command'])
 print (cmd)
try:
deviceOptions-{"org": organization, "type": deviceType, "id"; deviceid, "auth-method": authMethod, "authtoken":authToken} 
deviceCli=ibmiotf.device.Client(deviceOptions)
except Exception as e:
print ("caught exception connecting device is" str(e)) s
sys.exit()
#connect and sending data of ph Values and Turbidity
deviceCli.connect()
while True:
time.sleep(2)
Ph-random.randint (0,14) 
Turb-random.randint (0,10)
data=('Ph':Ph, "Turb':Turb) 
print(data)
det myon PublishCallback():
print("pl Value of Water is 4Ph) print ("Turb Value of Waters Turb)
success-deviceCli.publishkvent ("IoSensor","json", data, gos-0,on publish-ayon PublishCallBack)
i pot success:
print ("Not connected to loTF") time.sleep(1)
deviceCli.commandCallback-myCommandCallback
#disconnect the device from the cloud
deviceC11.connect()
