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

# AREA en el que dibujamos el mapa
lonmin=-56 
lonmax=-50
latmin=-43.5
latmax=-38.5

############################################# 
# MAIN
#############################################
def main():

    fichero = file("300234062212150.dat")
    data300234062212150 = pickle.load(fichero)
    fichero = file("300234062219190.dat")
    data300234062219190 = pickle.load(fichero)
    fichero = file("300234062219200.dat")
    data300234062219200 = pickle.load(fichero)
    fichero = file("300234062218210.dat")
    data300234062218210 = pickle.load(fichero)
    #wf.variables['longitude'][23]
    wf=Dataset('lonlat.nc','r')

   

    
    

    


  
        
            

  

    
    



   
    
   

    # PLOT SST MAP  
    cmin=3 # MIN color
    cmax=12 # MAX color
    
    





    
################################################################################################
#Ploteo
################################################################################################
    plotea_posiciones(data300234062212150,data300234062219190,data300234062219200,data300234062218210,wf,cmin,cmax,'temperatura','Derivas')
    
    




  
################################################################################################
# FUNCIONES 
################################################################################################


################################################################################################
#Plotea las posiciones
################################################################################################

def plotea_posiciones(data150,data190,data200,data210,posiciones,cmin,cmax,var,nombre):


    fig1=figure(facecolor='w',figsize=(100,100))
    ax=plt.gca()


    map1 = Basemap(llcrnrlon=lonmin,urcrnrlon=lonmax,llcrnrlat=latmin, urcrnrlat=latmax, resolution='l',projection='cyl')

    if var=='temperatura':
        ticks_range1=[1]
        ticks_range2=[20]
        t_lab=np.linspace(cmin,cmax, ((cmax-cmin) * ticks_range1[0]+1) ) 
        t=np.linspace(cmin,cmax, ((cmax-cmin)*ticks_range2[0]+1) )
        t_lab=[3,4,5,6,7,8,9,10,11,12]
    else:
        # para los ticks de los colores
        t_lab=[3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4]
        t=[3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4]

    color_under=([0,0,0.1])
    color_over=([0.4,0.0,0.0])

    # draw continents, paralles and meridians

    meridians_range=np.arange(-180,181,1)
    parallels_range=np.arange(-90,91,1)
    map1.drawmeridians(meridians_range,labels=[1,0,0,1])
    map1.drawparallels(parallels_range,labels=[1,0,0,1])
    map1.drawcoastlines()
    map1.fillcontinents(color=[0.8,0.8,0.8])
    
     
            

    if len(data190['latREAL'])>1: # si el fichero tiene valores validos, len(drifter) > 1 

        pc1=map1.scatter(data190['lonREAL'], data190['latREAL'], c= data190[var], s=30.0, norm = colors.BoundaryNorm(t,ncolors=256, clip = False),edgecolor='none')
        pc2=map1.scatter(data210['lonREAL'], data210['latREAL'], c= data210[var], s=30.0, norm = colors.BoundaryNorm(t,ncolors=256, clip = False),edgecolor='none')  
        pc3=map1.scatter(data200['lonREAL'], data200['latREAL'], c= data200[var], s=30.0, norm = colors.BoundaryNorm(t,ncolors=256, clip = False),edgecolor='none')
        pc4=map1.plot(data150['lonREAL'], data150['latREAL'],'.',markersize=5,color=('k'))


        pc5=map1.plot(posiciones.variables['longitude'][:], posiciones.variables['latitude'][:],'*',markersize=10,color=('y')) 
       
   
        #pc2=map1.plot(data['lonREAL'], data['latREAL'],'.',markersize=5,color=('#228B22'))  
        # estrella en la ultima posicion del drifter
        #pc=map1.plot(data['lon'][len(data['lon'])-1], data['lat'][len(data['lat'])-1],'o',markersize=10,color=('#228B22')) 
        #pc3=map1.plot(data['lon'][1], data['lat'][1],'*',markersize=10,color=('#228B22'))
        #pc4=map1.plot(data['lon'][344], data['lat'][344],'>',markersize=10,color=('#FF4500'))   
        #pc5=map1.plot(data['lon'][217], data['lat'][217],'>',markersize=8,color=('#0000FF'))   
        #pc6=map1.plot(data['lon'][278], data['lat'][278],'>',markersize=8,color=('#0000FF')) 
        #pc7=map1.plot(data['lon'][383], data['lat'][383],'>',markersize=8,color=('#0000FF'))
        #pc8=map1.plot(data['lon'][420], data['lat'][420],'>',markersize=8,color=('#0000FF'))

        #if i==0: # para solo poner una colorbar 
        cbar=colorbar(pc1, ticks=t_lab,shrink = 0.6,pad=0.1 ,orientation = 'horizontal', extend = 'both' ) 
        cbar.set_label(var) 
        pc1.cmap.set_over(color_over)
        pc1.cmap.set_under(color_under)
         
    ax.set_aspect('equal')

    for o in fig1.findobj(matplotlib.text.Text):
        o.set_size('15') 
 
    # titulo
    title(nombre,weight='bold',fontsize=15)
    # para mostrar la imagen en el terminal (comentar si se quiere guardar automaticamente)
    plt.show() 


    

if __name__ == '__main__':				
    main()
