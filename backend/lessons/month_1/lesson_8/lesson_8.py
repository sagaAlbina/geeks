

#
# file = open('new_file.txt', 'w')
# file.write('text in english')
# file.close()


# with open('new_file.txt', 'w') as new_file:
#     new_file.write('\nsecond line')
#
# with open('other.txt', 'x') as file:
#     file.write('new file')



# file = open('new_file.txt', 'w')
# file.write('text on check')
# file.close()

#
# with open('new_file.txt', 'w') as new_file:
#     new_file.write('second line\n')


# with open('other.txt', 'x') as file:
#     file.write('new file')


# with open('other.txt', 'r') as file:
    # for i in file.read():
    #     print(i, end='')
    #  print(file.readlines())
    # print(file.read()[12])




#
# try:
#     with open('text.txt', 'r', encoding='utf-8')as file:
#         print(file.read())
# except FileNotFoundError:
#     print('file not found')



# try:
#     x = 5 / 1
#     x = int(input('enter: '))
# except ZeroDivisionError:
#     print('zeroo')
# except ValueError:
#     print('not good')
# finally:
#     print('of course no!')



# x = 0
# while x == 0:
#     try:
#         x = int(input('enter int: '))
#         x += 5
#         print(x)
#     except ValueError:
#         print('enter better!')


#
# try:
#     x = int(input('enter int: '))
#     x += 5
#     print(x)
# except ValueError:
#     print('enter int better!')



# file = open('data/text.txt', 'r')
#
# # print(file.read())
# for line in file:
#     print(line, end='')
#
# file.close()


# data = input('enter text: ')
#
#
# file = open('data/text.txt', 'a')
#
# file.write(data + '\n')
#
#
# file.close()



# file = open('new_file.txt', 'w')
# file.write('text on eng')
# file.close()

# with open('new_file.txt', 'a') as new_file:
#     new_file.write('\nsecond line')
#
# with open('new_file.txt', 'w') as file:
#     file.write('new file')

# with open('other.txt', 'x') as file:
#     file.write('new file')



# n = []
# m = []
# lst = []
# def posneg(lst):
#     lst = input('add numbers: ').split()
#     for i in lst:
#         if int(i)<0:
#             n.append(i)
#         else:
#             m.append(i)
#     print(m,n)
#
# posneg(lst)









# animals = ['cat', 'dog', 'cow']
# qty = [10, 15, 3]
#
# with open('farm.txt', 'w') as f:
#     for a, q in zip(animals,qty):
#         print(f.write(a + ' ' + str(q) + '\n'))




# animals = ['cat', 'dog', 'cow', 'pig', 'rabbit', 'sheep']
# f = open('animals.txt', 'w')
# f.writelines(f'{i} ' for i in animals)
# f.close()
#
# nums = [125, 42, 309]
# f = open('nums.txt', 'w')
# f.writelines(str(i)+' ' for i in nums)
# f.close()


# file = open('new_file.txt', 'w')
# file.write('text on eng\n')
# file.close()


# with open('new_file.txt', 'a') as new_file:
#     new_file.write('\nsecond line')

# with open('new_file.txt', 'w') as file:
#     file.write('\nnew file')
#
# with open('other.txt', 'a') as file:
#     file.write('new file')
#
# with open('other.txt', 'x') as file:
#     file.write('new file')
#
# with open('other.txt', 'r') as file:
#     print(file.read())

# from time import sleep
#
# with open('other.txt', 'r') as file:
#     for i in file.read():
#         sleep(1)
#         print(i, end='')









