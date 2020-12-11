# Complete project details at https://RandomNerdTutorials.com

from umqtt.simple import MQTTClient
print(gc.mem_free())

from lightEffects import LightEffects
import ujson
import time
import sys
import webrepl
import netconfig

mqdepth = 0

def mqhandler(topic, msgraw):
  global mqdepth
  mqdepth += 1
  print(msgraw)
  msgs = ujson.loads(msgraw.decode('utf-8'))
  print(msgs)
  
  if type(msgs) is dict:
    msgs = [msgs]
  while True:
    for m in msgs:
      msg = m.copy()
      methodName = msg.pop('method')
      print(methodName)
      method = getattr(le, methodName)
      repeatCount = 1 if 'repeat' not in msg else msg.pop('repeat')
      print(repeatCount)
      try:
        for i in range(repeatCount):
          method(**msg)
        print('returned OK')
      except:
        sys.print_exception()
        return
    mqtt.check_msg()

mqtt = MQTTClient(netconfig.mqid, netconfig.mqhost, netconfig.mqport)
mqtt.set_callback(mqhandler)
mqtt.connect();
print(netconfig.iptopic)
print(sta.ifconfig()[0])
mqtt.publish(netconfig.iptopic,sta.ifconfig()[0],True) #retained message
mqtt.subscribe(netconfig.topic)

# number of pixels
n = 14
# strip control gpio
p = 2

le = LightEffects(neopin = 2, num = netconfig.ledcount)

webrepl.start()

while True:
  mqtt.wait_msg()


