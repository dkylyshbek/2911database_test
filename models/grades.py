class Grade:
    def __init__(self, grades):
        self.grades = grades
        

    
    def to_dict(self):
        return {
            "grades": self.grades,
        }
           