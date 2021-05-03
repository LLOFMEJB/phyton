number = int(input("Write a number: "))
prime_list = []
for i in range(1, number+1):
    if (number % i) == 0:
        prime_list.append(i)
if len(prime_list) == 2:
    print(number, " is a prime number!")
else:
    print(number, " is not a prime number!")
