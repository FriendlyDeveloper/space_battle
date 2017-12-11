'''
Created on Dec 10, 2017

@author: wesle
'''
from prey import Prey
from random import randrange
from PIL.ImageTk import PhotoImage

class Special(Prey):
    _width = 10
    _height = 10
    _colors = ['red', 'blue', 'orange', 'yellow', 'black', 'pink', 'green']
#     _color2 = 'blue'
#     _color3 = 'pink'
    def __init__(self,x,y):
        self.radiuses = 4
        
        Prey.__init__(self, x, y, self._width, self._height, angle = None , speed= 10)
        self.randomize_angle()
#         self._image = PhotoImage(file='x-wing_fighter.gif')
        self._image = PhotoImage(file='tie-fighter.jpg')
        
    def display(self,canvas):
        
        canvas.create_image(*self.get_location(),image=self._image)
#         color1 = self._colors[randrange(len(self._colors))]
#         color2 = self._colors[randrange(len(self._colors))]
#         color3 = self._colors[randrange(len(self._colors))]
#         
#         canvas.create_oval(self._x - self.radiuses, self._y - self.radiuses,
#                           self._x + self.radiuses, self._y + self.radiuses,
#                           fill = color1)
#         canvas.create_oval(self._x - self.radiuses*2, self._y + self.radiuses*2,
#                           self._x, self._y,
#                           fill = color2)
#         canvas.create_oval(self._x , self._y ,
#                           self._x + self.radiuses*2, self._y + self.radiuses*2,
#                           fill = color3)
    
    def update(self,model):
        self.move()