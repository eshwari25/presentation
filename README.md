# presentation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import numpy as np
def line_dir_pt(m,A):
  len = 1000
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(-15,0,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

xx, yy = np.meshgrid([-20,20], [-20,20])
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')
n1 = np.array([1,-1,1]).reshape((3,1))
c1 = 5
z1 = ((c1-n1[0]*xx-n1[1]*yy)*1.0)/(n1[2])
ax.plot_surface(xx, yy, z1, color='r',alpha=0.2)
A= np.array([1,-5,9]).reshape((3,1))
l1 = np.array([1,1,1]).reshape((3,1))
l1_p = line_dir_pt(l1,A)
l2 = np.array([1,-1,1]).reshape((3,1))
l2_p = line_dir_pt(l2,A)

O= np.array([0,0,0]).reshape((3,1))
P= np.array([-9,-15,-1]).reshape((3,1))
l3_p = line_dir_pt(l1,O)

plt.plot(l3_p[0,:],l3_p[1,:],l3_p[2,:],label="Line L3")
plt.plot(l1_p[0,:],l1_p[1,:],l1_p[2,:],label="Line L1")
plt.plot(l2_p[0,:],l2_p[1,:],l2_p[2,:],label="Line L2")
ax.scatter(A[0],A[1],A[2],'o',label="Point A")
ax.scatter(P[0],P[1],P[2],'o',label="Point P")
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()

plt.show()
