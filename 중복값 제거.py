#Input 으로 주어진 리스트에서 오직 한번만 나타나는 값 (unique value)을 가지고 있는 요소는 출력해주세요.
my_list = [1, 2, 3, 4, 5, 1, 2, 3, 7, 9, 9, 7]
remove = []
for i in range(len(my_list)+1):
  for j in range(i+1, len(my_list)):
      if my_list[i] == my_list[j]:
          remove.append(my_list[j])

for i in my_list:
    if i not in remove:
        print(i)
