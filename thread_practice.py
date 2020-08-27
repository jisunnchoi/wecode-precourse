import threading
from threading import Thread, Condition, Lock
from queue import Queue
import time

#기본 예제
shared_number = 0

def thread_1(number):
    global shared_number
    print("number = ",end=""), print(number)
    
    for i in range(number):
        shared_number += 1

def thread_2(number):
    global shared_number
    print("number = ",end=""), print(number)
    for i in range(number):
        shared_number += 1

if __name__ == "__main__":

    threads = [ ]

    start_time = time.time()
    t1 = threading.Thread( target= thread_1, args=(50000000,) )
    t1.start()
    threads.append(t1)

    t2 = threading.Thread( target= thread_2, args=(50000000,) )
    t2.start()
    threads.append(t2)

    for t in threads:
        t.join()

    print("--- %s seconds ---" % (time.time() - start_time))

    print("shared_number=",end=""), print(shared_number)
    print("end of main")


#Lock 의 개념 
shared_number = 0

def thread_1(number,lock):
    global shared_number
    print("number = ",end=""), print(number)
    
    lock.acquire()
    for i in range(number):
        shared_number += 1
    lock.release()

def thread_2(number, lock):
    global shared_number
    print("number = ",end=""), print(number)
    lock.acquire()
    for i in range(number):
        shared_number += 1
    lock.release()

if __name__ == "__main__":

    threads = [ ]

    start_time = time.time()
    lock =Lock()
    t1 = threading.Thread( target= thread_1, args=(50000000,lock) )
    t1.start()
    threads.append(t1)

    t2 = threading.Thread( target= thread_2, args=(50000000,lock) )
    t2.start()
    threads.append(t2)

    for t in threads:
        t.join()

    print("--- %s seconds ---" % (time.time() - start_time))

    print("shared_number=",end=""), print(shared_number)
    print("end of main")


#condition 개념 
shared_number = 0

def consumer(number, cv, que):
    global shared_number
    print("number = ",end=""), print(number)
    
    cv.acquire()
    for i in range(number):
        shared_number += 1
    cv.wait()

def producer(number, cv, que):
    global shared_number
    print("number = ",end=""), print(number)
    cv.acquire()
    que.put(shared_number)
    for i in range(number):
        shared_number += 1
    cv.notify()
    cv.release()

if __name__ == "__main__":

    threads = [ ]
    que = Queue()
    cv = Condition()

    start_time = time.time()
    t1 = threading.Thread( target= consumer, args=(50000000,cv, que) )
    t1.start()
    threads.append(t1)

    t2 = threading.Thread( target= producer, args=(50000000,cv, que) )
    t2.start()
    threads.append(t2)
    for t in threads:
        t.join()

    print("--- %s seconds ---" % (time.time() - start_time))

    print("shared_number=",end=""), print(shared_number)
    print("end of main")

