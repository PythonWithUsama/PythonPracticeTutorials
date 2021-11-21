# *args
# def sumofN(*numberlist):
#     sum = 0
#     for add in numberlist:
#         sum +=add
#     print(sum)
# numberList = [1,2,3,4,5,6]
# sumofN(*numberList)

# **kwargs
def employData(**data):
    for key, value in data.items():
        print(f"{key} is {value}")

employData(Firstname = "Usama", LastName = "Amjid", age = 20, phone = 3032665710)
employData(Firstname = "DarkWeb", LastName = "Programmer", age = 21, phone = +923486565710)
employData(name="Sumaira Parveen", age= 22, phone = 3032654545454545454545)