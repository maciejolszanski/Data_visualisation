import matplotlib.pyplot as plt

x_values = range(0,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap = plt.cm.plasma)
#ax.plot(x_values,y_values)

ax.set_title('Kwadraty wartości', fontsize=24)
ax.set_xlabel('Wartości', fontsize=12)
ax.set_ylabel("kwadraty", fontsize=12)

ax.tick_params(axis='both', which='major',  labelsize = 10)

ax.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')