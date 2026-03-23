import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3d
fig=plt.figure
ax=fig.add_subplot(111,projection='3d')
x=[1,2,3,4,5]
y=[5,6,7,8,9]
z=[2,3,3,3,2]
ax.scatter(x,y,z,color='r',label="3d points")
ax.set_title("3d scatter plot")
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")
plt.legend()
plt.show()