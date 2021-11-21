# with open("Usama","a") as writeSomething:
#     writeSomething.write("Hello, my name is usama amjid")
# with open("Sumaira.txt","a") as writesomething:
#     inputName = input("Enter name: ")
#     writesomething.write(inputName)
#     print("wirte successfully...")
# with open("maryam","at") as writesomething:
#     inputName = input("Enter name: ")
#     writesomething.write(inputName)
#     print("wirte successfully...")
# with open("maryam") as readlineof_maryam:
#     for fileline in readlineof_maryam:
#         print(readlineof_maryam.read())
#
# creatFile = input("Enter file name: ")
# with open(creatFile,"at") as writeSomething:
#     wirteData = input("Enter data of client: ")
#     writeSomething.write(wirteData)
#     print("successfully write...")
#
with open("ClientData") as readData:
    print(readData.read())