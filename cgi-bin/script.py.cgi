#!/usr/bin/python
import cgi
from collections.abc import Iterable



print("Content-type: text/html")
print("")

print("""
<!doctype html>
<html>
<body>
""")

form = cgi.FieldStorage()
form_values = {}

print(form)

print("<hr>")

for list in form:
    print(list, " : ")
    print(form.getlist(list))
    print("<br>")
    form_values[list] = form.getlist(list)
    amount = len(form.getlist(list))

print("form_values: ",form_values)

print("<br>amount: ",amount)

print("<hr>")

for i in range(amount):
    print("""
    	<div class="modules-wrapper">
			<div class="module">
				<input placeholder="Name" value=""")
    print("\"",form_values["name[]"][i],"\"",sep="")
    print(""" type="text" name="name[]">
				<select name="grade[]">
					<option>1.0</option>
					<option>1.3</option>
					<option>1.7</option>
					<option>2.0</option>
					<option>2.3</option>
					<option>2.7</option>
					<option>3.0</option>
					<option>3.3</option>
					<option>3.7</option>
					<option>4.0</option>
					<option>5.0</option>
				</select>"""
    )
    print("""<input type="number" value=""")
    print("\"",form_values["ects[]"][i],"\"",sep="")
    print(""" min="1" step="1" name="ects[]">
			</div>
		</div>
        """)


print("""
<hr>
<a href="/~ludwigm/index.html">back</a>

</body>
</html>
""")
