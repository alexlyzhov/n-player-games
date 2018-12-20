
# coding: utf-8

# ## Learning rates and alignment 

# Lets consider Player 1 and Player 2 with the respective loss functions: <br> <br>
# $$ l_1(x, y) = \frac{1}{2}x^2 + 10 xy, \ \ l_2(x, y) = \frac{1}{2}y^2 - 10 xy$$ <br> <br>
# 
# In this game Player 1 controls the variable x and Player 2 controls y respectively. <br> <br>
# 
# The simultaneous gradient is given by:
# 
# $$\xi = (\frac{\delta l_1}{\delta x}, \frac{\delta l_2}{\delta y}) = (x + 10y, y - 10x) $$
# 

# In[56]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

from tqdm import trange


# In[19]:


def g1(x, y):
    return x + 10 * y
def g2(x, y):
    return y - 10 * x


# In[53]:


# GRADIENT DESCENT
x_gd_1 = pd.DataFrame(np.zeros((500, 2)))
x_gd_1.iloc[0, :] = [1.0, 1.0]
for i in range(1, 499):
    x_gd_1.iloc[i, 0] = x_gd_1.iloc[i - 1, 0] - 0.005 * g1(x_gd_1.iloc[i - 1,0], x_gd_1.iloc[i - 1,1])
    x_gd_1.iloc[i, 1] = x_gd_1.iloc[i - 1, 1] - 0.005 * g2(x_gd_1.iloc[i - 1,0], x_gd_1.iloc[i - 1,1])



# In[57]:


plt.scatter(x_gd_1[0], x_gd_1[1])


# In[59]:


# Symplectic GRADIENT DESCENT
x_sgd_1 = pd.DataFrame(np.zeros((500, 2)))
x_sgd_1.iloc[0, :] = [1.0, 1.0]
for i in range(1, 499):
    x_sgd_1.iloc[i, 0] = x_sgd_1.iloc[i - 1, 0] - 0.005 * (
        g1(x_sgd_1.iloc[i - 1,0], x_sgd_1.iloc[i - 1,1]) * (1 - 10)
    )
    x_sgd_1.iloc[i, 1] = x_sgd_1.iloc[i - 1, 1] - 0.005 * (
        g2(x_sgd_1.iloc[i - 1,0], x_sgd_1.iloc[i - 1,1]) * (1 + 10)
    )



# In[60]:


plt.scatter(x_sgd_1[0], x_sgd_1[1])

