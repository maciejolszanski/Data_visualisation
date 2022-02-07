import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Define plot title and axes labels
ax.set_title('Kwadraty liczby', fontsize=24)
ax.set_xlabel('Liczby', fontsize=14)
ax.set_ylabel('Kwadraty', fontsize=14)

# Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', labelsize=14)

plt.show()