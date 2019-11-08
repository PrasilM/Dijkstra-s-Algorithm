#################
#  Assignment 5
#  Group Project
#################
import numpy as np
import pandas 
def readcsv(file):
	data  = pandas.read_csv(file)
	return(np.array(data))

Graph_array = readcsv('topology.csv')
print(Graph_array)
