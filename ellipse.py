import numpy as np
import matplotlib.pyplot as plt
def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.dot(omat,dir_vec(A,B))

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
O=np.array([0,0])
D=np.array([15,0])
C=np.array([0,15])
F=np.array([0,5*np.sqrt(3)])
A=np.array([5,0])
A1=np.array([-5,0])
B=np.array([0,10])
B1=np.array([-0,-10a])
x_OD=line_gen(O,D)
plt.plot(x_OD[0,:],x_OD[1,:],label='$X-AXIS$')
x_OC=line_gen(O,C)
plt.plot(x_OC[0,:],x_OC[1,:],label='$Y-AXIS$')
a=5
b=10
L=(2*(a**2)/b)
P=F+np.array([2.5,0])
Q=F-np.array([2.5,0])
x_PQ=line_gen(P,Q)
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$latus rectum$')
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1-0.1),P[1]*(1+0.2),'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1-0.1),Q[1]*(1+0.2),'Q')
plt.plot(F[0],F[1],'o')
plt.text(F[0]*(1-0.1),F[1]*(1+0.2),'F')
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1-0.1),O[1]*(1+0.2),'O')
plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1-0.1),A[1]*(1+0.2),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1-0.1),B[1]*(1+0.2),'B')
plt.plot(B1[0],B1[1],'o')
plt.text(B1[0]*(1-0.1),B1[1]*(1+0.2),'B1')
plt.plot(A1[0],A1[1],'o')
plt.text(A1[0]*(1-0.1),A1[1]*(1+0.2),'A1')




len=100
t=np.linspace(0,2*np.pi,len)
x=(a)*np.cos(t)
y=(b)*np.sin(t)
plt.plot(x,y)
plt.legend(loc='upper right')
plt.grid()
plt.axis('equal')
print("The length of the latus rectum",L)
plt.show()








