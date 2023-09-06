x = True
while x == True:
    print("Введите количество секунд или '0', если хотите выйти из программы")
    second = int(input())
    if second != 0:
        day = second // 86400
        second = second - day * 86400
        hour = second // 3600
        second = second - hour * 3600
        min = second // 60
        second = second - min * 60
        print("Дни: ",day, " Часы: ", hour, " Минуты: ", min, " Секунды: ", second )
    else:
        x = False


