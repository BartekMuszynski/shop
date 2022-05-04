def num1():

    while True :
        try:
            x = int(input("Podaj  liczbe :"))
            return x
            break
        except ValueError:
            print("Podales zla liczbe")
            continue
def num2():
    while True :
        try:
            x = int(input("Podaj  liczbe :"))
            return x
            break
        except ValueError:
            print("Podales zla liczbe")
            continue
def add(num1,num2):
    print(num1 + num2)


x =  num1()
y = num2()
add(x,y)


