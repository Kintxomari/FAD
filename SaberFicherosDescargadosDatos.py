#!/usr/bin/env python
# -*- coding: utf-8 -*-
from netCDF4 import * 
from numpy import arange, dtype # array module from http:/
from mpl_toolkits.basemap import Basemap, shiftgrid
from pylab import *
import matplotlib.colors as colors
from optparse import OptionParser
import sys, os, locale
import datetime
import glob
import math, numpy, re, time 
from datetime import datetime as real_datetime 
from datetime import tzinfo, timedelta 

import matplotlib.dates as mdates
import time, calendar 
import matplotlib.cbook as cbook
from matplotlib.dates import YearLocator,DayLocator,MonthLocator,DateFormatter 
from matplotlib.ticker import FuncFormatter, MultipleLocator, FormatStrFormatter
import matplotlib.text as text
import matplotlib.lines as mpllines
from netcdftime import utime
import netcdftime
from mpl_toolkits.axes_grid.inset_locator import inset_axes
from scipy import stats
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import CirclePolygon 
from matplotlib.collections import PatchCollection


import os
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import CirclePolygon 
from matplotlib.collections import PatchCollection
from wgs2utm import *
import pickle

def main():

    dir_folder='/home/kintxo/TIC-MOC/Campanya/BoyasInstrumentadas/300234062219190/'
    #variables del archivo .desc


    numMsg=[]


    #variables del archivo .sbd


    l=os.listdir(dir_folder)
    l.sort() # esta sentencia ordena los ficheros de entrada de forma que los va leyendo en orden y corresponden las fechas con el orden del fichero, viva Sergio !!!!! ueee
    for infile in l:

        if   infile[23:26]=='sbd' :

            num=np.int_(infile[18:22])  # 
            numMsg.append(num)

    plot_mensajes(numMsg)

    
################################################################################################
#Plotea numero mensaje
################################################################################################

def plot_mensajes(data):



    

    fig1=plt.figure('Mensajitos')

    data.sort()
    
   

    plt.plot(data)

    title('mensajes enviados')
    
    plt.show()

if __name__ == '__main__':				
    main()








