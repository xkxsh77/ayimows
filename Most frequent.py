def most_frequent(s):
    a=[i for i in s]
    b= list(set(a))
    c = []
    for i in range (len(b)):
        c.append (a.count(b[i]))
    for i in range (len(b)) :
       for j in range (i+1,len(b)):
        if c[i]<=c[j]:
            c[i],c[j]=c[j],c[i]
            b[i],b[j]=b[j],b[i]
    for i in range (len(b)):
         print(b[i]+" = "+str(c[i]))
a=input().strip()
most_frequent (a)
