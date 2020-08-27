import time
import threading


def receiver(condition):
    print('start receiver')

    with condition:
        print('wait')
        condition.wait()
        time.sleep(1)
        print('end')


def sender(condition):
    print('start sender')

    with condition:
        print('send notify')
        condition.notifyAll()
        print('end')


def main():
    condition = threading.Condition()

    for i in range(5):
        t = threading.Thread(target=receiver, name= 'receiver %s'%i, args=(condition,))
        t.start()
    
    send = threading.Thread(target=sender, name='sender', args=(condition,))
    time.sleep(1)
    with condition:
        condition.notify(1)

    time.sleep(3)
    send.start()

if __name__ == "__main__":
    main()