# -*- coding: utf-8 -*-
"""Data Manipulation (Custom NumPy Data Type).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cFcAXbk23cR7eWTp8_N-QQKPNTeAWOpi
"""

import numpy as np

# Define a custom data type
data_type = np.dtype([('name', 'U10'), ('age', 'i4'), ('score', 'f4')])

# Create an array with the custom data type
students = np.array([('Aditya', 21, 95.5), ('Bharat', 23, 80.0), ('Siddhant', 18, 80.0)], dtype=data_type)

# Accessing elements
print("Names:", students['name'])
print("Ages:", students['age'])
print("Scores:", students['score'])

