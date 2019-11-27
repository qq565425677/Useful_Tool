from math import pi,tan,pow

def f(x,Ga=0.687008764,Gb=0.9776258):
    return Ga*Gb/4*pow((pi/x),2)+((Ga+Gb)/2)*(1-pi/x/tan(pi/x))+2*tan(pi/2/x)/(pi/x)-1

def gexian(f,x0=0.6,x1=0.8,tol=10):
    xlist=[x0,x1]
    i=1
    while(abs(xlist[-1]-xlist[-2])>1/pow(10,tol)):
        xnm1,xn=xlist[i-1],xlist[i]
        xnp1=xn-(xn-xnm1)/(f(xn)-f(xnm1))*f(xn)
        xlist.append(xnp1)
        i+=1
    return xlist

def show(xlist,f):
    print('%6s%15s%22s'%('k','xk','f(xk)'))
    for i,v in enumerate(xlist):
        print('%6d%20.10f%20.10f'%(i,v,f(v)))

resultlist=gexian(f)
show(resultlist,f)