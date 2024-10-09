
#
# time = input('enter time: ').lower()
#
#
# if time == 'утро' or time == 'morning':
#     print('доброе утро')
# elif time == 'день'   or time == 'day':
#     print('добрый день')
# elif time == 'вечер'  or time == 'evening' :
#     print('добрый вечер')
# else:
#     print('Здраствуйте! время суток не известно')



# Операторы сравнения
# print(2 == 3)
# print(2 != 3)
# print(2 > 3)
# print(2 < 3)
# print(2 >=3)
# print(2 <=3)


# Логические операторы

# and or not
# print(2 > 3 or 2 < 3)
# print(2 > 3 and 2 < 3)
#

temperature = int(input('enter temperature: '))

if temperature >= -30 and temperature <= 0:
    print('cold')
elif temperature >= 1 and temperature <= 15:
    print('chilly')

elif temperature >= 16 and temperature <= 25:
    print('warm')

elif temperature >= 26 and temperature <= 40:
    print('hot')

else:
    print(f'несовместимая с жизнью температура - {temperature}')














