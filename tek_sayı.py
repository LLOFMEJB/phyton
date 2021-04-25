numbers_list = [2,3,4,12,11,2,3,5,12,2]
numbers_tek = []
for i in range(len(numbers_list)):
  if (numbers_list[i] % 2) == 1:
    numbers_tek.append(numbers_list[i])
print(numbers_tek)