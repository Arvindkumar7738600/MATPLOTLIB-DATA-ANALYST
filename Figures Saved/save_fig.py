# Syntax: savefig('filename.extension', dpi = value, bbox_inches = 'tight')

# dpi means 

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 40]

# Create Plot
plt.plot(x, y, color='red', marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Save figure
plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
# Hamesha plt.show() se phele use kara jata hai plt.savefig()
#dpi ka use report yaaha publish ke liye kiya jata hai.
# bbox_inches ka kaam yeh hai ki side ke border, space, size ko manage karta hai.

plt.show()