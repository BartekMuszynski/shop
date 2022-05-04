lst = [1,2,4,0,7,5,0,7,0,0,7]
# for x in range(len(lst)):
#     print(lst[x:x+3])


def split(x):
    lst1 = []
    bond = [0,0,7]
    for i in range(len(x)):
        lst1.append(x[i:i+3])
    if bond in lst1:
        print("My name is Bond,James Bond")
split(lst)