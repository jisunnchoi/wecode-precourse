import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(3):
            print(threading.currentThread().getName())

send = Messenger(name = 'sending out messages')
receive = Messenger(name = 'receiving messages')

send.start()
receive.start()

#
import threading
import time

start = time.perf_counter()
finish = time.perf_counter()

def do_something():
    print(f'sleeping 1 sec(s)')
    time.sleep(1)
    print('done sleeping')

t1 = threading.Thread(target = do_something)
t2 = threading.Thread(target = do_something)
t1.start()
t2.start()

#join() : 실행중인 thread가 종료되기를 기다림
t1.join()
t2.join()


print(f'finished in {round(finish-start, 2)} sec')


##########
import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} sec(s)')
    time.sleep(seconds)
    print('done sleeping')

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args =[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'finished in {round(finish-start, 2)} sec')