dict = {'Кольцо': ['золото', 350, 3], 'Серьги': ['серебро', 140, 7], 'Цепочка': ['золото', 225, 8 ], 'Браслет': ['серебро', 98, 5] }
print('Программа "Ювелирный магазин"')
x = True
while x==True:
    print("""         МЕНЮ 
    1. Просмотр описания: название – описание
    2. Просмотр цены: название – цена.
    3. Просмотр количества: название – количество.
    4. Всю информацию.
    5. Покупка
    6. До свидания""")
    answer = int (input("Выберите действие "))
    if answer == 1:
        name = input("Введите название предмета ")
        if name in dict:
            print(name, " ",dict[name][0])
        else:
            print("Такого элемента нет в списке!")
    elif answer == 2:
        name = input("Введите название предмета ")
        if name in dict:
            print(name, " ", dict[name][1], " руб.")
        else:
            print("Такого элемента нет в списке!")
    elif answer == 3:
        name = input("Введите название предмета ")
        if name in dict:
            print(name, " ", dict[name][2], " кол.")
        else:
            print("Такого элемента нет в списке!")
    elif answer == 4:
        print("Вся информация:")
        for name, info in dict.items():
            print("Название: ", name)
            print("Материал: ", dict[name][0])
            print("Стоимость: ", dict[name][1], " руб.")
            print("Количество: ", dict[name][2], " кол.")
            print("-------------------------------")
    elif answer == 5:
        name = input("Введите название предмета или 'n' для выхода ")
        if name =="n":
            continue
        elif name in dict:
            kol = int(input("Введите количество предметов "))
            if kol <= dict[name][2]:
                price = kol * dict[name][1]
                dict[name][2]-=kol
                print("Вы купили ", kol, " товара.", "Цена покупки равна ", price)
                print("Количество данного товара в магазине равно ", dict[name][2])
            else:
                print("В магазине недостаточно товара! ")
        else:
            print("Такого товара нет в магазине!")
    elif answer == 6:
        print("До свидания! ")
        x = False
        break
    else:
        print("Ошибка! Выберите действия ещё раз!")
