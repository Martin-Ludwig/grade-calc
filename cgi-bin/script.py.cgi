#!/usr/bin/python
import cgi
from collections.abc import Iterable

def get_parsed_field_storage():
    form_values = {}
    form = cgi.FieldStorage()
    for list in form:
        if form.getlist(list):
            form_values[list] = form.getlist(list)

    return form_values

def calc_grade(grades):
    if not grades:
        return []

    avgGrade = 0
    totalEcts = 0

    for i in range(len(grades["grades[]"])):
        avgGrade += float( grades["grades[]"][i] ) *  float( grades["ects[]"][i] )
        totalEcts += float(grades["ects[]"][i])

    grade = float(avgGrade) / float(totalEcts)
    return round(grade, 2)


form_values = get_parsed_field_storage()
amount = len(form_values["grades[]"])
avg_grade = calc_grade(form_values)

grade_class = ""
if (avg_grade <= 4):
    grade_class = "passed"
else:
    grade_class = "failed"

print("Content-type: text/html")
print("")

print("""<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="/~ludwigm/style.css">
	<title>Grade calculator</title>
</head>
<body>
    <h1>Grade calculator</h1>
""")

print("<p class=\"subline\">Your grade: <label class=\"avg-grade ",grade_class,"\">")
print(avg_grade)
print("</label></p>")

if amount > 0:
    print("""
        <div id="grade-results">
            <div class="modules-wrapper">
                <div class="module">
                    <div class="name">
                        Name
                    </div>
                    <div class="grade">
                        Grades
                    </div>
                    <div class="ects">
                        ETCS
                    </div>
                </div>
    """)


    for i in range(amount):
        print("""
            <div class="module">
            <div class="name">""")
        print(form_values["names[]"][i])
        print("""</div>
            <div class="grade">""")
        print(form_values["grades[]"][i])
        print("""</div>
            <div class="ects">""")
        print(form_values["ects[]"][i])
        print("""</div>
        </div>""")

    print("""
            </div>
        </div>
    """)

print("""
<a class="back" href="/~ludwigm/index.html">back</a>
</body>

</html>
""")
