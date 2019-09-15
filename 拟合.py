import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family']=['SimHei']

x = np.arange(1990,1997,1)
y = np.array([70 ,122 ,144 ,152, 174, 196, 202])

z1 = np.polyfit(x,y,4)
p1 = np.poly1d(z1)
xn=np.linspace(1990,1996,100,True)
yvalue = p1(xn)

plt.plot(x,y,'*',label='原始数据')
plt.plot(xn,yvalue,label='拟合曲线')



plt.xlabel('x轴')
plt.ylabel('y轴')

plt.legend(loc = 4)

plt.title('多项式拟合')
plt.show()