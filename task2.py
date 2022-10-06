# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input("Введите число: "))
div = 2  # делитель
list = []
oldnum = num
while div <= num:
    if num % div == 0:
        list.append(div)
        num //= div
        div = 2
    else:
        div += 1
print(f"Простые множители числа {oldnum} = {list}")
