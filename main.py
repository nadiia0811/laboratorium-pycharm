a = int(input("podaj liczbe 1: "))
b = int(input("podaj liczbe 2: "))
print("Wejście", a,', ', b)
if a > b:
    (a,b)=(b,a)
while a <= b:
    if a % 2 == 1:
        a+=1
        continue
    print(a, end=' ')
    a += 1



