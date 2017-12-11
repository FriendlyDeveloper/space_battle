# Hunter is derived from Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    
    def __init__(self,x,y):
        self.vision = 200
        Pulsator.__init__(self, x,y)
        Mobile_Simulton.__init__(self, x, y, self._width, self._height, angle = 0, speed= 5)
        self.randomize_angle()
        self._color = 'brown'
        
    def update(self, model):    
        prey_in_canvas = [sim for sim in model.simultons if isinstance(sim, Prey)]
#         print(prey_in_canvas)
        
        try:
#             print([sim for sim in prey_in_canvas if self.in_range((sim._x, sim._y))])
            closest_prey = min([sim for sim in prey_in_canvas if self.in_range((sim._x, sim._y))])
#             print(closest_prey)
        
#             print(atan2(closest_prey._y, closest_prey._x))
            
            self.set_angle(atan2(closest_prey._y-self._y, closest_prey._x-self._x))
            Pulsator.update(self, model)
        
        except:
            print('fail')
            
            
        self.move()
#         return Pulsator.update(self, model)
    
    def in_range(self, xy):
        return self.distance(xy) <= 200

        
    
        
