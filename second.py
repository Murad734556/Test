# num1=int(input("Num1:"))
# num2=int(input("num2: "))
# print(num1+num2)



# name=input("Name: ")
# surname=input("Surname: ")
# company=input("Company: ")
# print(f"""{name} {surname} is a talanted classic Pianist.
# He study at: {company}""")

# full='Edzen Dzen'
# print(full[::-1])


# text="""Бессознательное - некая энергия, а не биология и физиология,
#  это некоторые инстинктивные слои психики, которые охватывают все
#   особенности личности, все прежние 
# переживания человеческого опыта и все существующие типы поведения."""
# print(text.count(","))

# a= 100000
# b=200
# c=400
# if b> a and b > c:
#      print("b больше ")
# elif a > b and a > c:
#     print("a больше")
# elif c > b and c > a:
#     print("c больше ")
 
# age= int(input("Введите возраст: "))
# if age < 7:
#     print("В садик ")
# elif age >= 7 and age < 18:
#     print("В школу ")
# elif age >= 18 and age < 65:
#     print("В универ ")
# else:
#     print("В пенсию") 





# num = int(input("Number: "))
# if num % 2 ==0:
#     print("Четное")
# else:
#     print("Нечетное")




# day= int(input("Day: "))
# month=int(input("Month: "))
# year=int(input("Year: "))
# if day >= 1 and day <= 28:
#       if month >= 1 and month<=12:
#         if year >=1 and year <= 2022:
#           print("Правильный дата ")
#         else:
#             print("Неправильный год ")
#       else:
#           print("Неправильный месяц  ")
# else:
#     print("Неправильный день ")



num_1= int(input("Первое число: "))
num_2= int(input("Второе число: "))
if num_1 > num_2:
    print("Первое число больше  ")
else:
    print("Второе число больше ")


age=int(input("Age:"))
if age <=18:
    print("Алмаз, еще рано")
elif age >= 18 and age < 40:
    print("Алмаз, идем служить")
elif age == 40 and age > 40:
    print("Алмаз, уже не надо")
else:
    print("уже не надо")



season = int(input("Season: "))
if season in [12, 1, 2]:
    print("Зима")
elif season in [3, 4, 5]:
    print("Весна")
elif season in [6, 7, 8]:
    print("Лето")
elif season in [9, 10, 11]:
    print("Осень")
else:
    print("Неправильный диапозон")