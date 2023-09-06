n = int(input("Введите натуральное число n "))
x = True
while x == True:
    if n < 1:
        n = int(input("Ошибка! Введите натуральное число n "))
    else:
        x = False
mas = []
mas = n * [0]
pr = 1
for i in range(n):
    mas[i] = int(input("Введите элемент массива "))
for i in range(n):
    mas[i]= mas[i]**3
    pr = pr * mas[i]
print("Элементы массива в 3 степени:", mas)
print ("Сумма элементов массива равна ", sum(mas))
print ("Произведение элементов массива равно ",pr)
print ("Список элементов массива в обратном порядке ")
for i in range (n-1, -1, -1):
    print(mas[i])


