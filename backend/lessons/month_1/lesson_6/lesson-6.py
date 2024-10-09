
list1 =[0,1,2,3,4,5,6,7,8,9,10,11,12,13]

def get_min_max(lst):
    max = lst[0]
    min = lst[0]
    for v in lst:
        if v > max:
            max = v
        if v < min:
            min = v
    return (min,max)
result = get_min_max(list1)
print(f'max meaning: {result[0]}', f'min meaning {result[1]}')







#  Схема функции
#  Определение наименования(параметры):
#     тело функци
#     возвращение обьекта
#
# вызов функции
# наименования(аргументы)



# def get_data(name, surname=None):
#     print(f'name: {name} surname: {surname} ')
#
# get_data('asel', 'ubadulbekova')
# get_data(surname='li', name='kiril')
# get_data('alina')


# letters_count = len('geeks')
# print(letters_count +1)
#
# def len1(iterable):
#     counter = 0
#     for i in iterable:
#         counter += 1
#     return counter
#
# letters_count = len1('geeks')
# print(letters_count + 1)





# def get_square(lenth, width):
#     square = lenth * width
#     return square

# square = get_square(32,15)
# square3 = get_square(8,4)
# print(square)
# print(square3)
















# rating_film = {
#     'The Holiday:': {
#         'Alina': 7,
#         'lena': 8
#     },
#     'Clash of the Titans:':{
#         'Kesha': 10
#
#     }
# }
# for key, value in rating_film.items():
#     print(key,value)
#
#
# def add_movie(**kwargs):
#     add_films = input('enter film: ').title()
#     if add_films not in rating_film:
#         rating_film[add_films] = add_films
#     else:
#         print('this movie already exist!')
#         return add_films
# add_movie('add_films')



# print(monday)
# def get_data(name,surmame='none'):
#     print(f'name: {name}, surname: {surmame}')
#
# get_data('alina')

# letters_count = len('geeks')
# print(letters_count + 1)
#
# def len1(itarable):
#     count = 0
#     for i in itarable:
#         count += 1
#     return count
#
# letters_count = len1('geek')
# print(letters_count + 1)


# def get_square(lenth, width):
#     square = lenth * width
#     return square
# square = get_square(23,45)
# square3 = get_square(2,9)
# print(square)
# print(square3)



# def get_square(lenth,width):
#     '''' dok string'''
#     square = lenth + width
#     return square

#
# def plus(*args):
#     return sum(args)
# print(plus(23,45,45,33,23))

# def menu (**kwargs):
#      return kwargs
# monday = menu(eat='burger', drink='tea')







# def add_film(name, rating = 0):
#     add_movies = input('add movies: ').title()
#     if add_movies not in rating_film:
#         rating_film[add_movies]
#         print('Movis added successfully')
#     if add_movies in rating_film:
#         print('this movie already exist !!!')
#         evaluators_name = add_film(name)
#         movie_score = add_film(rating)
#         return add_movies
#     print(f'enter your name: {name}, rating for this movie: {rating}')


















# expenses = 0
# days = 7
#
# for day in range(1, days+1):
#     expenses += int(input(f'day: {day} enter expence: '))
# print(expenses)
# print(expenses/ days)



# def get_data(name, surname = 'dont have'):
#     print(f'name: {name}, surname: {surname}')
#
# get_data('asdfer')


# letters_count = len('geeks')
# print(letters_count)
#
# def len1(iterable):
#     count = 0
#     for i in iterable:
#         count += 1
#     return count
#
# letters_count = len1('geek')
# print(letters_count)





# def get_square(lenth, width):
#     square = lenth*width
#     return square
# square = get_square(23,12)
# square3 = get_square(34,18)
#
# print(square)
# print(square3)

#
# letters_count = len('fack')
# print(len(.))











# def fun1():
#     return True
# result = fun1()
# print(result)

















# def shift(lst,steps):
#     if steps < 0:
#         steps = abs(steps)
#         for i in range(steps):
#             lst.append(lst.pop(0))
#
#     else:
#         for i in range(steps):
#             lst.insert(0,lst.pop())
#
# nums = [4,5,6,7,8,9,0]
# print(nums)
#
# shift(nums, -2)
# print(nums)
#
#
# shift(nums,3)
# print(nums)









# def get_data(name, surname='неизвемтно'):
#
#     # print(f'name: {name} surname: {surname}')
#     return f'name: {name} surname: {surname}'
#
# get_data('Albina', 'Saga')
# get_data(surname='Leonova', name="yana")
# get_data('kjuy')
#
# result = get_data('Albina')
# print(result)

# letters_count = len('geeks')
# print(letters_count)
#
# def len1(iterable):
#     counter = 0
#     for i in iterable:
#         counter += 1
#     return counter
#
# letters_count = len1('geeks')
# print(letters_count)



#
# lenth = 25
# width = 10
# square = lenth * width
# print(square)
#
# lenth1 = 3
# width2 = 4
# square1 = lenth1 * width2
# print(square1)


#
# def get_squale(length: int, width: int) -> int:
#     ''''Принимаетт ширину и длину ,и возврощает площадь'''
#     square = length * width
#     return square
#
# # print(get_squale.__doc__)
# print(help((get_squale)))



# square = get_squale(24,10)
# square1 = get_squale(8, 4)
#
# print(square)
# print(square1)


#
# def pluse(a,b):
#     return a + b
# print(pluse(4, 8))

# def pluse(*args):
#     return sum(args)
# print(pluse(2,3,5,66,86,))
# print(pluse(4, 8))

# def menu(**kwargs):
#     return kwargs
#
# monday = menu(eat='burger', drink='tea')
# print(monday)


# from pprint  import pprint
# expence = 0
# days = 7
# data = {}
# for day in range(1, days+1):
#     input_expense = int(input(f'day {day} enter expenses: '))
#     expence += input_expense
#     data[day] = input_expense
#
# print(expence)
# print(expence / days)
# pprint(data)











# def say_hallo(username, age):
#     print(f'hello {username}!')
#     print(f'your age is {age}')
#     print('-' * 20)
#
# # say_hallo('Valeriya',20)
# # say_hallo('Vasya', 30)
# # say_hallo('Litvin', 40)
#
# def numbers_sum(num1 = 1, num2 = 2):
#     print(num1 + num2)
#
# numbers_sum(num1=2, num2=7)
# numbers_sum(num1=13, num2=5)
# numbers_sum(num1=78, num2=349)


