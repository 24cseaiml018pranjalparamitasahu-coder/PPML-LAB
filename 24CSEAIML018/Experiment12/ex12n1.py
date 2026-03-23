import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
plt.plot(x,y)
plt.title("Simple Line plot:")
plt.plot(x,y,linestyle="--",color='r',marker='o',label='dataline')
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid()
plt.show()