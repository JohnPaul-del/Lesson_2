prognoz = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+10', 'градусов']
i = 0

for i in range(len(prognoz)):
    if prognoz[i].isdigit():
        if -10 < int(prognoz[i]) < 10:
            prognoz[i] = '"0{}"'.format(prognoz[i])
        else:
            prognoz[i] = '"{}"'.format(prognoz[i])
    if prognoz[i].count('+') or prognoz[i].count('-'):
        _bufstr = prognoz[i]
        if len(_bufstr) == 2:
            prognoz[i] = '"' + _bufstr[0] + "0" + _bufstr[1] + '"'
        else:
            prognoz[i] = '"{}"'.format(prognoz[i])

print(" ".join(prognoz))
