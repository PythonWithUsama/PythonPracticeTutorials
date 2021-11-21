import time
# startTime = time.time()
# print(startTime)
# localTime = [time.asctime()]
# localTime = time.asctime()
# localTime = time.asctime(time.localtime(time.time()))
# print(localTime)
startTime = time.time()
for line in range(0,1000000):
    print(line,end=" ")
print("After executing for Loop ===> \n\n", time.time()-startTime)
startTime2 = time.time()
count = 1
while(True):
    print(count,end=" ")
    count +=1
    if count ==10000:
        break
print("After executing while loop ===> ", time.time()-startTime2)
