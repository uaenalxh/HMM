import numpy as np

Q=["box1","box2","box3"]#状态集合
V=["红","白"] #观测集合
#O=["红","白","红"]  #观测序列
O=[0,1,0] #转为数字类型
A=np.array([[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]])
B=np.array([[0.5,0.5],[0.4,0.6],[0.7,0.3]])
pai=np.array([0.2,0.4,0.4])

#暴力破解 穷举
sum=0
pathlist=[]#存路径
plist=[]#存概率
for i in range(len(Q)):
    for j in range(len(Q)):
        for k in range(len(Q)):
            pathlist.append((i,j,k))
            plist.append(pai[i]*B[i][O[0]]*A[i][j]*B[j][O[1]]*A[j][k]*B[k][O[2]])
            print((i,j,k) ,pai[i]*B[i][O[0]]*A[i][j]*B[j][O[1]]*A[j][k]*B[k][O[2]])
#看概率最大的路径 则是最优

maxp=max(plist) #计算列表最大值                
xb=plist.index(maxp)#取出最大值所对应的下标
print("最优路径为：",pathlist[xb])#输出最优解pathlist[xb]
print("最优路径对应概率为：",plist[xb])#输出最大概率p[xb]
