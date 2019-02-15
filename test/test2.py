from werkzeug.local import Local
import threading
import time

class A(Local):
    pass

my = A()
my.a = 123

def workder():
    my.a = 456
    t = threading.current_thread()
    print(t.getName())
    print('new thread value is : ' + str(my.a))

new_t = threading.Thread(target=workder, name='tong_thread')
new_t.start()
time.sleep(1)
print('----------------------')
print('main thread value is : ' +  str(my.a))