# "get_find" 함수를 작성하세요.
# 문자와 문자열이 주어졌을때, "get_find" 함수는 주어진 문자열에서 함께 주어진 문자가 나타나는 첫번째 위치를 반환합니다.
# Notes:
# 문자열의 첫번째 문자는 인덱스 값 0 을 가집니다.
# 만약 문자열에 해당 문자가 여러번 나타나면, 첫번째로 나타나는 위치를 반환해야 합니다.
# 만약 문자가 문자열에 존재하지 않는다면, -1 을 반환해야 합니다.
# find 함수를 사용하지 마세요.
# output = get_find('a', 'I am a hacker')
# print(output) # --> 2


def get_find(x, s):
    for i in range(len(s)):
        if s[i] == x:
            return i 
    return -1
          

print(get_find('a', 'I am a hacker'))
print(get_find('a','la'))           
print(get_find('c','abrakadabra'))


#주어진 리스트안에 있는 단어중 가장 긴 단어를 찾을수 있도록 함수를 완성해주세요.
def find_longest_word(s):
  return max(s, key=len)

print(find_longest_word(["PHP", "Exercises", "Backend"]))