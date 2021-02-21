names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(names)):
    employee = names[i].split(' ', -1)[-1]
    print("Привет, ", employee.title(), sep="")
