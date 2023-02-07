#!/usr/bin/env python
# coding: utf-8

# In[100]:


import matplotlib.pyplot as plt
import numpy as np
import random
import math

from scipy.optimize import fsolve
from scipy.optimize import golden
from scipy.optimize import root

import sympy
from  sympy.abc import *


# In[2]:


# f(x) = -12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30


# In[3]:


def func(x):
    return -12*(x**4)*np.sin(np.cos(x)) - 18*(x**3) + 5*(x**2) + 10*x - 30


# In[4]:


x = np.arange(-100, 100, 0.01)


# In[5]:


# сетка
plt.grid(True)

# оси координат
ax = plt.gca()
plt.rcParams['lines.linestyle'] = '-'

# plot X - axis
ax.axhline(y=0, color='k', linewidth=0.5)

# plot Y - axis
ax.axvline(x=0, color='k', linewidth=0.5)

# график
plt.rcParams['lines.linestyle'] = '-'
# plt.plot(x, func(x), 'r')

plt.plot(x, func(x), 'g')




# Заголовок
plt.title(r'$f(x) = -12*x^4*sin(cos(x)) - 18*x^3 + 5*x^2 + 10*x - 30$', fontsize=16, fontname='Times New Roman')

# Название осей
plt.xlabel('Ось X')
plt.ylabel('Ось Y')


# отображение в IDE
plt.show()


# In[172]:


# Возьмем участок функции
x = np.arange(-2, 3, 0.01)


# In[173]:


def func_min(x):
    return -12*(x**4)*np.sin(np.cos(x)) - 18*(x**3) + 5*(x**2) + 10*x - 30 + 74.10623434395414


# In[174]:


x1 = fsolve(func, -1)
x2 = fsolve(func, 2) 
min_y_1_2 = min(func(x))
min_f = golden(func, brack=(1, 2), full_output=True)
print(min_f)


# In[175]:


min_f1 = golden(func, brack=(-2, -1), full_output=True)
print(min_f1)


# In[183]:


def func_max(x):
    return -12*(x**4)*np.sin(np.cos(x)) - 18*(x**3) + 5*(x**2) + 10*x - 30 + 26.512722365415843


# In[184]:


x_find_max = np.arange(0, 1, 0.00001)
max_y_0_1 = max(func(x_find_max))
print(max_y_0_1)

max_x_0_1 = fsolve(func_max, 0)
print(max_x_0_1)


# In[197]:


pos_down = np.arange(-2, x1, 0.01)
pos_up = np.arange(x2, 3, 0.01)
neg_down1 = np.arange(x1, min_f1[0], 0.01)
neg_down2 = np.arange(max_x_0_1[0], min_f[0], 0.01)
neg_up1 = np.arange(min_f1[0], max_x_0_1[0], 0.01)
neg_up2 = np.arange(min_f[0], x2, 0.01)
x = np.arange(-2, 3, 0.01)
# сетка
plt.grid(True)

# оси координат
ax = plt.gca()
plt.rcParams['lines.linestyle'] = '-'

# plot X - axis 
ax.axhline(y=0, color='k', linewidth=0.5)

# plot Y - axis    
ax.axvline(x=0, color='k', linewidth=0.5)

# график
plt.rcParams['lines.linestyle'] = '-'
# plt.plot(x, func(x), 'r')

# корни
plt.plot(x1, 0, 'ro', label=f'корень 1 {x1}')
plt.plot(x2, 0, 'ro', label=f'корень 2 {x2}')

# минимумы/максимумы
plt.plot(min_f[0], min_f[1], 'yx', label=f'мин на участке 1 - 2 ({min_f[0]}, {min_f[1]})')
plt.plot(min_f1[0], min_f1[1], 'bx', label=f'мин на участке -1 - 0 ({min_f1[0]}, {min_f1[1]})')
plt.plot(max_x_0_1[0], max_y_0_1, 'rx', label=f'макс на участке 0 - 1 ({max_x_0_1[0]}, {max_y_0_1})')

# f>0
plt.rcParams['lines.linestyle'] = '-'
plt.plot(pos_down, func(pos_down), 'g', label='убывает > 0')
plt.plot(pos_up, func(pos_up), 'y', label='возрастает > 0')

# # f<0
plt.rcParams['lines.linestyle'] = '-.'
plt.plot(neg_down1, func(neg_down1), 'g', label='убывает < 0')
plt.plot(neg_down2, func(neg_down2), 'g')
plt.plot(neg_up1, func(neg_up1), 'y', label='возрастает < 0')
plt.plot(neg_up2, func(neg_up2), 'y')

# Заголовок
plt.title(r'$f(x) = -12*x^4*sin(cos(x)) - 18*x^3 + 5*x^2 + 10*x - 30$', fontsize=12, fontname='Times New Roman')

# Название осей
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# легенда
legend_obj = plt.legend()
legend_obj.set_draggable(True)
plt.show()


# In[ ]:




