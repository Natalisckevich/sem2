# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.

a = int(input('Введите число: '))

list = list(range(-a,a))
print(list)

numberOne=int(input('Введите позицию первого элемента: '))
numberTwo=int(input('Введите позицию второго элемента: '))
print(list[numberOne-1]*list[numberTwo-1])
