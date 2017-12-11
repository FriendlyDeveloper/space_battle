import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole

from pulsator  import Pulsator
from hunter    import Hunter
# from special   import Special

# from prey      import Prey
from blackhole_pic import Black_Hole 
from special_fighter import Special
# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

simultons = []
running = False
cycle_count = 0
selected = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global simultons, running, cycle_count
    simultons = []
    running = False
    cycle_count = 0


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global running, cycle_count
    
    running = True
    cycle_count += 1
    update_all()
    display_all()
    running = False
    


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected 
    selected = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global simultons, selected
    if selected == 'Remove':
        for sim in simultons:
            if sim.contains((x,y)):
                remove(sim)
#         print('Remove')
    else:
        if selected == 'special':
            #I had to manually account for the special class and I added the special class to the project
            simultons.append(Special(x,y))
        else:    
            simultons.append(eval(selected)(x,y))


#add simulton s to the simulation
def add(s):
    global simultons
    simultons.append(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global simultons
    result = set()
    for sim in simultons:
        #i tailored this specifically to find all sims that contain a certain point
        if p((sim._x, sim._y)):
#         if p(sim)
            result.add(sim)

    return result

#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        
        for sim in simultons:

            sim.update(model)
#             sim.update(__)


#delete each simulton in the simulation from the canvas; then call display for each
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    global simultons
    for sim in controller.the_canvas.find_all():
        controller.the_canvas.delete(sim)
    
    for sim in simultons:
        sim.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simultons))+" simultons"+str(cycle_count)+" cycles")
