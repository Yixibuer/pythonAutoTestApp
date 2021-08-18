import datetime
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)  #内置函数使新建的函数属性不变
        def wrapper(*args, **kw):
            print('%s %s() %s:' % (text, func.__name__, datetime.datetime.now()))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('执行方法')
def now(i):
    sum = i+1
    return sum

print(now(5))
print(now.__name__)