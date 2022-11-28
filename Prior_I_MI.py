
import numpy as np

def prior(Q):

    X=np.zeros([Q.shape[0]])
    for i in range(Q.shape[0]):
        X[i]=1
        for j in range(Q.shape[1]):
            X[i]*=Q[i][j]

    X=np.sqrt(X)
    S=np.sum(X)
    X=X/S
    X=np.round(X,2)
    #e=np.ones((1,Q.shape[0]))
    #l=np.dot(np.dot(e,Q),X)

    M=np.sum(Q, axis=0)
    l=np.dot(M,X)
    l = np.round(l, 3)
    I = (l - Q.shape[0]) / (Q.shape[0] - 1)
    I = np.round(I, 2)
    if Q.shape[0] <= 2:
        Im = 0
    elif Q.shape[0] == 3:
        Im = 0.58
    elif Q.shape[0] == 4:
        Im = 0.9
    elif Q.shape[0]==5:
        Im=1.12
    elif Q.shape[0]==6:
        Im=1.24
    elif Q.shape[0]==7:
        Im=1.32
    elif Q.shape[0]==8:
        Im=1.41
    elif Q.shape[0]==9:
        Im=1.45
    elif Q.shape[0]==10:
        Im=1.49

    print("Matrix:")
    print(Q)
    print("P:",X)
    print("n", Q.shape[0])
    print("lanbda: ",l)
    print("I(Q):", I)
    print("M(I):", Im)
    print(" ")
    return X, I, Im
