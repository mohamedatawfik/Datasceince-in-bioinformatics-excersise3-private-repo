#### Excersise 3
#### Name : Mohamed Tawfik
#### Matr.-Nr.: 3087942
#################################

import matplotlib.pyplot as plt
import random

# plot 10 randomly selected datapoints with a range between 0 and 10 into a diagram
points = 10
x = [random.uniform(0, 10) for i in range(points)]
y = [random.uniform(0, 10) for i in range(points)]

#  plotthe datapoints as dots
plt.scatter(x, y, label='Random Data', color='blue', marker='o')

# add labels to the x- and y-axis and a title
plt.title('Scatter Plot of Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# save the resulting plot as a png-file
plt.savefig('ten_random_dots_plot.png')
