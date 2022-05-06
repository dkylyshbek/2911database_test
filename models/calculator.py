import json
from models.grades import Grade

class Calculator:

    def __init__(self):
        pass

    def calculation(self):

        cfile = open("data/grades.json")
        cgrades = json.load(cfile)
        the_grades = []
        for grade in cgrades:
            my_grade = grade.get("grades")
            the_grades.append(int(my_grade))
        if sum(the_grades) == 0:
            ggrade = 0
        else:
            ggrade = sum(the_grades) / len(the_grades)

        # if type(self.grade)!=int:
        #     raise TypeError

        if ggrade > 100 or ggrade < 0:
            raise ValueError

        elif ggrade >= 93:
            return 4.0

        elif ggrade >= 90:
            return 3.7

        elif ggrade >= 87:
            return 3.3

        elif ggrade >= 83:
            return 3.0

        elif ggrade >= 80:
            return 2.7

        elif ggrade >= 77:
            return 2.3

        elif ggrade >= 73:
            return 2.0

        elif ggrade >= 70:
            return 1.7

        elif ggrade >= 67:
            return 1.3

        elif ggrade >= 63:
            return 1.0

        elif ggrade >= 60:
            return 0.7

        elif ggrade >= 0 and ggrade < 60:
            return 0
