class Student:
    def __init__(self, nom, prenom, id):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(
            f"Nom = {self.__nom}  Prenom = {self.__prenom}  ID = {self.__id}  Niveau = {self.__level}")


john = Student("John", "Doe", 145)

john.add_credits(10)
john.add_credits(15)
john.add_credits(5)
john.studentInfo()
