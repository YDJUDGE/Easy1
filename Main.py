

"""Проект Поросячья латынь(в доработке)"""

Pig_Latin1 = input("Введите предложение на английском языке")
Consonants = set("bcdfghjklmnpqrtsvwxz")
Vowels = set("aeiuoy")

"""Создал множества значений"""

d = Pig_Latin1.split(" ")
new = []

"""Разбиваем строку и создаём массив"""

for i in d:
    if i[0] in Vowels:
        new.append(i)
    elif i[0] in Consonants:
        new.append(i[1:] + i[0] + "ay")

"""Цикл проверки и добавления в массив значений"""


print(" ".join(new))


