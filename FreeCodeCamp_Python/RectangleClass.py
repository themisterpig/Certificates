class Retangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle (width=' + str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, x):
        self.width = x

    def set_height(self, y):
        self.height = y

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        parimeter = 2 * self.width + 2 * self.height
        return parimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):

        if self.height > 50:
            print("Too big for picture")
        else:
            for x in range(self.height):
                for a in range(self.width):
                    print("*", end="")
                print()
    def get_amount_inside(self,square):
        area = self.get_area()
        area2 = square.get_area()
        return area/area2


class Square:
    def __init__(self, width):
        self.width = width
        self.height = width

    def __str__(self):
        return 'Square (width=' + str(self.width) +')'

    def set_width(self, x):
        self.width = x

    def set_height(self, y):
        self.height = y

    def get_area(self):
        area = self.width * self.height
        return area

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def set_side(self,x):
        self.width =x
        self.height = x

    def get_picture(self):
        if self.height > 50:
            print("Too big for picture")
        else:
            for x in range(self.height):
                for a in range(self.width):
                    print("*", end="")
                print()


if __name__ == "__main__":
    rect = Retangle(10, 5)

    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))