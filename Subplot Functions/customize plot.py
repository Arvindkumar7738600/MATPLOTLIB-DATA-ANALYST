from turtle import color
import matplotlib.pyplot as plt
#fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))

fig, ax = plt.subplots(1,2, figsize = (10,5))

x = [1,2,3,4]
y = [10,20,15,25]

ax [0]. plot (x, y)
ax [0]. set_title( 'Line Plot')
ax [1]. bar (x,y, color='Red')
ax [1]. set_title('Bar Chart')

fig.suptitle('Comprasion of Line and Bar charts')

plt.tight_layout()
plt.show()