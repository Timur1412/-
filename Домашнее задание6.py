a = int(input())

if a == 0:
    print('Zero number')
else:
    if (a < 0) and (a % 2):
        print('Negative odd number')
    else:
        if (a < 0) and (a / 2):
            print('Negative even number')
        else:
            if (a > 0) and (a % 2):
                print('The number is not even')
            else:
                 if (a > 0) and (a > 2):
                     print('Possitive even number ')

