def anagram(arg):
    y = arg.strip().lower()
    lst = list(y.split(" "))
    lista = list(lst[0])
    listaa = list(lst[-1])
    lista.sort()
    listaa.sort()
    if lista == listaa:
        print("lol")
    else:
        print("not ol")


anagram("modern norman")