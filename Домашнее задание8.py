Mike = int(input())
Ivan = int(input())
capital = int(input())
a = Mike
b = Ivan
if a >= capital and b >= capital:
    print(2)
elif a >= capital and b < capital:
    print('Mike')
elif a < capital and b >= capital:
        print('Ivan')
elif (a + b) >= capital:
    print(1)
else:
    if (a + b) < capital:
        print(0)