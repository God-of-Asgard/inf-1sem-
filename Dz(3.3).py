import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
x = ['Понедельник','Вторник','Среда','Четверг','Пятница','Cуббота','Воскресенье']
y = [100,70,69,52,420,400,239]

plt.bar(x, y, label='Данные из комнаты 303-4' )

plt.xlabel('День недели')
plt.ylabel('Количество кондиций')
plt.title('КОНДИЦИИ')
plt.legend(loc='upper right')
plt.show()
