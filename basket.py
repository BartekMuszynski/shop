from tabulate import tabulate

basket = {"total to pay":0,"net value to pay ":0,"total number of products":0,"products in basket": []}#empty basket to begin with
data = [] #list used to create a table of products in shop
items_in_shop = {} #informations about all products in the shop
class Shop :
    def product(self,name,grossprice,netprice):
        #create a product
        self.name  =  name
        self.grossprice = grossprice
        self.netprice = netprice
        data.append([self.name,self.grossprice,self.netprice])
        items_in_shop[self.name] = {"gross price": self.grossprice, "net price": self.netprice}


    def table(self):
        #create table of products available in shop
        self.table = tabulate(data, headers=["name", "gross price","net price"], tablefmt="fancy_grid")
        print(self.table)

    def product_buy(self):
        #buying a product
        self.product_purchase = input("Write the name of the product You would like to purchase: ")
        if self.product_purchase in items_in_shop.keys():
            basket["products in basket"].append(self.product_purchase)
            basket["total to pay"] += items_in_shop[self.product_purchase]["gross price"]
            basket["net value to pay "] += items_in_shop[self.product_purchase]["net price"]
            basket["total number of products"] += 1
            print(basket)
        else:
            print("Sorry we don't have it !")

    def del_product_from_basket(self):
        #delete a product from the basket
        self.deleting_product_from_basket = input("Write the name of the product You would like to delete: ")
        if self.deleting_product_from_basket in basket["products in basket"]:
            basket["products in basket"].remove(self.deleting_product_from_basket)
            basket["total to pay"] -= items_in_shop[self.deleting_product_from_basket]["gross price"]
            basket["net value to pay "] -= items_in_shop[self.deleting_product_from_basket]["net price"]
            basket["total number of products"] -= 1
            print(basket)
        else:
            print("There is no such a  product in Your basket")

    def clean_basket(self):
        #remove all products from the basket
        for key, value in basket.items():
            if type(basket[key]) == list:
                basket[key] = []
            else:
                basket[key] = 0
        print(basket)

    def change_products_in_basket(self):
        #change properties of products in basket
        self.product_to_change = input("What product would you like to change ?")
        if self.product_to_change in basket["products in basket"]:
            self.action_change = input("What would You like to change :\n"
                                       "Product price-->press 'p'\n"
                                       "Remove a product from basket--> press 'r'\n"
                                       "Increase ammount of products --> press'c'")
            if self.action_change == "p":
                self.new_price = int(input("Write new  gross price:"))
                basket["total to pay"] -= items_in_shop[self.product_to_change]["gross price"]
                basket["net value to pay "] -= 2
                basket["total to pay"] += self.new_price
                print(basket)
            elif self.action_change == "r":
                basket["products in basket"].remove(self.product_to_change)
                basket["total to pay"] -= items_in_shop[self.product_to_change]["gross price"]
                basket["net value to pay "] -= items_in_shop[self.product_to_change]["net price"]
                basket["total number of products"] -= 1
                print(basket)
            elif self.action_change == "c":
                self.new_amount = int(input("Write new amount: "))
                for i in range(self.new_amount) :
                    basket["products in basket"].append(self.product_to_change)
                    basket["total to pay"] += items_in_shop[self.product_to_change]["gross price"]
                    basket["net value to pay "] += items_in_shop[self.product_to_change]["net price"]
                    basket["total number of products"] += 1
                print(basket)



    def shopping(self):
        #all actions during shopping
        Shop.product_buy(self)
        while True:
            self.choice_of_action = input("What action would You like to do now ?\n Continue shopping-->Press 'c'\n"
                           "Delete a product from the basket-->Press 'd'\n"
                            "Remove all products from the basket-->Press 'r'\n"
                            "Change properties of products in the basket-->Press 'ch'\n"
                           "End shopping-->Press any other  letter\n").lower()
            if self.choice_of_action == "c":
               Shop.product_buy(self)
            elif self.choice_of_action == 'd':
                Shop.del_product_from_basket(self)
            elif self.choice_of_action == "r" :
                Shop.clean_basket(self)
            elif self.choice_of_action == "ch":
                Shop.change_products_in_basket(self)
            else:
                print(basket)
                break


#initate some products
banana = Shop()
banana.product("banana",10,8)
orange = Shop()
orange.product("orange",12,10)
apple = Shop()
apple.product("apple",6,4)
pear = Shop()
pear.product("pear",20,18)
avocado = Shop()
avocado.product("avocado",30,28)
client = Shop()
client.table()
client.shopping()


