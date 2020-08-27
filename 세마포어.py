import time
import threading

class ResourcePool():
    def __init__(self):
        self.active_thread_list = []
        self.lock = threading.Lock()

    def use(self, name):
        with self.lock:
            self.active_thread_list.append(name)
            print('list of threads in resource pool : %s', self.active_thread_list)

    def unuse(self, name):
        with self.lock:
            self.active_thread_list.remove(name)
            print('list of threads in resource pool : %s', self.active_thread_list)

def worker(semaphore, pool):
    print('waiting to enter the pool')
    with semaphore:
        print('enter the pool')
        thread_name = threading.currentThread().getName()
        pool.use(thread_name)
        time.sleep(1)
        pool.unuse(thread_name)

def main():
    pool = ResourcePool()
    semaphore = threading.Semaphore(3)

    for i in range(5):
        t = threading.Thread(target=worker, name="thread-%s"%i, args=(semaphore,pool))
        t.start()

if __name__ == "__main__":
    main()