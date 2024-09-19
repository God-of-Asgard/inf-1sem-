x=input().split()
max=0
for i in range (0,len(x)):
    if(x.count(x[i])>max):
        max = x.count(x[i])
for i in range (0,len(x)):
    if(max==x.count(x[i])):
        print(x[i])
        break


