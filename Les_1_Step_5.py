revenue = int(input("Введите размер выручки компании: "))
costs = int(input("Введите сумму издержек компании: "))
if revenue - costs > 0:
    print(f"Компания получила прибыль {revenue - costs}")
    print("Рентабельность выручки составила {:.2f}".format(revenue / costs))
    employees = int(input("Введите количество сотрудников компании: "))
    print("Выручка на одного сотрудника составила: {:.2f}".format(revenue / employees))
else:
    print(f"Компания получила убыток {revenue - costs}")
