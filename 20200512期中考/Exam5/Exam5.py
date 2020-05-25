# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:11:02 2020

@author: ASUS
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles
import pandas as pd
data = pd.read_csv('grade.csv')
set1 = data.Programming
set2 = data.Economics
set3 = data.Calculus
