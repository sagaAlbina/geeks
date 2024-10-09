
#
# number = 5
# number += 5
# number **= 2
# number //= 4
# number -= 15
# print(number)
#
#
# word = 'geeks'
# print('o' in word)
# print('s' not in word)
# print('e' in word)
# print('s' not in word)

#
# counter = 0
#
# while counter <= 50:
#     if counter == 40:
#         print('stop')
#         break
#     counter += 1
#     if counter % 2 == 0:
#         continue
#     print('GEEKS', counter)


#
# rounds = int(input('сколько кругов нужно?'))
#
# while rounds > 0:
#
#     time = input(f'enter time:({rounds}) ').lower()
#     if time in 'exit stop выход':
#         break
#     if time == 'утро' or time == 'morning':
#         print('доброе утро')
#     elif time == 'день'   or time == 'day':
#         print('добрый день')
#     elif time == 'вечер'  or time == 'evening' :
#         print('добрый вечер')
#     else:
#         print('Здраствуйте! время суток не известно')
#
#     rounds -= 1

#
# word = 'kyrgyzstan'
#
# for letter in word:
#     if letter == 's':
#         break
#     if letter in 'yrzsan' :
#         continue
#     print(letter)
#





# a = int(input('enter number: '))
#
#
# even = 0
# odd = 0
#
# while a > 0:
#     if a % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     a = a // 10
#
# print('even: %d, odd: %d' % (even, odd))
#
#
#




# number = 5
# number += 5
# number **= 2
# number //= 4
# number -= 15
# print(number)
#
#



#
#
# word = 'geeks'
# print('o' in word)
# print('e' in word)
# print('z' in word)
# print('s' in word)



#
#
# count = 0
#
# while count <= 50:
#     if count == 40:
#         print('stop')
#         break
#     count += 1
#     if count % 2 == 0:
#         continue
#     print('geeks',count)




# rounds = int(input('skolko raz ?'))

#
# while rounds > 0:
#     time = input(f'enter time: ({rounds})') .lower()
#     if time in 'exit stop':
#         break
#     if time == 'утро' or time == 'morning':
#         print('доброе утро')
#     elif time == 'день'   or time == 'day':
#         print('добрый день')
#     elif time == 'вечер'  or time == 'evening' :
#         print('добрый вечер')
#     else:
#         print('Здраствуйте! время суток не известно')
#
#     rounds -= 1


#
# word = 'KYRGYZSTAN'
#
# for letter in word:
#     if letter == 'S':
#         break
#     if letter in 'YRZSAN':
#         continue
#
#     print(letter)





# Операторы назначения :
#
# number = 5
# print(number)
# number = number + 5
# print(number)
# #
# number = 5
#
# number += 5
# number = number + 5
#
# number **= 2
# number = number ** 2
#
# number //= 4
# number = number // 4
#
# number -= 15
# number = number - 15
# print(number)


# Операторы принадлежности
#
# word = 'geeks'
#
# print('o' in word)
# print('g' in word)
# print('z' not in word)
# print('s' not in word)
#




# циклы

#
# counter = 0
# while True:
#     print('geeks',counter)
#     counter += 1

#
# count = 0
# while count <= 50:
#     if count == 30:
#         print('exit')
#         break
#     count += 1
#     if count % 2 == 0:
#         continue
#     print('albina', count)
#
# rounds = int(input('сколько кругов нужно? '))
#
# while rounds > 0 :
#     time = input(f'enter time: ({rounds}) ').lower()
#     if time in 'exit stop':
#         break
#     if time == 'утро' or time == 'morning':
#         print('доброе утро')
#     elif time == 'день'   or time == 'day':
#         print('добрый день')
#     elif time == 'вечер'  or time == 'evening' :
#         print('добрый вечер')
#     else:
#         print('Здраствуйте! время суток не известно')
#     rounds -= 1


""" for """

# i - item , iterable, index

#
# word = 'KYRGYZSTAN'
#
# for letter in word:
#     if letter == 'S':
#         break
#     if letter in 'YRZSAN':
#         continue
#     print(letter)


# задание














# n = int(input())
#
# suma = 0
# mult = 1
#
# while n > 0 :
#     digit = n % 10
#     suma = suma + digit
#     mult = mult * digit
#     n = n // 10
#
# print('Сумма:',suma)
# print('Произедение:', mult)
#
















# p = int(input('Покозатель степени:  '))
# n = int(input('Предел: '))
#
#
# i = 1
#
# while i ** p <= n:
#     print(i ** p,end='')
#     i += 1
#
# print('\nПоследнее число , возведенное в степень:',i - 1)
#
#
#







# from unicodedata import digit
#
# n1 = int(input('Введите цело число: '))
# n2 = 0
#
# while n1 > 0 :
#     # находим остаток - последнюю цифру
#     digit = n1 % 10
#
#     # делим нацело - удаляем последнюю цифру
#     n1 = n1 // 10
#
#     # увеличеваем разрядность второго числа
#     n2 = n2 * 10
#
#     # добавляем очередную цель
#     n2 = n2 + digit
#
# print('"Обратное " ему число:', n2)















# from random import randint
#
# secret_number = randint(1,100)
# print('Отгадай число от 1 до 100')
#
# user_number = 0
# try_count = 0
#
# while user_number != secret_number:
#     try_count += 1
#     user_number = int(input(f'{try_count}- я попытка: '))
#     if user_number > secret_number:
#         print('много')
#     elif user_number < secret_number:
#         print('мало')
#     else:
#         print(f'Правильно. Я загадал {secret_number}')










