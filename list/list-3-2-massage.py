# 3-2. Сообщения: начните со списка, использованного в упражнении 3-1, но вместо вывода
# имени каждого человека выведите сообщение. Основной текст всех сообщений должен
# быть одинаковым, но каждое сообщение должно включать имя адресата.


names = ['sasha', 'dima', 'sergey', 'konstantin', 'andrew', 'viktor']

# конкатенация строк, плохой выбор для производительности, попробуем через
print('Hi, my name is ' + names[0].title() + ", and I am an Artem's friend.")
print()

#теперь запишем в переменную и выведем ее
var1 = 'Hi, my name is ' + names[1].title() + ", and I am an Artem's friend."
print(var1)
print()

#теперь отделим строку от функций
var2 = "Hi, my name is {}, and I am an Artem's friend."

#делаем первую букву Заглавной, и у нас не получаеться
var2.title()
#title() is a method on objects of type str, not a function in the string module.
#That means you can do "artem".title() or str.title("foo") but not string.title("foo").
#iter_var.title()

#выводим результат
print(var2.format(names[2]))
print()

#теперь циклом
for iter_var in names:
    #цикл автоматически разбил список(list) на элементы (и посчитал их количество)
    #по этому нам не нужно указывать список "names[0]", а просто "итерируемую" 
    #переменную iter_var(можно придумать любое имя переменной, обычно это "i" или
    #в нашем случае "name")
    print(var2.format(iter_var.title()))
    #iter_var.title() получилось применить, так как мы были внутри .format()