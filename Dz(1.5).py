n =int(input())
a=input()
b=""
c= list(map(''.join, zip(*[iter(a)]*n)))
for i in range(0,len(c)):
    b+=c[i][::-1]
print(b)




