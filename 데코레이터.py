def quick_fix(func):
    def result(car_speed, speed_standard):
        if func(car_speed, speed_standard):
            print(f'적발! 제한속도{car_speed-speed_standard}')
            return True
        else:
            return False
    return result

@quick_fix
def is_speeding(speed, standard):
    return speed > standard

print(is_speeding(150,110))
print(is_speeding(100,110))

is_speeding = quick_fix(is_speeding)

#파라미터가 있는 데코레이터
def add_warning(warning):
    def decorator(func):
        def decorated_func(age):
            if func(age) == True:
                return True
            else:
                print(warning)
                return False
        return decorated_func
    return decorator

@add_warning('안돼요')
def is_drinking_age(age):
    if age > 19:
        print('음주 가능')
        return True
    else:
        print('음주 불가')
        return False
is_drinking_age(17)
is_drinking_age(30)

#예제풀기
def name_decorator(name):
    def decorator(func):
        def decorated_func():
            return 'Hello,'+name.rjust(4)
        return decorated_func
    return decorator

@name_decorator("정우성")
def greeting():
    return 

print(greeting())
greeting = name_decorator(greeting)