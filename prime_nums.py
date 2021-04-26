number = int(input("Write a number: "))
prime = []
for i in range(1, number):
    if (number % i) == 0:
        prime.append(i)
if len(prime) < 3:
    print(number, " is a prime number!")
else:
    print(number, " is not a prime number!")
    
#https://github.com/LLOFMEJB/phyton.git