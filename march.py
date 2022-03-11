# numbers={1,2,3,4,5,6,7,8,9}
# print(numbers)

# Set- множества. в нем хранится уникальное значение


# cars={"Audi", "BMW", "Lexus"}
  
# #   Добавление
# cars.add('Nissan')

# print(cars)
# # Удаление случайного элемента
# cars.pop()
# # удаление указанного элемента 
# cars.remove("BMW")


# # objekts={}

# names={"Kurmanbek", "Muntasir", "Faha", "Diana", "Faha"}

# for i in names():
#     print(names)

# # 

# names=set(names)
# print(names)


# numbers={10,1,11,500,5,7}
# print(sorted(numbers))


# numbers={}

# while True:
            
#             try:
#                 num1=int(input("Number1: "))
#                 num2=int(input("Number2: "))


#                 print(num1 / num2)
#             # except ZeroDivisionError:
#             except ValueError:
#                 print("Строки нельзя делить")



# n=0
# while True:
#     n+=1
#     print(n)
#     if n == 1000:
#         raise ZeroDivisionError("Stop")



while True:


    
    num1=int(input("введите число1: "))
    num2=int(input("введите число2: "))
    operation=input('+, -, *, / \n ')
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1-num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        try:
            print(num1/num2)
        except ZeroDivisionError:
            print("На ноль делить нельзя")      

#hello
