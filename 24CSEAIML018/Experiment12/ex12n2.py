import matplotlib.pyplot as plt
categories=['A','B','C','D']
values=[3,7,8,15]
plt.plot(categories,values)
plt.title("bar plot:")
plt.plot(categories,values,color='g',label='bar plot')
plt.xlabel("Categories")
plt.ylabel("values")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5,7,6,8,7]
plt.plot(x,y)
plt.title("scatter plot:")
plt.plot(x,y,color='b',label='scatterpoints')
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()

