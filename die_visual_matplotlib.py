import matplotlib.pyplot as plt

from die import Die


# create dies (default it is D6)
die1 = Die()
die2 = Die()

rolls = 500_000

# roll the die few times and write the results to list
results = [die1.roll() + die2.roll() for roll_num in range(rolls)]

# analise the results
max_result = die1.num_sides + die2.num_sides 
frequencies = [results.count(value) for value in range(2, max_result+1)]

# visualising the results
fig, ax = plt.subplots()
labels = list(range(2, max_result+1))

ax.bar(labels, frequencies, width=0.35, tick_label=labels)
plt.show()