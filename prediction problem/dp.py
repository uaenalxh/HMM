import numpy as np
import matplotlib.pyplot as plt

class Viterbi:
    def __init__(self,o,A,B,PI,index):
       self.o=o
       self.A=A
       self.B=B
       self.index = index
       self.N=self.A.shape[0] #number of states
       self.M = len(self.index)  # types of observations
       self.T =len(self.o) #numbers of observations
       self.PI=PI # initial state 
       self.delte=np.zeros((self.T, self.N))
       self.I=[] #得到的状态序列是
       self.keci=np.zeros((self.T, self.N), dtype=int)

    def cal_delte(self):
        # 在书中时刻t的取值是 1到 T 但是写代码数组是从0 开始的 方便起见 我们讲t也从0开始
        o1=self.o[0]#第一个观测变量是
        o1_index=self.index[o1] #第一个观测变量的下标是
        for i in range(self.N):
            self.delte[0][i] = self.PI[i][0]*self.B[i][o1_index]
        for t in range(1,self.T):#从时刻t=1 开始 到T-1
            ot=self.o[t]
            ot_index=self.index[ot]   
            for i in range(self.N):
                max=0
                maxj=0
                for j in range(self.N):
                    a = self.delte[t-1][j] *self.A[j][i]*self.B[i][ot_index]
                    if a>max:
                        max=a
                        maxj=j
                self.delte[t][i]=max
                self.keci[t][i]=maxj
        
    def cal_max_path(self):
        max=0
        maxi=0
        path=[]
        for i in range(self.N):
            a=self.delte[self.T-1][i]
            if a>max:
                max=a
                maxi=i
        path.append(maxi+1)
        for t in range(self.T-1,0,-1):
            maxi=self.keci[t][maxi]
            path.append(maxi+1)
        for i in range(len(path)-1,-1,-1):
            self.I.append(path[i])
        print(self.I)
A=np.array([[0.5,0.2,0.3],
           [0.3,0.5,0.2],
           [0.2,0.3,0.5]])
B=np.array([[0.5,0.5],
           [0.4,0.6],
           [0.7,0.3]])
PI=np.array([[0.2],
            [0.4],
            [0.4]])
o=['红','白','红']
index={'红':0,'白':1}
hmm=Viterbi(o,A,B,PI,index)
hmm.cal_delte()
hmm.cal_max_path()
t = [(i+1) for i in range(hmm.T)]
s = []
for i in range(hmm.N):
    s.append([i+1]*hmm.T)

for i in range(hmm.T):
    plt.scatter(t,s[i],c='b')
x = [(i+1) for i in range(hmm.T)]
y = [(i+1) for i in range(hmm.N)]
plt.xticks(x)
plt.yticks(y)
plt.xlabel('time')
plt.ylabel('states')
for i in range(hmm.T):
    for j in range(hmm.N):
        plt.annotate(format(hmm.delte[i][j], '.4f'), xy=(t[i],s[j][i]), xytext=(t[i],s[j][i]+0.1))
for i in range(1, hmm.T):
    for j in range(hmm.N):
        dx = t[i]-t[i-1]
        dy = s[j][i] - (hmm.keci[i][j]+1)
        plt.quiver(t[i-1], hmm.keci[i][j]+1, dx, dy, angles='xy', scale=1, scale_units='xy')
plt.show()


