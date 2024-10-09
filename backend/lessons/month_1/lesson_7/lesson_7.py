
from random import choice


students_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,
                 18,19,20,21,22,23,24,25,26,27,28,29]

rates_journal = {}

while students_list:
    print('students count:', len(students_list))
    happy_student = choice(students_list)
    name = input(f'enter name student #{happy_student}: ').title()
    rate = int(input(f'enter rate for {name}:'))
    rates_journal[name] = rate
    students_list.remove(happy_student)

for name, rate in rates_journal.items():
    print(f'{name} -- {rate}')

print(
    f'students count: {len(rates_journal)}\n'
    f'average rate for group:'
    f'{sum(rates_journal.values() / len(rates_journal))}',
)





# try:
#     print(2 * 'la')
#
# except:
#     print('error')
# else:
#     print('ok')
# finally:
#     print('cheking done!')




# lambda_func = lambda n1, n2: n1 + n2
# print(lambda_func(1,2))



# def up_first_letter(word: str) -> str:
#     return word.title()
#
#
# def show_words(some_func, some_list):
#     for element in some_list:
#         print(some_func(element))
#
# cities = ['tokmok', 'bishkek', 'darhan', 'alay']
#
# show_words(lambda word: word.title(), cities)



# show_words(up_first_letter, cities)
# show_words(len, cities)

# cities = ['tokmok', 'bishkek', 'darhan', 'alay']
#
# print(cities)
#
#
# cities_map = list(map(lambda  word : word.upper(), cities))
# print(cities_map)





# filter_cities = list(filter(lambda word: len(word) < 7,cities))
# print(filter_cities)

# sorted_cities = sorted(cities, key=lambda  word: word[-1])
# print(sorted_cities)










# try:
#     print(2* 'py')
#
#
# except:
#     print('error found!')
#
#
# else:
#     print('ok')
#
#
# finally:
#     print('checking done')




# lamda_func = lambda n1, n2: n1+n2
# print(lamda_func(2,3))
#
#
# def def_func(n1, n2):
#     return n1 + n2
#
# print(def_func(2,3))





# def up_first_latter(word: str)-> str:
#     return word.title()
#
# def show_words(some_function, some_list):
#     for element in some_list:
#         print(some_function(element))
#
# cities = ['tokmok', 'bishkek', 'darhan', 'alay']
#
# show_words(up_first_latter, cities)
# show_words(len, cities)


# cities = ['tokmok', 'bishkek', 'darhan', 'alay']
# print(cities)
#
#
# cities_map = list(map(lambda word: word.title(),cities))
# print(cities_map)




# filter_cities = list(filter(lambda  word: len(word) < 5,cities))
# print(filter_cities)



# sorted_sities = sorted(cities, key=lambda word: word[-1])
# print(sorted_sities)



