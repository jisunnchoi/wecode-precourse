def is_paid_user(func):
    user_paid = True 
    def wrapper(*arges, **kwarges):
        if user_paid:
            func()
        else: 
            return 
    return wrapper

def is_paid_user(func):
    user_paid = True
    def decorated_func():
        if user_paid:
            return func()
        else:
            return 
    return decorated_func

@is_paid_user
def jackpot_stock_information():
    return '삼성을 사세요'
    

jackpot_stock_information()
print(jackpot_stock_information())

