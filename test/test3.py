import threading
import time


def worker():
    # 当前线程
    time.sleep(2)
    t = threading.current_thread()
    print(t.getName())

new_t = threading.Thread(target=worker, name='tong_thread')
new_t.start()

t = threading.current_thread()
print(t.getName())