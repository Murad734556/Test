# 1
num_1=int(input("First number: "))
num_2=int(input("Second number: "))
if num_1 >= num_2:
    print(num_1)
elif num_1 <= num_2:
    print(num_2)

# 1.2
num1=int(input("number: "))
if num1 <= 0:
    print("Отрицательное ")
elif num1 >= 0:
    print("Положительное ")

1.5
num=int(input("Number: "))
if  num<=0:
    print(num*-1) 


# 2
word1=input("Введите букву: ")
word2=input("Введите букву 2: ")
if word1 == word2:
      print("No")
else:
    print("Yes")

# 3
num = int(input("Number: "))
if num >= -100 and num <= 100:
    print("-")
else:
    print("+")

# 4

season =int(input("Season: "))
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

# 5

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
if num1 or num2 or num3 < 10:
    print("no")
else:
    print("yes")


# 6
print('введите первое число')
a = input()
print('введите второе число')
b = input()
print('введите третье число')
c = input()
print(f'{3-(a+b+c).count("-")}')


#  7
year = int(input("Year: "))
month = int(input("Month: "))
total = (year * 348) + (month * 29)
print(total, "дней прошло")


# 8
year = int(input("Year: "))
month = int(input("Month: "))
total = (year * 348) + (month * 29)
print(total, "дней прошло")

# 9
age=int(input("Age:"))
if age <=18:
    print("Алмаз, еще рано")
elif age >= 18 and age < 40:
    print("Алмаз, идем служить")
elif age == 40 and age > 40:
    print("Алмаз, уже не надо")
else:
    print("уже не надо")