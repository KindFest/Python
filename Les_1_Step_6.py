distance = int(input("Введите дистанцию за 1й день: "))
goal = int(input("Введите цель: "))
i = 1
while True:
    if distance > goal :
        print("{0}-й день: {1:.2f}".format(i, distance))
        print(f"Ответ: на {i}-й день спортсмен достиг цели — не менее {goal} км. ")
        break
    else:
        print("{0}-й день: {1:.2f}".format(i, distance))
        i += 1
        distance *= 1.1
