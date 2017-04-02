# scrap_python
def log(func):
    def wrapper(*args, **kw):
        print("oks")
        #print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper()
   
#@log
def now():
    print('2013-12-25')    
#now()
log(now)
'''
def funa():
    def funb():
        print("a")
        return 3
    return funb()
a = funa()
'''
