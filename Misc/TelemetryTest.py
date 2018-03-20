import math

class calc:
    
    m_currentX = 0;
    m_currentY = 0;
    def __init__(self):
        return 
        
    def calcXY(self, pos, angle):
        m_currentDistance = pos
        m_distanceTraveled = m_currentDistance    
        self.m_currentX = self.m_currentX +  m_distanceTraveled * math.cos(math.radians(angle))
        self.m_currentY =  self.m_currentY + m_distanceTraveled * math.sin(math.radians(angle))
        print(self.m_currentX, self.m_currentY)



def yaw(angle):
    print(((450 - angle) % 360))
    
def yaw_test():
    x = -180
    while x != 181:
      print(x,((90 - x) % 360), ((450 - x) % 360)) 
      x += 1
       
# taco = calc()
#
# taco.calcXY(50, 45)
# taco.calcXY(50, 90)