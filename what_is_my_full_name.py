# what_is_my_full_name 함수는 주어진 parameter중 first_name 과 last_name 이라는 parameter를 조합하여 
# full name을 리턴해주어야 합니다.

# 예를 들어, first_name이 "우성" 이고 last_name 이 "정" 이면 "정 우성" 라고 리턴하면 됩니다. 
# Last name과 first name 사이에 space(빈칸)이 들어가 있어야 합니다.
# 만일 last_name이 없거나 first_name이 없으면 둘 중하나만 리턴하면 됩니다.
# 예를 들어, last_name이 없으면 "우성" 이라고 이름만 리턴하면 됩니다,
# 마지막으로, last_name과 first_name 둘다 없으면 "Nobody" 라고 리턴하면 됩니다. 

def what_is_my_full_name(**kwarges):
    keys = []
    for key in kwarges.keys():
      keys.append(key)
    print(keys)
    if 'first_name' in keys and 'last_name' in keys:
        return kwarges['last_name']+kwarges['first_name'].rjust(3)
    elif 'first_name' not in keys and 'last_name' not in keys:
        return 'Nobody'
    elif 'first_name' not in keys:
        return kwarges['last_name']
    elif 'last_name' not in keys:
        return kwarges['first_name']
    
print(what_is_my_full_name(first_name = '우성', last_name = '정'))
#if문 순서 생각해서 코드짜기
print(what_is_my_full_name(a=1, b=2))
