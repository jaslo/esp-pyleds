
# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import network
import netconfig

#uos.dupterm(None, 1) # disable REPL on UART(0)
print("starting")

sta = network.WLAN(network.STA_IF)
# sta = network.WLAN(mode=WLAN.STA)

sta.active(True)
sta.connect(netconfig.ssid, netconfig.password)

while sta.isconnected() == False:
 pass

print(sta.ifconfig())
#webrepl.start()

gc.collect()









