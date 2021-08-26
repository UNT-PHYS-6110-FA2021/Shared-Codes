import matplotlib.pyplot as plt

#size of the 1D cell
box=10.

#initial configuration of particle A
position_a=0. # in m
velocity_a=1. # in m/s
mass_a=10 # in kg
trajectory_a=[]

#initial configuration of particle B
position_b=5. # in m
velocity_b=-2. # in m/s
mass_b=10 # in kg
trajectory_b=[]

t=0 #initial time, in seconds
dt=0.001 #in seconds
time=[]

nsteps=100000 
for i in range(nsteps):
    time.append(t)
    trajectory_a.append(position_a)
    trajectory_b.append(position_b)
    position_a=position_a+velocity_a*dt
    position_b=position_b+velocity_b*dt
#    if abs(position_b - position_a) < 1.e-3 :
#        velocity_holder=velocity_a
#        velocity_a=velocity_b
#        velocity_b=velocity_holder
    if (position_a>box) or (position_a<0):
        velocity_a=-velocity_a
    if (position_b>box) or (position_b<0):
        velocity_b=-velocity_b
    t+=dt

plt.plot(time,trajectory_a)
plt.plot(time,trajectory_b)
plt.show()