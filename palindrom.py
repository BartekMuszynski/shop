def palindrom(arg):

    y = arg.replace(" ","").strip().lower()
    if y == y[::-1]:
        return True
    else:
        return False


print(palindrom(" Bab "))
