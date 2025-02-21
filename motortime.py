#!/usr/bin/env python3

import time, datetime, motor
class hourmin:
  def __init__(self): 
    self.hour = 0
    self.minu = 0

class motortime:
   def __init__(self):
     # reset to 00:00
     #motor.reset()
     self.current = hourmin()
     self.current.hour = 0;
     self.current.minu = 0;

   def hourminu(self):
     now = datetime.datetime.now()
     print(now.time())
     hour = now.strftime('%H')
     minu = now.strftime('%M')
     t = hourmin()
     t.hour = int(hour)
     t.minu = int(minu)
     return t

   def off(self):
     # Nothing for the moment...
     return

   def display(self, val):
     old = self.current.hour * 60
     old = old + self.current.minu
     new = val.hour * 60
     new = new + val.minu
     mysteps = motor.STEPS_PER_REVOLUTION
     mysteps = mysteps // 60
     if (new == old):
       return
     if (new>old):
       mysteps = (new - old) * mysteps
       if val.minu == 0:
         mysteps = mysteps + 2
       else:
         if val.minu % 2 == 0:
           mysteps = mysteps + 1
       print(mysteps)
       motor.step_forward8(0.005, mysteps)
     else:
       mysteps = (old - new) * mysteps
       if val.minu == 0:
         mysteps = mysteps + 2
       else:
         if val.minu % 2 == 0:
           mysteps = mysteps + 1
       motor.step_backward8(0.005, mysteps)
     self.current.hour = val.hour
     self.current.minu = val.minu

if __name__ == "__main__":

    myout = motortime()

    while True:
      val = myout.hourminu()
      myout.display(val)
      time.sleep(1)
    myout.off()
