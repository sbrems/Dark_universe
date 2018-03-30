import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.widgets import RadioButtons

# Set up of the rotating function
def wirl(t, i):
    r=np.linspace(0.01, 100, 10000)
    if i==0:
       om=np.sqrt(1-np.arctan(r)/r)/r
    if i==1:
       om=10/r**2
    if i==2:
       om=1/r
    if i==3:
       om=100/r-1
    x0=-r*np.cos(om*t)
    y0=-r*np.sin(om*t)
    x=np.append(x0, -x0)
    y=np.append(y0, -y0)
    return x, y

# set initial values
i0=0
i=i0

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
line, = ax.plot([], [], '.', lw=0.8, ms=0.1, color='orange')
plt.axis('off')
ax.remove

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(t, i):
    ls=['$v\\sim\\sqrt{1-\\frac{1}{r}\\operatorname{arc}\\tan r}$', '$v\\sim\\frac{1}{r}$', '$v=\\mathrm{const.}$', '$v\\sim1-r$']
    i=ls.index(radio.value_selected)
    x, y = wirl(t, i)
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, fargs=(i, ), init_func=init, interval=20, blit=True)

# define click function
def click(label):
    ls=['$v\\sim\\sqrt{1-\\frac{1}{r}\\operatorname{arc}\\tan r}$', '$v\\sim\\frac{1}{r}$', '$v=\\mathrm{const.}$', '$v\\sim1-r$']
    i=ls.index(label)
    anim.frame_seq=anim.new_frame_seq()

rax = plt.axes([0.025, 0.025, 0.3, 0.3])
radio = RadioButtons(rax, ('$v\\sim\\sqrt{1-\\frac{1}{r}\\operatorname{arc}\\tan r}$', '$v\\sim\\frac{1}{r}$', '$v=\\mathrm{const.}$', '$v\\sim1-r$'), active=0)
radio.on_clicked(click)

plt.show()
