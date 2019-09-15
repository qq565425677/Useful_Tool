import time,functools
def time_cost(func):
    @functools.wraps(func)
    def cal(*args,**kw):
        start=time.time()
        func(*args,**kw)
        end=time.time()
        print('function %s consume %s seconds' % (func.__name__,str(end-start)))
    return cal