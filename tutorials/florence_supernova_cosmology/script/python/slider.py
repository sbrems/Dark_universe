import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

universe0='f'
alpha0=1.5
curv0=1

universe=universe0
alpha=alpha0
curv=curv0

def cosm(z, universe, alpha, curv=0):
    cHo = 4.47*10**9
    ct=cHo*curv
    if alpha !=1:
        if universe == 'F' or universe=='f':
            Dl=-cHo*(alpha)/(alpha-1.)*((1+z)-(1+z)**((2*alpha-1)/alpha))
        if universe == 'C' or universe=='c':
                Dl=ct*(1+z)*np.sin(-(alpha)/(alpha-1.)/curv*(1-(1+z)**((alpha-1)/alpha)))
        if universe == 'O' or universe=='o':
                Dl=ct*(1+z)*np.sinh(-(alpha)/(alpha-1.)/curv*(1-(1+z)**((alpha-1)/alpha)))
    if alpha ==1:
        if universe == 'F' or universe=='f':
            Dl=cHo*(1+z)*np.log(1+z)
        if universe == 'C' or universe=='c':
            Dl=ct*(1+z)*np.sin(np.log(1+z))
        if universe == 'O' or universe=='o':
            Dl=ct*(1+z)*np.sinh(np.log(1+z))
    return Dl
def update(val):
    universe=radio.value_selected[0]
    alpha = salpha.val
    curv = scurv.val
    l.set_ydata(5*np.log10(cosm(z, universe, alpha, curv)/10))
    l2.set_ydata(5*np.log10(cosm(z, universe, alpha, curv)/10))
    ln.set_ydata(my-5*np.log10(cosm(zsn, universe, alpha, curv)/10))
    lines[0].set_linewidth(0)
    fig.canvas.draw_idle()
def unidate(label):
    universe = label[0]
    alpha = salpha.val
    curv = scurv.val
    l.set_ydata(5*np.log10(cosm(z, universe, alpha, curv)/10))
    l2.set_ydata(5*np.log10(cosm(z, universe, alpha, curv)/10))
    ln.set_ydata(my-5*np.log10(cosm(zsn, universe, alpha, curv)/10))
    lines[0].set_linewidth(0)
    fig.canvas.draw_idle()
def reset(event):
    scurv.reset()
    salpha.reset()
    universe=universe0
    radio.set_active(1)

data = np.loadtxt('../data/supernovae.data')
zsn = data[:,0]
my = data[:,1]
me = data[:,2]

data = np.loadtxt('../data/grbs.data')
zgrb = data[:,0]
mygrb = data[:,1]
megrb = data[:,2]

z = np.arange(0.01, 6.51, 0.001)

fig, ax=plt.subplots(figsize=(15, 10))
plt.subplots_adjust(left=0.25, bottom=0.25)

axalpha = plt.axes([0.25, 0.1, 0.65, 0.03])
salpha = Slider(axalpha, '$\\alpha$', 0.1, 3.0, valinit=alpha0)
salpha.on_changed(update)

axcurv = plt.axes([0.25, 0.15, 0.65, 0.03])
scurv = Slider(axcurv, '$r_c$', 0.01, 1.0, valinit=curv0)
scurv.on_changed(update)

rax = plt.axes([0.025, 0.5, 0.15, 0.15])
radio = RadioButtons(rax, ('open', 'flat', 'closed'), active=1)
radio.on_clicked(unidate)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')
button.on_clicked(reset)


s = 5*np.log10(cosm(z, universe, alpha, curv)/10)

plt.subplot(221)
plt.errorbar(zsn,my,me,fmt='-o',color='b',label='supernova data', linewidth=0.8, markersize=2.5)
plt.title('SN Data')
plt.xlabel('Z')
plt.ylabel('DM')
l,=plt.plot(z,s,color='g', linewidth=0.8)
plt.xlim(0,1.5)
plt.ylim(32,47)

plt.subplot(222)
plt.errorbar(zsn,my,me,fmt='-o',color='b', linewidth=0.8, markersize=2.5)
plt.errorbar(zgrb,mygrb,megrb,fmt='-o',color='r', linewidth=0.8, markersize=2.5)
plt.title('SN + GRBs Data')
plt.xlabel('Z')
plt.ylabel('DM')
l2,=plt.plot(z,s,color='g', linewidth=0.8)

musn=5*np.log10(cosm(zsn, universe, alpha, curv)/10)

plt.subplot(212)
l3=plt.errorbar(np.log10(zsn),my-musn,me,fmt='-o',color='b',label='residuals', linewidth=0.8, markersize=2.5)
ln, lines=l3[0], l3[-1]
plt.plot(np.log10(zsn),0*(np.log10(zsn)),color='r', linewidth=0.8)
plt.title('SN Data - Residuals')
plt.xlabel('Log10(Z)')
plt.ylabel('Delta DM')

plt.show()
