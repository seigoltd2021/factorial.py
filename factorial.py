num = int(input("Введите число: "))

factorial = 1

if num < 0:
    print("Факториал не может быть найден для отрицательных чисел")
elif num == 0:
    print("Факториал 0 равен 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("Факториал", num, "равен", factorial)
