ran_list = list(range(1,56))
fib_list = []
i = 0
while i < 56:
    fib_list.append(ran_list[i])
    i += i
print(fib_list)