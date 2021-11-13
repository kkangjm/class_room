
import matplotlib.pyplot as plt

# sample data
ratio = [35, 30, 15, 10]
labels = ['Oh_my_girl', 'Black_pink', 'ITZY', 'Aespa']
explode = [0.05, 0.05, 0.05, 0.2]
colors = ['red', 'orange', 'yellow', 'purple']

# pie chart
plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90,
        counterclock=False, explode=explode, shadow=True, colors=colors)
plt.show()
