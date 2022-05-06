import json
from tabnanny import check
from models.calculator import Calculator
from models.courses import Course
from models.grades import Grade


class Student():
    def __init__(self, name:str):
        self.name=name
        file=open("data/courses.json")
        courses=json.load(file)
        self.courses=[]
        self.grades=[]
        for course in courses:
            course_number=course.get("course_number")
            teacher=course.get("teacher")
            credits=course.get("credits")
            grades=course.get("grades")
            course_obj=Course(course_number, teacher, credits, grades)
            grade_obj= Grade(grades)
            self.grades.append(grade_obj)
            self.courses.append(course_obj)
          


    def save(self):
        course_list=[]
        grade_list=[]
        for course in self.courses:
            course_dict=course.to_dict()
            course_list.append(course_dict)
        for grade in self.grades:
            grade_dict=grade.to_dict()
            grade_list.append(grade_dict)
        file=open("data/courses.json", 'w')
        gfile=open("data/grades.json", 'w')
        gfile.write(json.dumps(grade_list))
        file.write(json.dumps(course_list))
    
    def delete(self, course_id):
        for i,course in enumerate(self.courses):
            if course.course_number==course_id:
                self.courses.pop(i)
                self.grades.pop(i)
                return True
        return False

    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_number==course_id:
                return course
        return None

    def add(self, course, grade):
        if isinstance(course, Course):
            self.courses.append(course)
        if isinstance(grade, Grade):
            self.grades.append(grade)

