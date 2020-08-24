lambdas = [
   lambda password : 'SHORT_PASSWORD' if (len(password) < 8) 
   else 'NO_CAPITAL_LETTER_PASSWORD' if not any(c.isupper() for c in password)
   else True
   ]


def check_password_using_lambda(password):
    
    for f in lambdas:
        if f(password) is not None:
            return f(password)

    return True


print( check_password_using_lambda('123') )            # SHORT_PASSWORD
print( check_password_using_lambda('12356789f') )      # NO_CAPITAL_LETTER_PASSWORD
print( check_password_using_lambda('123456789fF') )