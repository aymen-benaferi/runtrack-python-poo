class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnees : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"x = {self.x}")

    def afficherY(self):
        print(f"y = {self.y}")

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y


p = Point(1, 2)
p.afficherLesPoints()
p.afficherX()
p.afficherY()
p.changerX(3)
p.changerY(4)
p.afficherLesPoints()
