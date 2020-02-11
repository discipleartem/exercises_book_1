#3-1. Имена: сохраните имена нескольких своих друзей в списке с именем names. 
# Выведите имя каждого друга, обратившись к каждому элементу списка (по одному за раз).


names = ['sasha', 'dima', 'sergey', 'konstantin', 'andrew', 'viktor']

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

# IndexError: list index out of range
#print(names[6])



print()
print()
print('А теперь циклом:')
# а теперь циклом
for n in names:

    print(n.title())
