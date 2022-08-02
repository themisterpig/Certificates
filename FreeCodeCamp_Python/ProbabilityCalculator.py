import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            self.contents += v * [k]

    def draw(self, number):
        i = 0
        lista = []

        while i != number:
            randomNumber = random.randint(0, (len(self.contents) - 1))
            while lista.__contains__(randomNumber):
                randomNumber = random.randint(0, (len(self.contents) - 1))
            lista.append(self.contents[randomNumber])

            i = i + 1
        return lista


def getExpectedBalls(expected_balls):

    lista = []
    for k, v in expected_balls.items():
        for a in range(v):
            lista.append(k)
    return lista

def checkList(lista,lista_expected):
    listaDecoy = lista_expected.copy()
    listaDecoy2 = lista.copy()
    for a in lista_expected:
        if listaDecoy2.__contains__(a):
            listaDecoy.remove(a)
            listaDecoy2.remove(a)

    if listaDecoy:
        return False
    else:
        return True

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    lista_expected = getExpectedBalls(expected_balls)
    probability = 0
    for a in range(num_experiments):
        lista = hat.draw(num_balls_drawn)

        if checkList(lista,lista_expected):

            probability = probability + 1

    return probability


if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,expected_balls={"red":2,"green":1},num_balls_drawn=5,num_experiments=2000)
    print(probability)
