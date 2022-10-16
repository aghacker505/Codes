n=int(input()) #number oF test cases
l=[] #creating an empty list
def result(n):
    s=''  #an empty string
    #assigning the return values
    if n==3:
        return '010'
    elif n==4:
        return '1001'
    elif n==5:
        return '01010'
    elif n==6:
        return '010010'
    else:
        n=n-3
        s='010'
        while n!=3:
            n-=1
            s+='0'
        s+='010'
    return s
for k in range(n):
    a=int(input())
    l.append(result(a))
for j in l:
    print(j)