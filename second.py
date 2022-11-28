
from Prior_I_MI import *

Q31=np.array([[1,1/4,9,1],[4,1,3,2],[1/9,1/3,1,3],[1,1/2,1/3,1]])
Q32=np.array([[1,1,1,1/2],[1,1,2,1],[1,1/2,1,9],[2,1,1/9,1]])
Q33=np.array([[1,3,1/3,1/5],[1/3,1,2,1/3],[3,1/2,1,2],[5,3,1/2,1]])
Q34=np.array([[1,1/2,1/5,1/2],[2,1,3,1/3],[5,1/3,1,1/4],[2,3,4,1]])
Q35=np.array([[1,1,5,1],[1,1,1/2,1/2],[1/5,2,1,1/3],[1,2,3,1]])
Q36=np.array([[1,3,1/4,1],[1/3,1,2,1/2],[4,1/2,1,1/4],[1,2,4,1]])
Q37=np.array([[1,2,2,1/7],[1/2,1,3,1/8],[1/2,1/3,1,1/4],[7,8,4,1]])
Q38=np.array([[1,1/2,1/9,1],[2,1,1/4,1],[9,4,1,2],[1,1,1/2,1]])

Q21=np.array([[1,1/4,1/3],[4,1,1],[3,1,1]])
Q22=np.array([[1,1/4,1/4],[4,1,1/2],[4,2,1]])
Q23=np.array([[1,1/2,1/6],[2,1,1/2],[6,2,1]])

Q1=np.array([[1,1,2],[1,1,1/4],[1/2,4,1]])

P31, I31, Im31 = prior(Q31)
P32, I32, Im32 = prior(Q32)
P33, I33, Im33 = prior(Q33)
P34, I34, Im34 = prior(Q34)
P35, I35, Im35 = prior(Q35)
P36, I36, Im36 = prior(Q36)
P37, I37, Im37 = prior(Q37)
P38, I38, Im38 = prior(Q38)

P21, I21, Im21 =prior(Q21)
P23, I23, Im23 =prior(Q23)
P22, I22, Im22 =prior(Q22)

P1, I1, Im1 =prior(Q1)

A1=np.array([[I31],[I32],[I33]])
A2=np.array([[I34],[I35],[I36]])
A3=np.array([[I36],[I37],[I38]])
A1=A1.reshape((3,1))
A2=A2.reshape((3,1))
A3=A3.reshape((3,1))

I=I1+np.dot(P21.T,A1)+np.dot(P22.T,A2)+np.dot(P23.T,A3)

Am1=np.array([[Im31],[Im32],[Im33]])
Am2=np.array([[Im34],[Im35],[Im36]])
Am3=np.array([[Im36],[Im37],[Im38]])
Am1=Am1.reshape((3,1))
Am2=Am2.reshape((3,1))
Am3=Am3.reshape((3,1))

Im=Im1+np.dot(P21,Am1)+np.dot(P22,Am2)+np.dot(P23,Am3)

I0=I/Im

print("I=",I)
print("M(I)=",Im)
print("I0=",I0)
