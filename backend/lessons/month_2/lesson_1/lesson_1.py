


# class Car:
#     name = 'MERS'
#
#     def __init__(self, model,year):
#         self.model = model
#         self.year = year
#
#
#     # def sayname(self):
#     #     print(self.name)
#
#     def __str__(self):
#         return f'{self.model} {self.year}'
#
#
# mers =Car('bmw', 1999)
# mers2 = Car('lexus', 2010)
#
# # mers.sayname()
# # mers2.sayname()
# print(mers)
# print(mers2)



# class Dog:
#     name = None
#     age = None
#     color = None
#
# sharik = Dog()
# sharik.name = 'sharik'
# sharik.age = 2
# sharik.color = 'red'
#
#
# print(sharik.name, sharik.age)


# class Dog:
#
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age =age
#         self.color = color
#
#     def voice(self):
#         print(f'{self.name}: gaf gaf gaf')
#     def sit_down(self):
#         print(f'{self.name}: sitting')
#
#     def playing(self):
#         print(f'{self.name}: is being played')
#
# sharik = Dog('sharik', 2, 'red')
# sharik.voice()
# sharik.playing()
#
# bobik = Dog('bobik', 190, 'red')
# bobik.voice()

# print(sharik.name, sharik.age, sharik.color)


# print(f'name of dog {sharik.name}, ages of dog: {sharik.age},'
#       f' color {sharik.name}: {sharik.color}')


'''
    магические метды:
'''

# class Banknote:
#     def __init__(self, value = int):
#         self.value = value
#
#     def __repr__(self):
#         return f' Banknote {self.value}'
#
#     # def __str__(self):
#     #     return f' banknote in nominal {self.value} rubles'
#
# if __name__ == '__main__':
#     banknote = Banknote(45)
#     others = eval(repr(banknote))
#     print(others)


#
# class Word(str):
#
#     def __new__(cls, word):
#         if ' ' in word:
#             print('Value contains spaces. Truncating to first space.')
#             word = word[:word.index(' ')]
#         return str.__new__(cls, word)




import os
print(os.path.dirname(__file__))








