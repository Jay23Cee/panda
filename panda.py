import pandas as pd
import numpy as np


data = pd.read_csv("Accident.csv", delimiter = ',')
slec =data[['Premise Description','Time Occurred','Victim Age','Area Name']]
print(slec)


#   """ import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import csv

#print('hellow')

#data = pd.read_csv("Accident.csv", delimiter = ',')
#slec =data[['Premise Description','Time Occurred','Victim Age','Area Name']]
#x= slec['Premise Description']
#y= slec['Victim Age']
#width = 1/1.5
#plt.bar(x, y, width, color="blue")


#fig = plt.gcf()
#plotly_fig = tls.mpl_to_plotly(fig)
#py.iplot(plotly_fig, filename='mpl-basic-bar')
#   """
