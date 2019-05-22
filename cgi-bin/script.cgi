#!/usr/bin/python
import cgi

print("Content-type: text/html")
print("")

form = cgi.FieldStorage()


print("""
<!doctype html>
<html>
<body>
<h1>hello</h1>

""")

print(form.getvalue("name[]"))


print("""

<a href="/~ludwigm/index.html">back</a>

</body>
</html>
""")
