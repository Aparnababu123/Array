def assign(a,n):
    a.sort()
    ans=[0]*n
    p=0
    q=n-1
    for i in range(n):
        #checking for even indexes
        if(i+1)%2==0:
            ans[i]=a[q]
            q-=1
        else:
            ans[i]=a[p]
            p+=1
    for  i in range(n):
        print(ans[i], end=' ')
a=[1,2,3,4,6,5]
n=len(a)
assign(a,n)