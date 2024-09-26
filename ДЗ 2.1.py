def prostoe(n):
    pr =[]
    a=2
    while (a**2<=n):
        if n%a ==0:
            pr.append(a)
            n=n//a
        else:
            a+=1
    if n>1:
        pr.append(n)
    return(pr)
n=int(input())
print(prostoe(n))