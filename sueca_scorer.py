# UNQ_C1
# GRADED FUNCTION: sigmoid
import numpy as np
import matplotlib.pyplot as plt

import copy
import math



def sigmoid(z):
    """
    Compute the sigmoid of z

    Args:
        z (ndarray): A scalar, numpy array of any size.

    Returns:
        g (ndarray): sigmoid(z), with the same shape as z
         
    """
          
    ### START CODE HERE ### 


    if type(z) != int and type(z) != float: 
        g = np.zeros(len(z))
       
        for i in range(len(z)):
            gtest = 1 / (1 + np.exp(-z[i]))
            g[i]=gtest
    else:
        g = 1 / (1 + np.exp(-z))
        
    ### END SOLUTION ###  
    
    return g


print ("sigmoid([ -1, 0, 1, 2]) = " + str(sigmoid(np.array([-1, 0, 1, 2]))))

# UNIT TESTS
