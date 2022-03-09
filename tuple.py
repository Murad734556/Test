# data = ("hello", 10, 1.5, 55)
# print(data[1:3])
# lst=list(data)
# data = tuple(lst)


# cars=("lexus", "bmw", "mers", "wer")
# a,b,c,d=cars
# dta=()
# print(type(dta))
# ta=[]
# print(type(ta))
# a=""
# print(type(a))


# for i in range(11):
#     print(i)

# num=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# chet=[]
# nechet=[]
# for i in num:
#     if i % 2 ==0:
#          chet.append(i)
#     else:
#         nechet.append(i)

# print(chet)
# print(nechet)


# a=20
# b=30
# while a<b:
#     a+=1
#     print(a)

# n=0
# for i in range(100):
#     n+=1
#     print(i,n)


# number=[1,2,3,4,5,6,7,8,9,10]
# for i in number:
#      print(i)
#      if i ==7:
#          break
#      else:
#         continue 


# n=0
# while True:
#     n+=1
#     print(n)
#     if n == 1000:
#         break

# num=[]
# for i in range(101):
#     num.append(i)
#     print(num)




# for i in range(1,498):
#     if i % 2 ==0:
#         print(i)


# while True:
#     number1 = int(input("number: "))



            # dictionary

# student={'age': '17'}
# print(student)
# print(student['age'])

# student['18']=18
# print(student)

# print(student.get('color'))

# print(student.values())
# print(student.items())

# for key, value in student.items():



# del student['age']
# print(student)

# student.pop('age')

# contacts={'Muntasir':'0550454844','Kuma': '0554 23 54 89'}
# find_number=input("Name: ")
# title_name=find_number.title()
# if title_name in contacts:
#      print("Такое есть:", contacts [title_name])
# else:
#     print("Такого нет")

# # как добавить значение:

# contacts.setdefault("Faha", '04851540')
# print(contacts)





# contacts={'Muntasir':'0550454844','Kuma': '0554 23 54 89'}
# while True:
#     command=input("1 - добавить \n 2 - удалить \n 3 - искать  \n 4 -посмотреть все контакты  \n")
#     if command =='1':
#                add_name=input("Name: ")
#                add_num=input("Number: ")
#                contacts.setdefault(add_name, add_num)
#                print(f"Контакт {add_name} успешно добавлен!")

#     elif command =='2':
#                add_name=input("Name: ")
#                add_num=input("Number: ")
#                contacts.pop(add_name, add_num)
#                print(f"Контакт {add_name} успешно удален!")
#     elif command == '3': 
#                 find_name=input("Какой контакт вы хотите найти?")
#                 title_find= find_name.title()
#                 if title_find in contacts:
#                        print("Такое есть:", contacts [title_find])
#                        print("Контакт найден")
#                        print(contacts)
#     elif command == '4':
#                   print(contacts)

#     else:
#         print("Неверная команда!")
                           


    

            #    if add_name and  add_num in contacts:
                # print(f"Контакт {add_name} успешно найден!")


students = [
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Agnes', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Doe', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Alex', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Mikkel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susann', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Steve', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aktan', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
]
# for i in students:
#     for key, value in i.items():
#         if value == 'python':
#             print(i)


for i in students:
    for k, v in i.items():
        if i['age']  > 30:
            print(i)







# 1) высните процентное соотношение мужского пола и женского.

# 2) выведите всех студентов с курса python

# 3) уберите дубликаты

# 4) выведите студентов, которые старше 30 и найдите процент их количества относительно других

# 5) отсортируйте студентов по:

# имени

# курсу

# полу

# возрасту

# 6) все студенты курса  javascript  перешли на курс  python.  Как вы поменяете это в словаре ?
# Напишите код

# 7) Добавьте по 5 новых студентов на курсы  java  и  python

# 8)  Отчислите всех студентов младше 15 лет


