basket = {"total to pay":15,"net value to pay ":16,"total number of products":17,"products in basket": ["lala"]}
data = {"banana": {"gross price": 10,"net price": 8},"orange": {"gross price": 110,"net price": 108}}

# y = input("Write :")
# if y in data:
#         basket["total to pay"]+=data[y]["gross price"]
#         basket["net value to pay "]=data[y]["net price"]
#
# print(basket)
# y = input("Write :")
# if y in data:
#         basket["total to pay"]+=data[y]["gross price"]
#         basket["net value to pay "]=data[y]["net price"]
# print(basket)
# data["apple"] = {"gross price": 10,"net price": 8}
# print(data)
# print(data["banana"]["gross price"])
for key, value in basket.items():
    if type(basket[key]) == list:
        basket[key] = []
    else :
        basket[key] = 0

print(basket)