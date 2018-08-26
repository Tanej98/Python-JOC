# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:37:34 2018

@author: KATA_TANEJ_KUMAR
"""

import matplotlib.pyplot as plt
import statistics
estimate=[1,2,3,4,5,6,7,8,9,10,15,13,16,18,20,25,55,203,54,1,64,3062,620,650,650,2,6,2,320,60,32,20,320,32,3,32,60]
estimate.sort()
mean=statistics.mean(estimate)
y=[5]*len(estimate)
print('mean :',mean)
plt.plot(estimate,y,'ro')
plt.plot(mean,5,'bs')    
