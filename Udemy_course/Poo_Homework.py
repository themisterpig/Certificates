import math

#
# class Line:
#     def __init__(self,coor1,coor2):
#         #two list =[num,num]
#         self.coor1 = coor1
#         self.coor2 = coor2
#
#     def distance(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         print(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
#
#
#
#     def slope(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         print( (y2 - y1) / (x2 - x1))
#
# # EXAMPLE OUTPUT
#
# coordinate1 = (3,2)
# coordinate2 = (8,10)
#
# li = Line(coordinate1,coordinate2)
#
# li.distance()
#
# li.slope()

#
# class Cylinder:
#
#     pi = math.pi
#
#     def __init__(self,height=1,radius=1):
#         self.height = height
#         self.radius = radius
#
#     def volume(self):
#         result = self.height * self.pi * self.radius ** 2
#         print(result)
#
#     def surface_area(self):
#         top = self.pi * (self.radius) ** 2
#         print((2 * top) + (2 * self.pi * self.radius * self.height))
#
#
# c = Cylinder(2,3)
# c.volume()
# c.surface_area()