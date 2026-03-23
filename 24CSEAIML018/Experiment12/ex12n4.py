import matplotlib.pyplot as plt
sizes = [15, 20, 45, 10]
labels = ['a', 'b', 'c', 'd']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0, 0.1, 0) 
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart')
plt.axis("equal") 
plt.show()