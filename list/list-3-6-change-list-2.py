# 3-6. Больше гостей: вы решили купить обеденный стол большего размера. Дополнительные
# места позволяют пригласить на обед еще трех гостей.
# • Начните с программы из упражнения 3-4 или 3-5. Добавьте в конец программы коман-
# ду print, которая выводит сообщение о расширении списка гостей.
# • Добавьте вызов insert() для добавления одного гостя в начало списка.
# • Добавьте вызов insert() для добавления одного гостя в середину списка.
# • Добавьте вызов append() для добавления одного гостя в конец списка.
# • Выведите новый набор сообщений с приглашениями – по одному для каждого участ-
# ника, входящего в список.

guests_list = ['Andrew&Marina', 'Viktor', 'Dima Ch.', 'Jabber']

for guest in guests_list:
    print('Приглашаю Вас {} разделить мою радость и принять участие в пире.'.format(guest))
print()
print('у нас появилось еще 3 места')
print()
guests_list.insert(0, 'Kolya S.')
guests_list.insert(3, 'Kirill')
guests_list.append('Konstantin')

print('Приглашаю Вас {} разделить мою радость и принять участие в пире.'.format(guests_list[0]))
print('Приглашаю Вас {} разделить мою радость и принять участие в пире.'.format(guests_list[1]))
print('Приглашаю Вас {} разделить мою радость и принять участие в пире.'.format(guests_list[2]))
print('Приглашаю Вас {} разделить мою радость и принять участие в пире.'.format(guests_list[3]))
print('Приглашаю Вас {} разделить мою радость и принять участие в пире.'.format(guests_list[4]))
print('Приглашаю Вас {} разделить мою радость и принять участие в пире.'.format(guests_list[5]))
print('Приглашаю Вас {} разделить мою радость и принять участие в пире.'.format(guests_list[6]))