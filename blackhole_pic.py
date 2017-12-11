# Black_Hole is derived from Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
from PIL.ImageTk import PhotoImage



class Black_Hole(Simulton):
    _width = 60
    _height = 60
#     radius = 10
    
    def __init__(self, x, y):
        self.radius = 40
        self._x = x
        self._y = y
        Simulton.__init__(self, x, y, self._width, self._height)
        self._color = 'black'
        
        
    def display(self, canvas):
        self._image = PhotoImage(file='blackhole.gif')
        canvas.create_image(*self.get_location(),image=self._image)
        
#         canvas.create_oval(self._x - self.radius, self._y - self.radius,
#                             self._x + self.radius, self._y + self.radius,
#                             fill = self._color)
#         
    def update(self, model):
        
        for sim in model.simultons:
            inside = model.find(self.contains)
            
            prey_inside = [sim for sim in inside if isinstance(sim, Prey)]

        for sim in prey_inside:
            model.remove(sim) 
            
        return prey_inside
        #not to sure how to get it to return whats inside
    
    def contains(self, xy):
        return self.distance(xy) <= self.radius
    
    
    
            
        