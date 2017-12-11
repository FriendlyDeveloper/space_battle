# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


# from blackhole import Black_Hole
from blackhole_pic import Black_Hole
from prey import Prey
#added import

class Pulsator(Black_Hole):
#     count = 30
    def __init__(self, x, y):
        self.count = 30
#         self._x = x
#         self._y = y
#         self.radius = 1
        Black_Hole.__init__(self, x, y)
        
        
    def update(self,model):
        for sim in model.simultons:
            inside = model.find(self.contains)
            
            prey_inside = [sim for sim in inside if isinstance(sim, Prey)]

        if len(prey_inside) >= 1:
            self.change_dimension(1,1)
            #doesn't do much
            self.radius += 1
            
            print('increase')
            self.count = 30
        
        elif self.count > 0:
            self.count -= 1
    
        else:
            if self._height == 1:
                model.remove(self) 
            self.count = 30
            self.change_dimension(-1, -1)
            self.radius -= 1
            
        
        for sim in prey_inside:
            model.remove(sim)    
        
        return prey_inside 

    

        