import time
import threading

def blocking_lock(lock):
    print('start blocking lock')

    while True:
        time.sleep(1)
        lock.acquire()
        try:
            print('(blockign) grab it')
            time.sleep(0.5)
        finally:
            print('(blocking) release')
            lock.release()

def nonblocking_lock(lock):
    print('start nonblocking lock')
    attempt, grab = 0, 0

    while grab < 3:
        time.sleep(1)
        print('(nonblocking) attempt')
        success = lock.acquire(False)

        try:
            attempt += 1
            if success:
                print("(nonblocking) grab it")
                grab += 1

        finally:
            if success:
                print('(nonblocking) release')
                lock.release()
    print(f'attempt: {attempt}, grab : {grab}')

def main():
    lock = threading.Lock()

    blocking = threading.Thread(target=blocking_lock, name='blocking',args = (lock,))
    blocking.setDaemon(True)
    blocking.start()

    nonblocking = threading.Thread(target=nonblocking_lock, name='nonblocking',args = (lock,))
    nonblocking.start()

if __name__ == "__main__":
    main()
