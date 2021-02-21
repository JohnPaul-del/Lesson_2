price = [44.60, 78.76, 42, 12.67, 90.09, 54.34,
         16.70, 32.20, 50, 87.56, 60, 71.70, 81.25,
         22.12, 108.70, 55, 8.92, 35.06, 4.08, 1.90]

#Subtask1
print("*"*30, f"\n\nВывод цен с подписью:", sep="")
for i in range(len(price)):
    if type(price[i]) == float:
        rub= str(price[i]).split('.', -1)[0]
        kop = str(price[i]).split('.',-1)[-1]
        if len(kop) == 1:
            kop = "{}0".format(kop)
    else:
        rub = str(price[i])
        kop = "00"
    print(f"{rub} руб. {kop} коп./", end="")

#Subtask2
print(f"\n", "*"*30, f" \n\nСортировка списка без создания нового. Вывод ID списка: \n", id(price), sep="")
price.sort()
print(price)
print(id(price), f"\n", "*"*30, sep="")

#Subtask3
print(f" \nРеверс списка в новом:\n", sorted(price, reverse = True), f"\n", "*"*30, f"\n", sep="")

#Subtask4
price.sort()
print(f"Топ-5 самых высоких цен:\n", price[:14:-1], sep="")
