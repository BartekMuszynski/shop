from tabulate import tabulate
bbasket = {"number of products ": 0, "total gross price": 0, "total net price ": 0,"products": []}

products = [["banana",10,8,2],
        ["orange",12,10,2],
        ["apple",5,3,2],
        ["pear",8,6,2],
        ["watermelon",20,18,2]]
data= [["banana",1,10,8,2],
        ["orange",2,12,10,2],
        ["apple",3,5,3,2],
        ["pear",4,8,6,2],
        ["watermelon",5,20,18,2]]
table = tabulate(data,headers=["name","number","gross_price","net_price","tax"],tablefmt="fancy_grid")
print(table)



class shop:
        def choice(self):
                while True:
                        try:
                                self.y = int(input("Please chose product number: "))
                                assert  self.y in range(1,6)
                                return  self.y

                        except AssertionError:
                                print("There is no product with such a number")
                                continue
                        except ValueError:
                                print("That's not a number")
                                continue



        def basket_add(self):
                if self.y == 1:
                        bbasket["number of products "] += 1
                        bbasket["total gross price"] += products[0][1]
                        bbasket["total net price "] += products[0][2]
                        bbasket["products"].append([products[0][0]])
                if self.y == 2:
                        bbasket["number of products "] += 1
                        bbasket["total gross price"] += products[1][1]
                        bbasket["total net price "] += products[1][2]
                        bbasket["products"].append([products[1][0]])
                if self.y == 3:
                        bbasket["number of products "] += 1
                        bbasket["total gross price"] += products[2][1]
                        bbasket["total net price "] += products[2][2]
                        bbasket["products"].append([products[2][0]])
                if self.y == 4:
                        bbasket["number of products "] += 1
                        bbasket["total gross price"] += products[3][1]
                        bbasket["total net price "] += products[3][2]
                        bbasket["products"].append([products[3][0]])
                if self.y == 5:
                        bbasket["number of products "] += 1
                        bbasket["total gross price"] += products[4][1]
                        bbasket["total net price "] += products[4][2]
                        bbasket["products"].append([products[4][0]])
                print("Shopping summary: ", bbasket)


        def basket_dicard(self):
                try :
                        self.d = int(input("What product Would You like to discard ?Enter the number "))
                        return self.d
                except ValueError:
                        print("Not in basket !")

                if self.d == 1:
                        bbasket["number of products "] -= 1
                        bbasket["total gross price"] -= products[0][1]
                        bbasket["total net price "] -= products[0][2]
                        bbasket["products"].remove([products[0][0]])
                if self.d == 2:
                        bbasket["number of products "] -= 1
                        bbasket["total gross price"] -= products[1][1]
                        bbasket["total net price "] -= products[1][2]
                        bbasket["products"].remove([products[1][0]])
                if self.d == 3:
                        bbasket["number of products "] -= 1
                        bbasket["total gross price"] -= products[2][1]
                        bbasket["total net price "] -= products[2][2]
                        bbasket["products"].remove([products[2][0]])
                if self.d == 4:
                        bbasket["number of products "] -= 1
                        bbasket["total gross price"] -= products[3][1]
                        bbasket["total net price "] -= products[3][2]
                        bbasket["products"].remove([products[3][0]])
                if self.d == 5:
                        bbasket["number of products "] -= 1
                        bbasket["total gross price"] -= products[4][1]
                        bbasket["total net price "] -= products[4][2]
                        bbasket["products"].remove([products[4][0]])
                print("Shopping summary: ", bbasket)




        def shopping(self):
                shop.choice(self)
                shop.basket_add(self)
                while True :
                        self.x = input("What action would You like to do now ?\n Continue shopping-->Press 'c'\n"
                                       "Discard a product from the basket-->Press 'd'\n"
                                       "End shopping-->Press any letter\n").lower()
                        if self.x == "c":
                                shop.choice(self)
                                shop.basket_add(self)
                        elif self.x == 'd':
                                shop.basket_dicard(self)
                        else:
                                print(bbasket)
                                break


g1 = shop().shopping()
