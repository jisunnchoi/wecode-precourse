def generator_send():
    received_value = 0
    while True:
        received_value = yield
        print('received_value: ', received_value)
        yield received_value**2 

gen = generator_send()
print(gen)
next(gen)
print(gen.send(2))
next(gen)
print(gen.send(3))

#리스트 컴프리헨션과 제너레이터 
import time

def print_iter(iter):
    for element in iter:
        print(element)

def lazy_return(num):
    print("sleep 1s")
    time.sleep(1)
    return num

L = [ 1,2,3]
print("comprehension_list=")
comprehension_list = [ lazy_return(i) for i in L ]
print_iter(comprehension_list)

print("generator_exp=")
generator_exp = ( lazy_return(i) for i in L )
print_iter(generator_exp)