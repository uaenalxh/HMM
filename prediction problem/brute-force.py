import numpy as np

Q=["box1","box2","box3"]
V=["红","白"] 
O=[0,1,0] #observation collection
A=np.array([[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]])
B=np.array([[0.5,0.5],[0.4,0.6],[0.7,0.3]])
pai=np.array([0.2,0.4,0.4])

#brute force
sum=0
pathlist=[]
plist=[]
for i in range(len(Q)):
    for j in range(len(Q)):
        for k in range(len(Q)):
            pathlist.append((i,j,k))
            plist.append(pai[i]*B[i][O[0]]*A[i][j]*B[j][O[1]]*A[j][k]*B[k][O[2]])
            print((i,j,k) ,pai[i]*B[i][O[0]]*A[i][j]*B[j][O[1]]*A[j][k]*B[k][O[2]])

maxp=max(plist)             
xb=plist.index(maxp)
print("The optimal path:",pathlist[xb])
print("The optimal probability:",plist[xb])
