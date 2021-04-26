number = input("Please write a number : ")
numlist = list(number)
i = 0
armstop = 0
while True:
  if (("-") in numlist):
    number = input(" It is an invalid entry. Don't use non-numeric, float, or negative values...: ")
    numlist = list(number)
    
  elif not (number.isdigit()):
    number = input(" It is an invalid entry. Don't use non-numeric, float, or negative values...: ")
    numlist = list(number)
    
  elif isinstance(number, float):
    number = input(" It is an invalid entry. Don't use non-numeric, float, or negative values...: ")
    numlist = list(number)

  else:
    break
while i < len(numlist):
  armstop += pow(int(numlist[i]),len(numlist))
  i += 1

if armstop == number:
  print(number, " is an Armstrong number!")

else:
  print(number, " is not an Armstrong number!")