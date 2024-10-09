# словари, множества


student = {
    'name': 'Albina',
    'age': 20
}

student['surname'] = 'Sagnalieva'
student.update({'volv':'perter', 'ree': 'sdfre'})

student['age'] = 21


print(student)
#
# print(student['name'])
# print(student.get('',' nety'))



#
# time = input('enter time: ').lower()
#
#
# if time == 'утро' or time == 'morning' :
#     print('доброе утро')
# elif time == 'день'   or time == 'day':
#     print('добрый день')
# elif time == 'вечер'  or time == 'evening' :
#     print('добрый вечер')
# else:
#     print('Здраствуйте! время суток не известно')
#










#
# beshbarmak = {'лапша',"мясо", "лук"}
# plov = {'рис', 'морковь', 'мясо'}
#
#
# # print(beshbarmak.symmetric_difference(plov))
# # print(beshbarmak ^ plov)
#
# print(beshbarmak.intersection(plov))
# print(beshbarmak & plov)

# print(beshbarmak.difference(plov))
# print(beshbarmak - plov)
#
# print(beshbarmak.union(plov))
# print(beshbarmak | plov)










#
# numbers1 = [1,2,3,4,2,1,3,5]
# numbers2 = (1,2,3,4,2,1,3,5)
# numbers3 = {1,2,3,4,2,1,3,5}
#
# print(numbers1)
# print(numbers2)
# print(numbers3)













## students = {
#     'name': 'Albina',
#     'age': 20,
#     'surname': 'Sagnalieva'
#
#  }
#
# for key, value in students.items():
#     print(f'{key} - {value}')
#



# print(students.keys())
# print(students.values())
# print(students.items())






# for i in students:
#     print(f'{i}: {students[i]}')


# '''delete'''
# students.pop('age')
# del students['surname']
#
#
# '''edit'''
#
# students['age'] = 19
#
#
# '''add '''
# students['surname'] = 'Sagnalieva'
# students.update({'weight': 67.4, 'height': 1.65  })
#
# print(students)
#
#
#
#
#





#
# ''' доступ к значениям словоря'''
# print(students['name'])
# print(students.get('', 'not have'))





#
# '''доступ к значениям словаря'''
# print(students['name'])
# print(students.get('nam', 'not this plase'))
