# 3-4. Список гостей: если бы вы могли пригласить кого угодно (из живых или умерших)
# на обед, то кого бы вы пригласили? Создайте список, включающий минимум трех людей,
# которых вам хотелось бы пригласить на обед. Затем используйте этот список для вывода
# пригласительного сообщения каждому участнику.

guests_list = ['Andrew&Marina', 'Viktor', 'Dima Ch.', 'Andrew&Larisa']

print('Приглашаю Вас {} разделить мою радость и принять участие в пире.'.format(guests_list[0]))
print()

#а теперь циклом
for guest in guests_list:
    print('Приглашаю Вас {} разделить мою радость и принять участие в пире.'.format(guest))