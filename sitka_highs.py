import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data\sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # readeing highest temperature
    dates, highs, lows = [], [], []
    for row in reader:
        # temp in Celsius rounded to 0.00
        high = (int(row[5]) - 32)/1.8//0.01/100
        highs.append(high)
        low = (int(row[6]) - 32)/1.8//0.01/100
        lows.append(low)
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

# Visualising
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9))
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Najwyższa temperatura dnia - 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura [C]", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
start_date = datetime.strptime('2018-01-01', '%Y-%m-%d')
final_date = datetime.strptime('2018-12-31', '%Y-%m-%d')
ax.axis([start_date, final_date ,-7, 25])

plt.show()

    
    

