import numpy
import random
a = numpy.array([[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5],])
b = numpy.ones((3,3))
c = numpy.full((3,3),10)
d = numpy.random.randint(-5,10,size=(3,3))
x = numpy.ones((5,5))
y = numpy.zeros((3,3))
y[1,1] = 9
x[1:4#rzedy,1:4#kolumny] = y
print(x)


# import numpy
# # import copy
# # y = numpy.full((10,6),"                         ")
# y = numpy.linspace(1,10)
# y[0,0] = "Product"
# y[0,1] = "Name"
# y[0,2] = "Quantity"
# y[0,3] = "Gross_price"
# y[0,4] = "Net_price"
# y[0,5] = "Tax"
# y[1,0] = "Product"
# y[1,1] = "Banana"
# y[1,2] = 1
# y[1,3] = 10
# y[1,4] = 8
# y[1,5] = 2
#
# print(y)