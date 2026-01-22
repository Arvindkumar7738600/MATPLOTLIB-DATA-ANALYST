#plt.bar(x, height, color='color name', width = value, label='label name')

#Vertically Graph
import matplotlib.pyplot as plt
product = ['A','B','C','D']
sales = [1000, 1500, 800, 1220]
plt.bar(product, sales, color= 'orange', label= 'Sales 2025'), plt.xlabel('Product')
plt. ylabel('Sales')
plt. title('Product Sale Comparison')
plt. legend ()
plt.show()

#Horizantally Graph
import matplotlib.pyplot as plt
product = ['A','B','C','D']
sales = [1000, 1500, 800, 1220]
plt.barh(product, sales, color= 'orange', label= 'Sales 2025'), plt.xlabel('Product')
plt. ylabel('Sales')
plt. title('Product Sale Comparison')
plt. legend ()
plt.show()