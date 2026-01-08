num=[1,1,1,2,2,2,3,3,3,4,5,5]
count=1
res={}
for i in range(len(num)):
      if i==len(num)-1:
           res[num[i]]=count 
      elif num[i]==num[i+1]:
       count += 1
      else :  
       res[num[i]]=count
       count=1

print(res)