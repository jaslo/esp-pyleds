
import machine, neopixel
import time
import urandom

def delay(ms):
  time.sleep_ms(ms)
  
def randint(max):
    min = 0
    span = max - min
    div = 0x3fffffff // span
    offset = urandom.getrandbits(30) // div
    val = min + offset
    return val
    
class LightEffects:
  
  def __init__(self, neopin, num):
    self.pin = neopin
    self.num = num
    self.np = neopixel.NeoPixel(machine.Pin(neopin), num)
    self.setAll(0,0,0)
    self.showStrip()

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
      
  def twinkle(self, red, green, blue, count, speedDelay, onlyOne = False):
    print('in twinkle')
    self.setAll(0,0,0)
    for i in range(count):
      self.setPixel(randint(self.num), red, green, blue)
      self.showStrip()
      delay(speedDelay)
      if onlyOne:
        self.setAll(0,0,0)
  
  def twinkleRandom1(self, count, speedDelay):
    self.setAll(0,0,0)
    for i in range(count):
      b = randint(512)  # 0-255 on, 256-511 off
      if b > 255:
        r = g = b = 0
      else:
        g = 0 if b == 255 else randint(256-b)
        r = 0 if g == 255 else randint(256-g)
      self.setPixel(randint(self.num), r, g, b);
      self.showStrip()
      delay(speedDelay)
    
  def twinkleRandom(self, count, speedDelay, onlyOne = False):
    self.setAll(0,0,0)
    for i in range(count):
      b = randint(256)
      g = 0 if b == 255 else randint(256-b)
      r = 0 if g == 255 else randint(256-g)
      self.setPixel(randint(self.num), r, g, b);
      self.showStrip()
      delay(speedDelay)
      if onlyOne:
        self.setAll(0,0,0)
  
  def sparkle(self, red, green, blue, speedDelay):
    pixel = randint(self.num)
    self.setPixel(pixel, red, green, blue)
    self.showStrip()
    delay(speedDelay)
    self.setPixel(pixel, 0, 0, 0)
    
  
  def sparkleBG(self, red, green, blue, bgred, bggreen, bgblue, speedDelay):
    pixel = randint(self.num)
    self.setPixel(pixel, red, green, blue)
    self.showStrip()
    delay(speedDelay)
    self.setPixel(pixel, bgred, bggreen, bgblue)

  def sparkleBGCount(self, red, green, blue, bgred, bggreen, bgblue, count, speedDelay):
    pixels = []
    for i in range(count):
      pixel = randint(self.num)
      self.setPixel(pixel, red, green, blue)
      pixels.append(pixel)
      
    self.showStrip()
    delay(speedDelay)
    for i in range(count):
      self.setPixel(pixels[i], bgred, bggreen, bgblue)

  def snowSparkle(self, red, green, blue, sparkleDelay, speedDelay):
    self.setAll(red, green, blue)
    pixel = randint(self.num)
    self.setPixel(pixel, 0xff, 0xff, 0xff);
    self.showStrip()
    delay(sparkleDelay)
    self.setPixel(pixel, red, green, blue)
    self.showStrip()
    delay(speedDelay)
    
  def colorWipe(self, red, green, blue, speedDelay):
    for i in range(0, self.num):
      self.setPixel(i, red, green, blue)
      self.showStrip()
      delay(speedDelay)
  
  def randomWipe(self, speedDelay):
    for i in range(0, self.num):
      b = randint(256)
      g = 0 if b == 255 else randint(256-b)
      r = 0 if g == 255 else randint(256-g)
      self.setPixel(i, r, g, b)
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
    print('in theaterChase')
    for j in range(10):
      for q in range(3):
        for i in range(0, self.num, 3):
          self.setPixel((i+q) % self.num, red, green, blue)
        self.showStrip()
        delay(speedDelay)
        
        for i in range(0, self.num, 3):
          self.setPixel((i+q) % self.num, 0, 0, 0)
  
  def theaterChaseBG(self, red, green, blue, bgred, bgblue, bggreen, speedDelay):
    print('in theaterChase')
    for j in range(10):
      for q in range(3):
        for i in range(0, self.num, 3):
          self.setPixel((i+q) % self.num, red, green, blue)
        self.showStrip()
        delay(speedDelay)
        
        for i in range(0, self.num, 3):
          self.setPixel((i+q) % self.num, bgred, bgblue, bggreen)
          
  def theaterChaseRainbow(self, speedDelay):
    for j in range(256):
      for q in range(0,3):
        for i in range(0, self.num,3):
          c = self.wheel((i+j) % 255)
          self.setPixel((i+q) % self.num, *c)
        self.showStrip()
        delay(speedDelay)
        for i in range(0, self.num,3):
          self.setPixel((i+q) % self.num, 0, 0, 0)
            












