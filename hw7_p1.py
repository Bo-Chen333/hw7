# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:10:44 2018

@author: cb425
"""

import numpy as np
import cv2


#Import DataSet

data = cv2.imread("hendrix_final.png")
data = data.astype(np.float64)
data_re = cv2.resize(data,(500,500))
cv2.imwrite("data_re.png",data_re)

data_r = data_re[:,:,2]
data_g = data_re[:,:,1]
data_b = data_re[:,:,0]

#Function definitions
def GSorthogonalization (data):
    data_treated = np.zeros(data.shape)
    for i in range(data.shape[1]):
        v = data[:,i]
        e = v
        for j in range(i):
            e = e - (np.dot(data_treated[:,j].T,v)/np.dot(data_treated[:,j].T,data_treated[:,j]))*data_treated[:,j]
        data_treated[:,i] = np.array(e)   
    
    return data_treated

    
#Gram-Schmidt orthogonalization

data_final = np.zeros(np.shape(data_re))
data_final[:,:,0] = GSorthogonalization(data_b)
data_final[:,:,1] = GSorthogonalization(data_g)
data_final[:,:,2] = GSorthogonalization(data_r)

cv2.imwrite("data.png",data_final)