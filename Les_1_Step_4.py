number_str = input("Нахождение наибольшей цифры в числе. Введите число: ")
number_lengt = len(number_str)
coef = 10 ** (number_lengt-1)
i = number_lengt - 1
number = int(number_str)
max_number = number // coef
counter = 1
number_temp = number - coef * max_number
while i > 0:
    i -= 1
    coef = 10 ** i
    if max_number < number_temp // coef:
        max_number = number_temp // coef
        counter = number_lengt - i
    number_temp = number_temp - coef * (number_temp // coef)
print(f'Максимальной цифрой в {number} является '
      f'{max_number} на {counter}й позиции')