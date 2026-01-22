import matplotlib.pyplot as plt

x = ['Mon', 'Tue', 'Web', 'Thur', 'Fri', 'Sat']
y = [10, 24, 14, 8, 13, 15]

plt.plot(x, y)

plt.title('Employee sales this week')

plt.xlabel("Day of the week")
plt.ylabel("Employee")

plt.show()