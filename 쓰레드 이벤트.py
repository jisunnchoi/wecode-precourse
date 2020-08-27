import time
import threading

def first_wait(e1, e2):
    while not e1.isSet():
        event = e1.wait(1)
        print('event status: ', event)

        if event:
            print('e1 is set')
            time.sleep(3)
            print('set e2')
            e2.set()

def second_wait(e2):
     while not e2.isSet():
        event = e2.wait(1)
        print('event status: ', event)

        if event:
            print('set e2')

def main():
    e1 = threading.Event()
    e2 = threading.Event()

    t1 = threading.Thread(name='first', target=first_wait, args=(e1,e2))
    t1.start()

    t2 = threading.Thread(name='second', target=second_wait,args=(e2,))
    t2.start()

    print('wait')
    time.sleep(5)
    print('set e1')
    e1.set()
    time.sleep(5)
    print('exit')

if __name__ == "__main__":
    main()