from tabulate import tabulate


class Shop :
    def product(self,name,price):
        #create a product
        self.name  =  name
        self.price = price

    def table(self):
         data = [[self.name,self.price]]
         self.table = tabulate(data, headers=["name", "price"], tablefmt="fancy_grid")
         print(self.table)







banana = Shop()
banana.product("banana",10)
banana1 = Shop()
banana1.product("banana1",12)
banana1.table()