#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import netCDF4
#from numpy import arange, dtype # array module from http:/
#from matplotlib.toolkits.basemap import Basemap, shiftgrid
#from mpl_toolkits.basemap import Basemap, shiftgrid
#from pylab import *
#import matplotlib.colors as colors
#from optparse import OptionParser
#import sys, os, locale
#import datetime
#import glob
#import math, numpy, re, time 
#from datetime import datetime as real_datetime 
#from datetime import tzinfo, timedelta 

#import matplotlib.dates as mdates
#import time, calendar 
#import matplotlib.cbook as cbook
#from matplotlib.dates import YearLocator,DayLocator,MonthLocator,DateFormatter 
#from matplotlib.ticker import FuncFormatter, MultipleLocator, FormatStrFormatter
#import matplotlib.text as text
#import matplotlib.lines as mpllines
#from netcdftime import utime
#import netcdftime
#from mpl_toolkits.axes_grid.inset_locator import inset_axes
#from scipy import stats
#import numpy as np
#import matplotlib
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#from mpl_toolkits.basemap import Basemap
#from matplotlib.patches import CirclePolygon 
#from matplotlib.collections import PatchCollection


import os
import math
import numpy as np
#import matplotlib
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#from mpl_toolkits.basemap import Basemap
#from matplotlib.patches import CirclePolygon 
#from matplotlib.collections import PatchCollection

############################################# 
# MAIN
#############################################
def main():

    dir_folder='/home/kintxo/Python/Pruebas'
    
    

    for infile1 in os.listdir(dir_folder):
        posiciones=infile1[0:22]+'.sbd'  # Es el fichero de posiciones y datos .sbd
        detalles=infile1[0:22]+'.desc'   # Es el fichero que da los detalles
        if infile1 == posiciones:
             for infile2 in os.listdir(dir_folder):
                
                if (infile1[0:22] == infile2[0:22]) and (infile1[23:25]!=infile2[23:25]):

                                       
                    os.system("cat /home/kintxo/Python/Pruebas/" + infile1 + ">> /home/kintxo/Python/Pruebas/" + infile2)
                    string3="""tr "\n" " " < /home/kintxo/Python/Pruebas/"""+  infile2 + "> Salida-"""+infile1[0:22]  #Saltos por 
                    os.system(string3)
                    
           
        
        
        

        

    

if __name__ == '__main__':
    main()
