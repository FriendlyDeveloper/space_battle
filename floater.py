# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random, randrange


class Floater(Prey):
    radius = 5
    _color = 'red'
    width = 10
    height = 10
    
    def __init__(self,x,y):
        Prey.__init__(self, x, y, self.width , self.height, angle = None, speed = 5)
        self.randomize_angle()
#         self._color = 'red'
        self._image = PhotoImage(file='ufo.gif')
    
    def display(self, canvas): 
        
        canvas.create_image(*self.get_location(),image=self._image)
#        canvas.create_oval(self._x - Floater.radius, self._y - Floater.radius,
#                           self._x + Floater.radius, self._y + Floater.radius,
#                           fill = self._color)
       
    def update(self,model):
        delta_speed = .5
        delta_angle = .5
        
        change = randrange(1,10)
        if change <= 3:
            
# #         self.get_speed
#             if self.get_speed == 3:
#                 self.set_speed = 3.5
#                 
#             
#             elif self.get_speed == 7:
#                 self.set_speed = 6.5
            
#             else:
            new_speed = delta_speed + (random()-delta_angle)
            if new_speed < 3:
                self.set_speed (3)
            elif new_speed > 7:
                self.set_speed(7)
            else:
                self.set_speed(new_speed)
                
            self.set_angle(self.get_angle() + (random()-delta_angle))
            
        self.move()