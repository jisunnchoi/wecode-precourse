import threading 

def worker(count):
    print('name: %s, argument: %s'%(threading.currentThread().getName(),count))

def main():
    for i in range(5):
        #threading 모듈의 Thread 클래스에 처리할 함수(worker)를 넣고 초기화하기 (이름, 변수 설정 가능)
        t = threading.Thread(target=worker, name='thread%i'%i, args = (i,))
        t.start()

if __name__ == '__main__':
    main()

class Worker(threading.Thread):
    def __init__(self, args, name=''):
        threading.Thread.__init__(self)
        self.args = args
    
    def run(self):
        print('name: %s, argument: %s'%(threading.currentThread().getName(), self.args[0]))

def main():
    for i in range(5):
        t = Worker(name = 'thread%i'%i, args = (i,))
        t.start()

if __name__ == '__main__':
    main()