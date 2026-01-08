num=[1,2,3,4,5,2,3,4]
res={}
for i in range(len(num)):
      if num[i] in res:
           res[num[i]]+=1
      else :  
       res[num[i]]=1

print(res)