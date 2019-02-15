from werkzeug.local import LocalStack
from threading import Thread
import time

my_stack = LocalStack()
my_stack.push(2)
print('in main thread , value is : %s' % str(my_stack.top))

def worker():
    "新线程"
    print('in tong_thread , value is : %s' % str(my_stack.top))
    my_stack.push(1)
    print('in tong_thread , value is : %s' % str(my_stack.top))

new_t = Thread(target=worker, name='tong_thread')
new_t.start()
time.sleep(1)

# 主线程
print('执行到了主线程')
print('in main thread , value is : %s' % str(my_stack.top))
