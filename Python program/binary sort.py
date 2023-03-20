a=[10,11,12,13,14,15,16,17,18,19,20]
i=0
start=i
end=len(a)-1
num=input ("enter the desire number")
num=int(num)
while (start<end):
    
    
    
    
        
    mid=(start+end)/2
    mid=round(mid)
    mid1=a[mid]
    if (num>mid1):
        start=mid
        end=len(a)-1
        
        
    if (num<mid1):
        start=i
        end=mid
        
        
    if (num==mid1):
        i=mid-1
        print (i+1)
        break
     
else:
    print("your Desire number is not in the list")
            
    
