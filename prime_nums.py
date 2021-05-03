number = int(input("Write a number: "))
prime = []
for i in range(1, number+1):
    if (number % i) == 0:
        prime.append(i)
if len(prime) == 2:
    print(number, " is a prime number!")
else:
    print(number, " is not a prime number!")
