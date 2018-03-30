# I modified the mycosmicsne.py script a little bit so that it will run on python3 and also save the output under generated names.

import numpy as np
import matplotlib.pyplot as plt

cHo = 4.47*10**9

var = True
while var:
    universe = input('Choose an universe: Open (O), Flat (F), Closed (C)  =  ')
    if universe == 'O' or universe == 'o':
        print ('You Choose an Open Universe')
        curv = float(input('Choose the curvature radius as a function of the Hubble radius: '))
        var = False
        name = universe.capitalize()+'_r='+str(curv)
        cu = ', $R=$'+str(curv)
    elif universe == 'F' or universe == 'f':
        print ('You Choose a Flat Universe')
        curv = 0
        var = False
        name = universe.capitalize()
        cu = ''
    elif universe == 'C' or universe == 'c':
        print ('You Choose a Closed Universe')
        curv = float(input('Choose the curvature radius as a function of the Hubble radius: '))
        var = False
        name = universe.capitalize()+'_r='+str(curv)
        cu = ', $R=$'+str(curv)
    else:
        print("There's something wrong with your input. Try it again.")

alpha = float(input('Choose an expansion law a(t)=t**alpha  , alpha = '))
ct = cHo*curv
name = name+'_alpha='+str(alpha)

data = np.loadtxt('../data/supernovae.data')
zsn = data[:,0]
my = data[:,1]
me = data[:,2]

data = np.loadtxt('../data/grbs.data')
zgrb = data[:,0]
mygrb = data[:,1]
megrb = data[:,2]

z = np.arange(0.01, 6.51, 0.01)
if alpha !=1:
    if universe == 'F' or universe=='f':
        Dl=-cHo*(alpha)/(alpha-1.)*((1+z)-(1+z)**((2*alpha-1)/alpha))
        Dlsn=-cHo*(alpha)/(alpha-1.)*((1+zsn)-(1+zsn)**((2*alpha-1)/alpha))
    if universe == 'C' or universe=='c':
        Dl=ct*(1+z)*np.sin(-(alpha)/(alpha-1.)/curv*(1-(1+z)**((alpha-1)/alpha)))
        Dlsn=ct*(1+zsn)*np.sin(-(alpha)/(alpha-1.)/curv*(1-(1+zsn)**((alpha-1)/alpha)))
    if universe == 'O' or universe=='o':
        Dl=ct*(1+z)*np.sinh(-(alpha)/(alpha-1.)/curv*(1-(1+z)**((alpha-1)/alpha)))
        Dlsn=ct*(1+zsn)*np.sinh(-(alpha)/(alpha-1.)/curv*(1-(1+zsn)**((alpha-1)/alpha)))

if alpha ==1:
    if universe == 'F' or universe=='f':
        Dl=cHo*(1+z)*np.log(1+z)
        Dlsn=cHo*(1+zsn)*np.log(1+zsn)
    if universe == 'C' or universe=='c':
        Dl=ct*(1+z)*np.sin(np.log(1+z))
        Dlsn=ct*(1+zsn)*np.sin(np.log(1+zsn))
    if universe == 'O' or universe=='o':
        Dl=ct*(1+z)*np.sinh(np.log(1+z))
        Dlsn=ct*(1+zsn)*np.sinh(np.log(1+zsn))

plt.figure(figsize=(15, 10))
plt.suptitle('Supernova cosmology ('+universe.capitalize()+cu+', $\\alpha=$'+str(alpha)+')')

plt.subplot(221)
plt.errorbar(zsn,my,me,fmt='-o',color='b',label='supernova data', linewidth=0.8, markersize=2.5)
plt.title('SN Data')
plt.xlabel('Z')
plt.ylabel('DM')
mu=5*np.log10(Dl/10)
plt.plot(z,mu,color='g', linewidth=0.8)
plt.xlim(0,1.5)
plt.ylim(32,47)

plt.subplot(222)
plt.errorbar(zsn,my,me,fmt='-o',color='b', linewidth=0.8, markersize=2.5)
plt.errorbar(zgrb,mygrb,megrb,fmt='-o',color='r', linewidth=0.8, markersize=2.5)
plt.title('SN + GRBs Data')
plt.xlabel('Z')
plt.ylabel('DM')
mu=5*np.log10(Dl/10)
plt.plot(z,mu,color='g', linewidth=0.8)

musn=5*np.log10(Dlsn/10)

plt.subplot(212)
plt.errorbar(np.log10(zsn),my-musn,me,fmt='-o',color='b',label='residuals', linewidth=0.8, markersize=2.5)
plt.plot(np.log10(zsn),0*(np.log10(zsn)),color='r', linewidth=0.8)
plt.title('SN Data - Residuals')
plt.xlabel('Log10(Z)')
plt.ylabel('Delta DM')

plt.savefig('../plots/'+name+'.pdf')
print(name)
plt.show()

