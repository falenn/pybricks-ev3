''' helper mod with report functions'''
import os
from matplotlib import pyplot


def showPath():
    print(os.path)

def plot_results(plot1, plot2):
    pyplot.plot(plot1) 
    pyplot.plot(plot2)
    pyplot.show()