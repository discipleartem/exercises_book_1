# УПРАЖНЕНИЯ
# 3-8 . Повидать мир: вспомните хотя бы пять стран, в которых вам хотелось бы побывать .
# • Сохраните названия стран в списке . Проследите за тем, чтобы список не хранился
# в алфавитном порядке .
# • Выведите список в исходном порядке . Не беспокойтесь об оформлении списка, просто
# выведите его как обычный список Python .

# • Используйте функцию sorted() для вывода списка в алфавитном порядке без изменения списка .
# • Снова выведите список, чтобы показать, что он по-прежнему хранится в исходном
# порядке .

# • Используйте функцию sorted() для вывода списка в обратном алфавитном порядке
# без изменения порядка исходного списка .
# • Снова выведите список, чтобы показать, что исходный порядок не изменился .


# • Измените порядок элементов вызовом reverse() . Выведите список, чтобы показать,
# что элементы следуют в другом порядке .


# • Измените порядок элементов повторным вызовом reverse() . Выведите список, чтобы
# показать, что список вернулся к исходному порядку .


# • Отсортируйте список в алфавитном порядке вызовом sort() . Выведите список, чтобы
# показать, что элементы следуют в другом порядке .

# • Вызовите sort() для перестановки элементов списка в обратном алфавитном порядке .
# Выведите список, чтобы показать, что порядок элементов изменился .




countries = ['Japane', 'USA', 'China', 'Switzerland', 'Russia']

# #вывод списка
# print(countries)
# print()

# #сортировка списка по алфавиту
# print(sorted(countries))
# print()

# print(countries)
# print()

# #вывод списка в обратном порядке
# print(sorted(countries, reverse=True))
# print()

# print(countries)
# print()

# #вывод списка в обратном порядке с изменением исходного списка
# countries.reverse()
# print(countries)
# print()

# #возврат к исходному состоянию с изменением исходного списка
# countries.reverse()
# print(countries)
# print()

#сортировка в алфавитном порядке с изменением исходного списка
countries.sort()
print(countries)
print()

#сортировка в обратном алфавитном порядке с изменением исходного списка
countries.sort(reverse=True)
print(countries)
print()