#input으로 주어진 list의 각 요소가 해당 list에 몇 번 나타나는지
#딕셔너리로 만들어서 리턴
def get_occurrence_count(my_list):
  my_dict = {}
  for i in range(len(my_list)):
      my_dict[my_list[i]] = my_list.count(my_list[i])
  return my_dict
