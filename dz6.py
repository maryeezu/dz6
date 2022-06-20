list = [15, 48, 'hello', 6, 19, 'world']
print(list)

for i in list:
    if type(i) is int:
        if i % 2 == 0:
            print('Сумма цифр четного числа', i, ':', i // 10 + i % 10)
        else:
            ind = list.index(i)
            list[ind] = list[1]
print(list)

n = 0
k = 0
s1 = list[2]
s2 = list[5]
s = s1 + s2

for x in s:
    if x in ['a', 'e', 'o', 'u', 'i']:
        n += 1
    else:
        k += 1

print('Количество гласных:', n)
print('Количество согласных:', k)