import parser
data = "5**3"
a = parser.expr(data).compile()
# print(a)
res = eval(a)
print(res)