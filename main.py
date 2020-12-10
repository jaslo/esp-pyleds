# Complete project details at https://RandomNerdTutorials.com

from umqtt.simple import MQTTClient

from lightEffects import LightEffects
import ujson
import time
import sys

'''
message:
{ method: colorWipe,
  red: 0,
  green: 0,
  blue: 0,
  speedDelay: 30
}
'''

def mqhandler(topic, msgraw):
  msgs = ujson.loads(msgraw.decode('utf-8'))
  if type(msgs) is dict: msgs = [msgs]
  for msg in msgs:
    methodName = msg.pop('method')
    method = getattr(le, methodName)
    repeatCount = 1 if 'repeat' not in msg else msg.pop('repeat')
    try:
      for i in range(repeatCount):
        method(**msg)
        mqtt.check_msg()
      print('returned OK')
    except:
      print('exception: ', sys.exc_info()[0])      

mqtt = MQTTClient("upy-led1", "192.168.0.137", 1883)
mqtt.set_callback(mqhandler)
mqtt.connect();
mqtt.subscribe('/pyled1/pattern')
mqtt.publish('/pyled1/ipaddr', sta.ifconfig()[0], True)

# number of pixels
n = 14
# strip control gpio
p = 2

le = LightEffects(neopin = 2, num = 30)

while True:
  mqtt.wait_msg()


for i in range(5):
  le.cylonForwardBG(128,0,0,0,255,0,6,30)

time.sleep(5)

for i in range(5):
  le.cylonBackwardBG(0,0,255,64,64,64,6,30)
  
time.sleep(5)


le.rainbowCycle(1)
le.colorWipe(0,0,0,30)
# le.rainbowCycle(10)
# le.colorWipe(0,0,0,30)

'''
for i in range(40,0,-10):
  le.cylonBounce(255,0,0,6,i,30)

le.cylonBounceBG(255,0,0,0,255,0,6,30)
le.cylonBounceBG(255,0,0,0,255,0,6,30)
le.cylonBounceBG(0,255,0,255,0,0,6,30)
le.cylonBounceBG(0,255,0,255,0,0,6,30)

le.colorWipe(0,0,0, 30)

le.twinkleRandom(120,120, False)

#le.colorWipe(0,0,0, 30)
#le.twinkleRandom(120,300,True)

le.colorWipe(0,255,0, 30)
  
for i in range(120):
  le.sparkleBG(255,0, 0, 0, 64, 0, 120)

le.colorWipe(255,0,0, 30)

for i in range(120):
  le.sparkleBG(0, 255, 0, 48,0,0, 120)
'''

le.colorWipe(255,0,0,30)
le.colorWipe(0,255,0, 30)
le.colorWipe(96,96,96, 30)








