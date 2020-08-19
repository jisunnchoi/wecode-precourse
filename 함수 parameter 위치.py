#에러 수정
def func_param_with_var_args(name, *args, age):
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)


func_param_with_var_args("정우성", "01012341234", "seoul", age = 20)

#에러 수정
def func_param_with_kwargs(name, age, address=0, **kwargs):
    print("name=",end=""), print(name)
    print("age=",end=""), print(age)
    print("kwargs=",end=""), print(kwargs)
    print("address=",end=""), print(address)


func_param_with_kwargs("정우성", "20", mobile="01012341234", address="seoul")

#에러  
def mixed_params(name="아이유", *args, age, **kwargs, address):
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)
    print("kwargs=",end=""), print(kwargs)
    print("address=",end=""), print(address)


mixed_params(20, "정우성", "01012341234", "male" ,mobile="01012341234", address="seoul")

#에러 수정 
def mixed_params(age, *args, name="아이유", address, **kwargs):
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)
    print("kwargs=",end=""), print(kwargs)
    print("address=",end=""), print(address)


mixed_params(20, "정우성", "01012341234", "male" ,mobile="01012341234", address="seoul")