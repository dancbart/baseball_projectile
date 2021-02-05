# %% markdown
# ## Physics 3200 - Python.  Homework "Classes"
#
# Daniel Barton
#
# Construct a Class named projectile.
#
#
#     The class variables should include:
#
#     1. Height from which projectile is shot
#     2. The height at which it lands
#     3. Initial Velocity
#     4. Angle of that velocity with respect to horizontal
#
#     Next, The Class Methods should include:
#
#     A. Range of Projectile (Minimum distance to hit home run 99 m)
#     B. Maximum height
#     C. Final velocity
#
# %% codecell
import math
import numpy as np

class Projectile:
    def __init__(self,h0,v0,theta):
        self.h0 = h0
        self.v0 = v0
        self.theta = theta
        self.radians = self.theta/57.3 #convert degrees to radians
        self.v0x = v0*math.cos(self.radians)
        self.v0y = v0*math.sin(self.radians)
        self.a = 9.8 # meters/s**2
        self.t = 2*self.v0y/self.a #this gives the time in flight, depending on the initial velocity.
        self.x_final = self.v0x*self.t
        self.y_max = h0 + self.v0y*(self.t/2) - 0.5*self.a*(self.t/2)**2
        self.final_vel = math.sqrt(self.v0y**2 + 2*self.a*(self.y_max - h0))

    def range_value(self):
        print("Range ",round(self.x_final,2),"Meters")
        if (self.x_final > 99):
            print ("Congratulations, you hit a Home Run ball!")
        elif (self.x_final < 99 and self.theta >= 71.9):
            print ("Woops, fly ball...hit lower next time")
        elif (self.x_final < 99 and self.theta < 71.9):
            print ("Oooo, try hitting harder to get a Home Run")

    def initial_velocity(self):
        print("Initial x,y velocity ","(",(round(self.v0x,2)),",",round(self.v0y,2),")","m/s")

    def time_in_flight(self):
        print("Time in flight ",round(self.t,2),"Seconds")

    def height_value(self):
        print("Max height ",round(self.y_max,2),"Meters")

    def final_velocity(self):
        print("Final velocity ",round(self.final_vel,2),"m/s")

# Enter initial conditions in parentheses for hitting baseball:
# (bat height [meters], initial velocity [m/s], hit angle [degrees])
# Hits at an angle above 71.9 degrees are "fly ball", no home run.
r1 = Projectile(1.5,32,55)
r1.initial_velocity()
r1.time_in_flight()
r1.height_value()
r1.final_velocity()
r1.range_value()
# %% codecell
