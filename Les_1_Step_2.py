total_sec = int(input("Введите время в секундах: "))
hours = total_sec // 3600
if (hours // 10) < 1 :
    hours = '0' + str(hours)
minutes = (total_sec % 3600) // 60
if (minutes // 10) < 1 :
    minutes = '0' + str(minutes)
seconds = total_sec % 3600 % 60
if (seconds // 10) < 1 :
    seconds = '0' + str(seconds)
print(f"{total_sec} секунд равно {hours}ч:{minutes}м:{seconds}с")
