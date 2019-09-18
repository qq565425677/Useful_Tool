import random
import numpy as np
from numba import jit
import functools,time

import warnings
warnings.filterwarnings("ignore")

def time_cost(func):
    @functools.wraps(func)
    def cal(*args,**kw):
        start=time.time()
        func(*args,**kw)
        end=time.time()
        print('function %s consume %s seconds' % (func.__name__,str(end-start)))
    return cal

@jit
def qiongju():
    n = 1000
    r = 1.0
    a, b = (0.0, 0.0)
    x_neg, x_pos = a - r, a + r
    y_neg, y_pos = b - r, b + r
    count = 0
    X=np.linspace(x_neg,x_pos,n,True)
    Y=np.linspace(y_neg,y_pos,n,True)
    for x in X:
        for y in Y:
            if x*x + y*y <= 1.0:
                count += 1
    print ('穷举1*10e6个点产生的pi值：%f' % ((count / float(n**2)) * 4))
    
@jit
def mengtekaluo():
    n = 10000000
    r = 1.0
    a, b = (0.0, 0.0)
    x_neg, x_pos = a - r, a + r
    y_neg, y_pos = b - r, b + r
    count = 0
    for i in range(0, n):
        x = random.uniform(x_neg, x_pos)
        y = random.uniform(y_neg, y_pos)
        if x*x + y*y <= 1.0:
            count += 1
    print ('蒙特卡洛1*10e6个点产生的pi值：%f' % ((count / float(n)) * 4))
    
qiongju()
mengtekaluo()