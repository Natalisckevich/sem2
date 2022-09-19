 # 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

num = int(input('Введите число: '))
result = 0
for i in range(1, num+1):
    result += (1+1/num)**num
print(round(result, 2))