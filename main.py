# Complete project details at https://RandomNerdTutorials.com

from umqtt.simple import MQTTClient
print(gc.mem_free())

from lightEffects import LightEffects
import ujson
import time
import sys
import netconfig
import webrepl

gotmsg = False
saveraw = None
exception = None

def mqhandler(topic, msgraw):
  global gotmsg
  global saveraw
  global exception
  
  saveraw = msgraw
  
  gotmsg = True
  
  print(msgraw)
  msgs = ujson.loads(msgraw.decode('utf-8'))
  print(msgs)
  
  if type(msgs) is dict:
    msgs = [msgs]
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
    except KeyboardInterrupt:
      exception = 'keyboard'
      pass
    except:
      sys.print_exception()
      print('exception')
      pass
  
  print('next message')
  return msgs
  
mqtt = MQTTClient(netconfig.mqid, netconfig.mqhost, netconfig.mqport)
mqtt.set_callback(mqhandler)
mqtt.connect();
print(netconfig.iptopic)
print(sta.ifconfig()[0])
mqtt.publish("/" + netconfig.mqid + netconfig.iptopic,ujson.dumps({"id": netconfig.mqid, "ip":sta.ifconfig()[0]}),True) #retained message
mqtt.subscribe("/" + netconfig.mqid + netconfig.topic)

# strip control gpio
p = 2

try:
  f = open('saveraw.json','rb')
  saveraw = f.read()
  f.close()
except OSError:
  print('oserror reading')
  sys.print_exception()
  pass # no save file
  
le = LightEffects(neopin = 2, num = netconfig.ledcount)

webrepl.start()

#for i in range(100):
#  parms = {'count':10,'speedDelay':60}
#  le.twinkleRandom(**parms)

print('queue loop')
while True:
  gotmsg = False
  mqtt.check_msg()
  if not gotmsg and saveraw:
    print("reprocess:" + saveraw.decode('utf-8'))
    time.sleep_ms(100) #need time to break out of exception loop!!!!
    mqhandler("",saveraw)
    time.sleep_ms(100) #need time to break out of exception loop!!!!
  elif exception:
    print(exception)
    break
  elif saveraw != None:
    print('save pattern string')
    f = open('saveraw.json','wb')
    f.write(saveraw.decode('utf-8'))
    f.close()
    time.sleep_ms(100) #need time to break out of exception loop!!!!
  else:
    time.sleep_ms(100) #need time to break out of exception loop!!!!





