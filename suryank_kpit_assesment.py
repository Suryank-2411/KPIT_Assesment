lst1= [1,2,3,4,5,6,7]
lst2=[[2,3],[4,5],[1,6]]
n=len(lst1)
lst3=[1]
ans=[]
for i in range(1,n):
    lst3.append(lst1[i]^lst3[i-1])
    
for j in lst2:
    if(j[0]==0):
        ans.append(lst3[j[1]])
    else:
        ans.append(lst3[j[1]]^lst3[j[0]-1])
print(ans)        