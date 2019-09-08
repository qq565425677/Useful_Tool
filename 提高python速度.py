import time,functools
def time_cost(func):
    @functools.wraps(func)
    def cal(*args,**kw):
        start=time.time()
        func(*args,**kw)
        end=time.time()
        print('function %s consume %s seconds' % (func.__name__,str(end-start)))
    return cal
    
@time_cost
def test_func():
    sum=0
    for num in range(100000000):
        sum+=num
    print(sum)
    
test_func()
print('-----------------------')

from numba import jit

@time_cost
@jit
def test_numba():
    sum=0
    for i in range(100000000):
        sum+=i
    print(sum)
    
test_numba()
print('-----------------------')
input()