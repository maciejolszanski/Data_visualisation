from calendar import calendar
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import calendar
import numpy as np


def read_dates_and_rains(filename):
    
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, rains = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')

            try:
                rain = float(row[3])
            except ValueError:
                print(f"No data for {current_date} in {filename}!")
            else:
                rains.append(rain)
                dates.append(current_date)
        
        return dates, rains

def sum_rains_monthly(dates, rains):

    rains_in_month = []

    for m in range(1,13):
        rain = 0
        for date in dates:
            if date.month == m:
                rain += rains[dates.index(date)]
        
        rain = rain // 0.001 / 1000
        rains_in_month.append(rain)

    return (rains_in_month)
    
            
if __name__ == '__main__':
    sitka_file = 'data\sitka_weather_2018_simple.csv' 
    d_v_file = 'data\death_valley_2018_simple.csv'

    s_dates, s_rains = read_dates_and_rains(sitka_file)
    d_v_dates, d_v_rains = read_dates_and_rains(d_v_file)

    s_rains_monthly = sum_rains_monthly(s_dates, s_rains)
    d_v_rains_monthly = sum_rains_monthly(d_v_dates, d_v_rains)

    # visualising
    plt.style.use('default')
    labels = calendar.month_name[1:] # 0 is '' so its deleted
    x = np.arange(1,len(labels)+1)
    width = 0.35

    fig, ax = plt.subplots(figsize=(15, 9))
    s_bar = ax.bar(x - width/2, s_rains_monthly, width, label='Sitka')
    d_v_bar = ax.bar(x + width/2, d_v_rains_monthly, width, 
                     label='Death Valley')

    ax.set_title('Opady w roku 2018', fontsize=40)
    ax.set_ylabel('Opady w mm/m^2', fontsize=16)
    ax.set_xlabel('Miesiąc', fontsize=16)
    ax.set_xticks(x,labels)
    # fig.autofmt_xdate()
    ax.legend()

    ax.bar_label(s_bar, padding=3)
    ax.bar_label(d_v_bar, padding=3)

    plt.show()
