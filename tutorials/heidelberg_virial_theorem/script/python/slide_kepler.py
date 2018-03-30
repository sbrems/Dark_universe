import numpy as np
import pylab as plt
from matplotlib.widgets import Slider, Button
from scipy.integrate import odeint

def func(x, t, alpha):
    dxdt=np.empty(4)
    dxdt[0]=x[2]
    dxdt[1]=x[3]
    dxdt[2]=x[0]*x[3]**2-alpha/x[0]**(alpha+1)
    dxdt[3]=-2/x[0]*x[2]*x[3]
    return dxdt

alpha0=1
alpha=alpha0

x0=np.array([1, 0, 1, 0.8])
t=np.linspace(0, 500, 1000000)
sol=odeint(func, x0, t, args=(alpha, ))
x=sol[:,0]*np.cos(sol[:,1])
y=sol[:,0]*np.sin(sol[:,1])

def update(val):
    alpha = salpha.val
    sol=odeint(func, x0, t, args=(alpha, ))
    x=sol[:,0]*np.cos(sol[:,1])
    y=sol[:,0]*np.sin(sol[:,1])
    l.set_xdata(x)
    l.set_ydata(y)
    fig.canvas.draw()
def reset(event):
    salpha.reset()

fig, ax=plt.subplots(figsize=(15, 10))
plt.plot([0], [0], 'x', color='black', ms=3)
l,=plt.plot(x,y,color='b', linewidth=0.8)
plt.xlim(-10, 10)
plt.ylim(-5, 5)
plt.axis('off')

plt.subplots_adjust(left=0.25, bottom=0.25)

axalpha = plt.axes([0.25, 0.1, 0.65, 0.03])
salpha = Slider(axalpha, '$\\alpha$', 0.8, 1.2, valinit=alpha0)
salpha.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')
button.on_clicked(reset)

plt.show()
