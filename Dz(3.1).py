import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
x = [0, 20, 70, 90, 120]
y = [20, 70, 120, 50, 20]
plt.plot(x, y)
ax = plt.gca()
ax.set_xlim(1, 120)
ax.set_ylim(0, 120)
plt.xlabel('t,c')
plt.ylabel('F,Н')
ax.set_xticks([10, 20, 30, 40,50,60,70,80,90,100])
ax.set_yticks([0, 10, 20, 30, 40, 50, 60,70,80,90,100,110,120])

ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

ax.xaxis.set_minor_formatter(ticker.FormatStrFormatter('%g'))
ax.yaxis.set_minor_formatter(ticker.FormatStrFormatter('%g'))
plt.grid(True)
plt.show()
