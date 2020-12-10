
import machine, neopixel
import time
from random1 import randrange

def delay(ms):
  time.sleep_ms(ms)


class LightEffects:
  
  def __init__(self, neopin, num):
    self.pin = neopin
    self.num = num
    self.np = neopixel.NeoPixel(machine.Pin(neopin), num)
    self.setAll(0,0,0)

  def showStrip(self):
    self.np.write()
  
  def setPixel(self, i, r, g, b):
    self.np[i] = (r, g, b)
    
  def setAll(self, r, g, b):
    for i in range(self.num):
      self.np[i] = (r, g, b)

  def RGBLoop(self):

    def setRGB(self, i, k):
      if i == 0: self.setAll(k, 0, 0); return
      elif i == 1: self.setAll(0, k, 0); return
      elif i == 2: self.setAll(0, 0, k); return
        
    for j in range(0, 3): # r, g, b
      # fade in
      for k in range(0, 256):
        self.setRGB(j, k)
        self.showStrip() 
        delay(3)
      # fade out
      for k in range(255, 0, -1):
        self.setRGB(j, k)
        self.showStrip()
        delay(3)
      
  def FadeInOut(self, red, green, blue):
    for k in range (0, 256):
      f = k/256.0
      self.setAll(f * red, f * green, f * blue)
    self.showStrip()
    
    for k in range (255, 0, -1):
      f = k/256.0
      self.setAll(f * red, f * green, f * blue)
    self.showStrip()
  
  def cylonBounce(self, red, green, blue, eyeSize, speedDelay, returnDelay):
    self.cylonBounceBG(red, green, blue, 0, 0, 0, eyeSize, speedDelay)
    delay(returnDelay)
    
  def cylonBounceBG(self, red, green, blue, bgred, bggreen, bgblue, eyeSize, speedDelay):
    col = [red,green,blue]
    col10 = [red//10, green//10, blue//10]
    for i in range(0, self.num-eyeSize-1):
      self.setAll(bgred,bggreen,bgblue)
      self.setPixel(i, *col10)
      for j in range(1,eyeSize):
        self.setPixel(i+j, *col)
      self.setPixel(i+eyeSize+1, *col10)
      self.showStrip()
      delay(speedDelay)
    
    # delay(returnDelay)
    
    for i in range(self.num-eyeSize-2, 0, -1):
      self.setAll(bgred,bggreen,bgblue)
      self.setPixel(i, *col10)
      for j in range(1, eyeSize):
        self.setPixel(i+j, *col)
      self.setPixel(i+eyeSize+1, *col10)
      self.showStrip()
      delay(speedDelay)

  def cylonForwardBG(self, red, green, blue, bgred, bggreen, bgblue, eyeSize, speedDelay):
    col = [red,green,blue]
    col10 = [red//10, green//10, blue//10]
    for i in range(0, self.num):
      self.setAll(bgred,bggreen,bgblue)
      self.setPixel(i, *col10)
      for j in range(1,eyeSize):
        self.setPixel((i+j) % self.num, *col)
      self.setPixel((i+eyeSize+1) % self.num, *col10)
      self.showStrip()
      delay(speedDelay)
    # better to cycle through the eyesize and clear to bg  
    #self.setAll(bgred,bggreen,bgblue)
    
  def cylonBackwardBG(self, red, green, blue, bgred, bggreen, bgblue, eyeSize, speedDelay):
    col = [red,green,blue]
    col10 = [red//10, green//10, blue//10]
    for i in range(self.num-1, -1, -1):
      self.setAll(bgred,bggreen,bgblue)
      self.setPixel(i, *col10)
      for j in range(1, eyeSize):
        self.setPixel((i+j) % self.num, *col)
      self.setPixel((i+eyeSize+1) % self.num, *col10)
      self.showStrip()
      delay(speedDelay)

    # better to cycle through the eyesize and clear to bg  
    self.setAll(bgred,bggreen,bgblue)
      
  def newKITT(self, red, green, blue, eyeSize, speedDelay, returnDelay):
    self.rightToLeft(red, green, blue, eyeSize, speedDelay, returnDelay)
    self.leftToRight(red, green, blue, eyeSize, speedDelay, returnDelay)
    self.outsideToCenter(red, green, blue, eyeSize, speedDelay, returnDelay)
    self.centerToOutside(red, green, blue, eyeSize, speedDelay, returnDelay)
    self.leftToRight(red, green, blue, eyeSize, speedDelay, returnDelay)
    self.rightToLeft(red, green, blue, eyeSize, speedDelay, returnDelay)
    self.outsideToCenter(red, green, blue, eyeSize, speedDelay, returnDelay)
    self.centerToOutside(red, green, blue, eyeSize, speedDelay, returnDelay)
    
  def centerToOutside(self, red, green, blue, eyeSize, speedDelay, returnDelay):
    for i in range((self.num-eyeSize)/2, 0, -1):
      self.setAll(0,0,0)
      self.setPixel(i, red/10, green/10, blue/10)
      for j in range(1,eyeSize):
        self.setPixel(i+j, red, green, blue)
      self.setPixel(i+eyeSize+1, red/10, green/10, blue/10)
      self.setPixel(self.num-i, red/10, green/10, blue/10)
      for j in range(1, eyeSize):
        self.setPixel(self.num-i-j, red, green, blue)
      self.setPixel(self.num-i-eyeSize-1, red/10, green/10, blue/10)
      self.showStrip()
      delay(speedDelay)
    delay(returnDelay)
    
  def outsideToCenter(self, red, green, blue, eyeSize, speedDelay, returnDelay):
    for i in range((self.num-eyeSize)/2):
      self.setAll(0,0,0)
      self.setPixel(i, red/10, green/10, blue/10)
      for j in range(1,eyeSize+1):
        self.setPixel(i+j, red, green, blue)
      self.setPixel(i+eyeSize+1, red/10, green/10, blue/10)
      self.setPixel(self.num-i, red/10, green/10, blue/10)
      for j in range(1, eyeSize+1):
        self.setPixel(self.num-i-j, red, green, blue)
      self.setPixel(self.num-i-eyeSize-1, red/10, green/10, blue/10)
      self.showStrip()
      delay(speedDelay)
    delay(returnDelay)

  def leftToRight(self, red, green, blue, eyeSize, speedDelay, returnDelay):
    for i in range(self.num-eyeSize-2):
      self.setAll(0,0,0)
      self.setPixel(i, red/10, green/10, blue/10)
      for j in range(1,eyeSize+1):
        self.setPixel(i+j, red, green, blue)
      self.setPixel(i+eyeSize+1, red/10, green/10, blue/10)
      self.showStrip()
      delay(speedDelay)
    delay(returnDelay)
    
  def rightToLeft(self, red, green, blue, eyeSize, speedDelay, returnDelay):
    for i in range(self.num-eyeSize-2, 0, -1):
      self.setAll(0,0,0)
      self.setPixel(i, red/10, green/10, blue/10)
      for j in range(1,eyeSize+1):
        self.setPixel(i+j, red, green, blue)
      self.setPixel(i+eyeSize+1, red/10, green/10, blue/10)
      self.showStrip()
      delay(speedDelay)
    delay(returnDelay)
    
    
  def twinkle(self, red, green, blue, count, speedDelay, onlyOne):
    self.setAll(0,0,0)
    for i in range(count):
      self.setPixel(randrange(self.num), red, green, blue)
      self.showStrip()
      delay(speedDelay)
      if onlyOne:
        self.setAll(0,0,0)
      
    
  def twinkleRandom(self, count, speedDelay, onlyOne):
    self.setAll(0,0,0)
    for i in range(count):
      b = randrange(256)
      g = 0 if b == 255 else randrange(256-b)
      r = 0 if g == 255 else randrange(256-g)
      self.setPixel(randrange(self.num), r, g, b);
      self.showStrip()
      delay(speedDelay)
      if onlyOne:
        self.setAll(0,0,0)
  
  def sparkle(self, red, green, blue, speedDelay):
    pixel = randrange(self.num)
    self.setPixel(pixel, red, green, blue)
    self.showStrip()
    delay(speedDelay)
    self.setPixel(pixel, 0, 0, 0)
    
  
  def sparkleBG(self, red, green, blue, bgred, bggreen, bgblue, speedDelay):
    pixel = randrange(self.num)
    self.setPixel(pixel, red, green, blue)
    self.showStrip()
    delay(speedDelay)
    self.setPixel(pixel, bgred, bggreen, bgblue)

  def snowSparkle(self, red, green, blue, sparkleDelay, speedDelay):
    self.setAll(red, green, blue)
    pixel = randrange(self.num)
    self.setPixel(pixel, 0xff, 0xff, 0xff);
    self.showStrip()
    delay(sparkleDelay)
    self.setPixel(pixel, red, green, blue)
    self.showStrip()
    delay(speedDelay)
    
#  def runningLights(self, red, green, blue, waveDelay):
#    position = 0
#    for i in range(self.num*2):
#      position++
#      for j in range(self.num):
#        level = Math.sin(
  
     
  def colorWipe(self, red, green, blue, speedDelay):
    for i in range(0, self.num):
      self.setPixel(i, red, green, blue)
      self.showStrip()
      delay(speedDelay)
  
  def wheel(self, wheelPos):
    c = [0, 0, 0]
    if wheelPos < 85:
      c[0] = wheelPos * 3
      c[1] = 255 - wheelPos * 3
      c[2] = 0
    elif wheelPos < 170:
      wheelPos -= 85
      c[0] = 255 - wheelPos * 3
      c[1] = 0
      c[2] = wheelPos * 3
    else:
      wheelPos -= 170
      c[0] = 0
      c[1] = wheelPos * 3
      c[2] = 255 - wheelPos * 3
    
    return c
  
  def rainbowCycle(self, speedDelay):
    for j in range(256): # 1 cycles of all colors
      for i in range(self.num):
        c = self.wheel(int(((i * 256 / self.num) + j) % 255))
        self.setPixel(i, *c)
      self.showStrip()
      delay(speedDelay)
    
  
  def theaterChase(self, red, green, blue, speedDelay):
    for j in range(0,10):
      for q in range(0,3):
        for i in range(0, self.num):
          self.setPixel(i+q, red, green, blue)
        self.showStrip()
        delay(speedDelay)
        
        for i in range(0, self.num, 3):
          self.setPixel(i+q, 0, 0, 0)
        
  def theatreChaseRainbow(self, speedDelay):
    for j in range(0,256):
      for q in range(0,3):
        for i in range(0, self.num,3):
          c = self.wheel((i+j) % 255)
          self.setPixel(i+q, **c)
        self.showStrip()
        delay(speedDelay)
        for i in range(0, self.num,3):
          self.setPixel(i+q, 0, 0, 0)
            







