import re
string = ["this is good","python is good","python is not python without any module"]
# string = "this is my python. python is good. python is not python without any module"
pattren = re.compile(r"python")
result = pattren.finditer(str(string))
print(result)
for match in result:
    print(match)

