# Syntax plt.plot(x, y, colour="colour", linestyle='line_style', linewidth='value', marker= 'marker', lable='lable name')

import matplotlib.pyplot as plt

months = [1, 2, 3, 4]
sales = [1000, 2000, 1500, 2200]

plt.plot(months, sales, color ="blue", linestyle = '--', linewidth = 2, marker = 'o', label='2026 Jan Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales Of Month')
plt.title('Monthly Sales Data Report')
plt.legend()
plt.grid(color = 'Gray', linestyle = ':', linewidth =1)
plt.xlim(1,4)
plt.ylim(0, 2500)
plt.xticks([1, 2, 3, 4], ['M1', 'M2', 'M3', 'M4'])
plt.show()