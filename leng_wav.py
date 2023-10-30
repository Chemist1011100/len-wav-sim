import matplotlib.pyplot as plt
import numpy as np
from test_w import Waves

le1 = int(input("Длина волны 1 - "))
wave1 = Waves(le1)

le2 = int(input("Длина волны 2 - "))
wave2 = Waves(le2)

ko = (le1+le2)/2
wave3 = Waves(ko)

x = np.arange(-50, 50, 0.01)
y1 = np.sin(x*(le1/100))
y2 = np.sin(x*(le2/100))
y3 = np.sin(x*(ko/100))

plt.plot(x, y1, label=le1, color=wave1.take_col())
plt.plot(x, y2, label=le2, color=wave2.take_col())
plt.plot(x, y3, label=ko, color=wave3.take_col())


# Добавляем систему координат (ось x)
plt.axhline(0, color='black',linewidth=0.5)
# Добавляем систему координат (ось y)
plt.axvline(0, color='black',linewidth=0.5)

# Устанавливаем диапазон по оси x от -5 до 5
plt.xlim(0, 2)
plt.ylim(-1.5, 1.5)

# Добавляем заголовок и подписи к осям
plt.title('Графики световых волн и средней арифметической')
plt.xlabel('x')
plt.ylabel('y')

# Включаем легенду
plt.legend()

# Включаем сетку
plt.grid(True)

# Отображаем график
plt.show()

# y_r = np.sin(x*7.5)
# y_o = np.sin(x*6.2)
# y_y = np.sin(x*5.85)
# y_g = np.sin(x*5.75)
# y_b = np.sin(x*5.1)
# y_c = np.sin(x*4.8)
# y_v = np.sin(x*4.5)
#
# plt.plot(x, y_r, label='red', color='red')
# plt.plot(x, y_o, label='orange', color='orange')
# plt.plot(x, y_y, label='yellow', color='yellow')
# plt.plot(x, y_g, label='green', color='green')
# plt.plot(x, y_b, label='blue', color='blue')
# plt.plot(x, y_c, label='cyan', color='cyan')
# plt.plot(x, y_v, label='violet', color='violet')

