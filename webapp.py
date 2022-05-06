import json
from flask import Flask, request, jsonify, render_template, redirect
import requests
from models.grades import Grade

from models.student import Student
from models.courses import Course
from models.calculator import Calculator

app = Flask(__name__)
STUDENT = Student("Ryan")
CALC = Calculator()

@app.route("/")
def homepage():

    return render_template("home.html", student=STUDENT, calc=CALC)

@app.route("/delete/<course_number>")
def delete(course_number):
    if STUDENT.delete(course_number):
        STUDENT.save()
        return redirect("/")
    else:
        return "Unsucessful", 404

@app.route("/view/<course_number>")
def view(course_number):
    course=STUDENT.find_course_by_id(course_number)
    if course!=None:
        return render_template("view.html", course=course, student=STUDENT), 201
    else:
        return "Course not found", 404


@app.route("/create", methods=["GET","POST"])
def create_page():
    if request.method=="GET":
        return render_template("create.html")

    if request.method=="POST":
        course_number=request.form.get("course_number")
        teacher=request.form.get("teacher")
        credits=request.form.get("credits")
        grades=request.form.get("grades")
        try:
            new_course=Course(course_number, teacher, credits, grades)
            new_grade=Grade(grades)
            STUDENT.add(new_course, new_grade)
            STUDENT.save()
            return render_template("home.html", student=STUDENT, calc=CALC)
        except:
            return "Error", 404

@app.route("/calculate", methods=["GET"])
def calculate():
    if request.method=="GET":
        CALC.calculation()
        return render_template("home.html", calc=CALC, student=STUDENT)




if __name__ == "__main__":
    app.run(debug=True)

