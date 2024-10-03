import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
amount = [30, 1, 66, 3, 0]
labels = ["Миша взял БАЗЗА", "Макар выбирает персонажа не последним", "Артем взял вольта", "Игра на плохих картах", "В команде противника умеют играть"]
color_ = ["red", "violet", "blue", "pink", "purple"]

plt.pie(amount, labels=labels,colors=color_ , autopct='%1.f%%')
plt.title("Вероятность побед в мультиплеерной игре 'Brawl stars' ")
plt.show()
