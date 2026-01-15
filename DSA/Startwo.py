#Reverse Right triangle

n=5
for i in range (5,0,-1):
    for j in range (i,0,-1):
        print("*",end=" ")
    print()

# Same but with numbers intead of star

n=5
for i in range (5,0,-1):
    for j in range (i,0,-1):
        print(i,end=" ")
    print()