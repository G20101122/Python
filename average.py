# -*- coding: utf-8 -*-
# average.py
"""
Created on Mon Jan 25 18:44:37 2021

@author: wangw
"""

import numpy as np
array = np.array([10.46, 10.09, 9.61, 10.23, 10.58, 9.99, 9.19, 10.05, 8.60, 9.76, 10.87, 11.08])
print(array)
print('average number: ', np.mean(array))
print('maximum number: ', np.max(array))
print('minimum number: ', np.min(array))
print('standard deviation: {:.3f}'.format(np.std(array)))
