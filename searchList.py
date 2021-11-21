l = ["this is good","python is good","python is not python without any module"]

# for list in l:
#     print(list.count("this is good"))

for list in l:
    if list.__contains__("python is"):
        print(list)
        
    