# 1



for i in range(5):
    print(0)
   

# 2

num=[]
for i in range(1,100):
    num.append(i)
    print(i)




## 3

for  i in range(1,497):
    if i %2==0:
      print(i)
    
# 4

for i in range(1,1000000):
    print(sum.i)    



# 5

num=[]
for i in range(1,100):
    num.append(i)
    print(0)

# 6

bum=input("Введите текст: ")
bum1=input("Введите тексt2: ")
bum1, bum=bum,bum1
print(bum,"\n", bum1 )

# 7

while True:
      num=int(input("Введите возраст: "))
      while num > 18:
        print("Доступ разрешен!")
        
        break
      else:
           print("Извините доступ разрешен только с 18 лет")
           continue


# 8



while True:
        a= input("Пароль 1: ")
        b= input("Пароль 2: ")

        if a != b:
            print("Различаются! ")
        elif len (a)<8:   
            print("Короткий ")
        elif "123" in a:
            print("Простой! ")


        else:
            print("OK")
            break    
