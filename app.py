from flask import Flask, render_template, request

app = Flask(__name__)

# Grade to GPA mapping
grade_points = {
    "A+": 4.0,
    "A": 3.75,
    "A-": 3.5,
    "B+": 3.25,
    "B": 3.0,
    "B-": 2.75,
    "C+": 2.5,
    "C": 2.25,
    "D": 2.0,
    "F": 0.0
}

@app.route("/", methods=["GET", "POST"])
def index():
    cgpa = None
    courses = []

    if request.method == "POST":
        course_names = request.form.getlist("course")
        credits = request.form.getlist("credit")
        grades = request.form.getlist("grade")

        total_points = 0
        total_credits = 0

        for c, cr, g in zip(course_names, credits, grades):
            if c and cr and g:
                cr = float(cr)
                gp = grade_points.get(g, 0)
                total_points += gp * cr
                total_credits += cr
                courses.append({"course": c, "credit": cr, "grade": g, "point": gp})

        if total_credits > 0:
            cgpa = round(total_points / total_credits, 2)

    return render_template("form.html", cgpa=cgpa, courses=courses, grades=grade_points.keys())

if __name__ == "__main__":
    app.run(debug=True)
