import datetime
def getdate():
    # datetime.datetime.now()
    date = datetime.datetime.now()
    return date
with open("usamaFile","a") as introFile:
    d = getdate()
    introFile.write(str(d))
    newline = introFile.write("\n")
    # readline = introFile.readlines()
    # print(readline)
    # food = input()
    # writedata = introFile.write(food)
# file = open("usamaFile")
# readMode = file.readline()
# print(readMode)
# # print(file.readline())
# file.close()