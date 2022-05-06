

class Course:
    def __init__(self, course_number, teacher, credits, grades):
        self.course_number = course_number
        self.teacher = teacher
        self.credits = credits
        self.grades = grades
        

    
    def to_dict(self):
        return {
            "course_number": self.course_number,
            "teacher": self.teacher,
            "credits": self.credits,
            "grades": self.grades,
        }
           
