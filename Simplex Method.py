a=[[2,3,1,0,0,6],[3,7,0,1,0,12],[-7,-12,0,0,1,0]]
def pivotcolumn():
    global a
    global pivotcolumn1
    global f
    
    b=a[-1]
    c=len(a[-1])
    i=0
    f=[]
    e=[]
    o=[]
    while (i<c):
        print(a)
        d=b[i]
        if(d<0):
            f.append(d)
        else:
            e.append(1)
        i+=1
##    gg=0
##    while(gg<len(f)):
    if(len(f)==0):
        print("Given data is optimal")
    if(len(f)!=0):
        t=sorted(f)
        j=0
        while(j<len(f)):
         if(t[0]==f[j]):
             o.append(j)
         else:
             i=0
         j+=1    
    pivotcolumn1=(o[0])
##        gg+=1
    return f

def pivotrow():
    global pivotrow1
    pivotcolumn=pivotcolumn1
   
##    ff=0
##    while(ff<len(f)):
    v=0
    z=[]
    while(v<len(a)-1):
        y=a[v][-1]/a[v][pivotcolumn]
        z.append(y)
        v+=1

    s=0
    q=[]
    u=sorted(z)

    while(s<len(f)):
        if(u[0]==z[s]):
            q.append(s)
        else:
            i=0
        s+=1
    print(q)
    pivotrow1=q[0]
    return pivotrow1
def pivotelement():
    global pivotelement1
    pivotcolumn=pivotcolumn1
    pivotrow=pivotrow1
    pivotelement1=a[pivotrow][pivotcolumn]
    print(pivotelement1)
    print(f"So,Pivot column={pivotcolumn+1} and Pivot row={pivotrow+1} and Pivot Element={pivotelement1}")
    return pivotelement1
def simplexmethod (a):
    global hh
    
    pivotelement=pivotelement1
    pivotrow=pivotrow1
    pivotcolumn=pivotcolumn1

    hh=0
    while(hh<len(f)):
        l=0
        while(l<len(a[0])):
         cc=a[pivotrow][l]/pivotelement
         round1=round(cc,3)
         a[pivotrow][l]=round1
         l+=1
        x=0
        while(x<len(a)):
            rr=0
            li=[]
            while(rr<len(a[0])):
             if(x!=pivotrow):
              ele=(-a[pivotrow][rr]*a[x][pivotcolumn]+a[x][rr])
              li.append(ele)
              rr+=1                                                                                                           
             elif (x==pivotrow):
              i=0
              rr+=1
            
            if(x!=pivotrow):
             a[x]=li
            
            x+=1
       
        
       
        hh+=1
j=len(f)
b=pivotcolumn()
while(j<len(f)):
    pivotcolumn()
    pivotrow()
    pivotelement()
    simplexmethod(a)
    j+=1
