# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).

# random number
# using random . random and then subtract something
#what happens under the hood of python
import math 
from prey import Prey

class Ball(Prey):
    radius = 5
    def __init__(self, x, y):
        self.height = 10
        self.width = 10
        self._color = 'blue'
        Prey.__init__(self, x, y, self.width , self.height, angle = None, speed = 5)
        self.randomize_angle()
        
    def display(self, canvas): 
       canvas.create_oval(self._x - Ball.radius, self._y - Ball.radius,
                          self._x + Ball.radius, self._y + Ball.radius,
                          fill = self._color)

    def update(self,model):
        self.move()