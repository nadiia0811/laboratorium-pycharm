int1 = int(input('Enter number1'))
int2 = int(input('Enter number2'))
if int1 > int2:
    (int1, int2) = (int2, int1)
    while int1 < int2:
        print(int1)
        int1 += 1








