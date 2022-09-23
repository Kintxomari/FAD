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

##########è################################################################
# Globals
###########################################################################



folder= '/home/kintxo/adjuntos/190Seguriti/'
#folder= '/home/kintxo/adjuntos/pruebas/'


############################################# 
# MAIN
#############################################
def main():

    dir_folder=folder
    l=os.listdir(dir_folder)
    l.sort() # esta sentencia ordena los ficheros de entrada de forma que los va leyendo en orden y corresponden las fechas con el orden del fichero, viva Sergio !!!!! ueee
    for infile in l:
        posiciones=infile[0:22]+'.sbd'
        ficheropos = folder+posiciones
        detalles=infile[0:22]+'.desc'
        ficherodet = folder+detalles
        #print infile
        if   infile[23:26]=='sbd' :

            string7= """tr "," " " <  """ + ficheropos +  "> out7.txt" # quita todas las comnas y las cambia por espacios. Si hago este comando para que no deje nada no funciona ["tr "," ""]
            os.system(string7)
            string8= "tr -s ' ' <out7.txt > out8.txt" # que todos los espacios se quedan en une solo espacio
            os.system(string8) # ejecucion


            f = open('out8.txt','r')
            linea = f.readline()
            s=linea.split()
            print linea,len(s)

if __name__ == '__main__':				
    main()




