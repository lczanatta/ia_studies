#Data processing 

#Import the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the datasets

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values