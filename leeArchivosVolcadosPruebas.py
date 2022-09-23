#!/usr/bin/env python
# -*- coding: utf-8 -*-
import netCDF4
from numpy import arange, dtype # array module from http:/
#from matplotlib.toolkits.basemap import Basemap, shiftgrid
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

############################################# 
# MAIN
#############################################
def main():

    dir_folder='/home/kintxo/Python/Pruebas'
    #variables del archivo .desc

    fecha=[]
    latIR=[]
    lonIR=[]
    numMsg=[]
    size=[]
    status=[]

    #variables del archivo .sbd
    temperatura= []
    conductividad=[]
    humedad=[]
    tension=[]
    tiempoGPS=[]
    latREAL=[]
    lonREAL=[]

    
    

    
#DECLARO UNA VARIABLE DE TIPO DICCIONARIO DONDE VOY A GUARDAR TODOS LOS DATOS


    datos = {}.fromkeys( ['fecha','latIR','lonIR','numMsg','msg_size','status','temperatura','conductividad','humedad','tension','tiempoGPS','latREAL','lonREAL'] )

#CON ESTE FOR INICIALIZO LA VARIABLE

    for key in datos.keys():
        datos[key]=[]

    for infile in os.listdir(dir_folder):
        posiciones=infile[0:22]+'.sbd'  # Es el fichero de posiciones y datos .sbd
        detalles=infile[0:22]+'.desc'   # Es el fichero que da los detalles
        #print infile[23:25]
        if   infile[23:26]=='sbd' :                   #posiciones[0:22] == detalles[0:22]:
        
        
        # LEO LA FECHA DEL FICHERO .desc

            string0="grep  Time  /home/kintxo/Python/Pruebas/" + detalles + "> out0.txt"
            os.system(string0)
            string1="awk '{print $6,$7,$9,$8 }' out0.txt > out1.txt"
            os.system(string1)
            t=read_date('out1.txt')
            fecha.append(t)
            
    
       # LEO LA POSICIÓN DEL FICHERO .desc

            string2="grep  Lat  /home/kintxo/Python/Pruebas/" + detalles + "> out2.txt"
            os.system(string2)
                                          
            latIRi,lonIRi=read_positionIR('out2.txt')
            latIR.append(latIRi)
            lonIR.append(lonIRi)


      # LEO EL NÚMERO DE MENSAJE DEL FICHERO .desc

            string4="grep  MOMSN  /home/kintxo/Python/Pruebas/" + detalles + "> out4.txt"
            os.system(string4)
            numi = read_num_msg('out4.txt')
            numMsg.append(numi)

      # LEO EL TAMAÑO DE MENSAJE DEL FICHERO .desc

            string5="grep  Size  /home/kintxo/Python/Pruebas/" + detalles + "> out5.txt"
            os.system(string5)
            sz = read_size('out5.txt')
            size.append(sz)
         
      # LEO EL STATUS DEl MENSAJE DEL FICHERO .desc

            string6="grep  Status  /home/kintxo/Python/Pruebas/" + detalles + "> out6.txt"
            os.system(string6)
            stat = read_status('out6.txt')
            status.append(stat)


       # LEO TODOS LOS VALORES  DEL FICHERO .sbd,TEMPERATURA,CONDUCTIVIDAD,HUMEDAD,TENSION,TIEMPOGPS Y POSICIÓN REAL

            
            string7= """tr "," " " <  /home/kintxo/Python/Pruebas/""" + posiciones +  "> out7.txt"
            os.system(string7)
            string8= "tr -s ' ' < out7.txt > out8.txt" # que todos los espacios se quedan en une solo espacio
            os.system(string8) # ejecucion
            tmpi,condi,humi,tensi,tgpsi,latREALi,lonREALi=read_valores('out8.txt')
            
            temperatura.append(tmpi)
            conductividad.append(condi)
            humedad.append(humi)
            tension.append(tensi)
            tiempoGPS.append(tgpsi)
            latREAL.append(latREALi)
            lonREAL.append(lonREALi)
            
            
                              
            

  

    
    


# ESTAS SON LAS VARIABLES QUE LEO DEL FICHERO .DESC

    datos['fecha']= fecha
    datos['latIR']= np.array(latIR)
    datos['lonIR']= np.array(lonIR)
    datos['numMsg']= np.array(numMsg)
    datos['msg_size']= np.array(size)    
    datos['status']= status  



# ESTAS SON LAS VARIABLES QUE ENVÍA LA BOYA'temperatura','conductividad','humedad','tension','tiempoGPS','latREAL','lonREAL' 


    datos['temperatura']= np.array(temperatura)
    datos['conductividad']= np.array(conductividad)
    datos['humedad']= np.array(humedad)
    datos['tension']= np.array(tension)
    datos['tiempoGPS']= np.array(tiempoGPS)
    datos['latREAL']= np.array(latREAL)
    datos['lonREAL']= np.array(lonREAL)
 
    #print datos
    
    
    print datos['status'][0]
    print datos['msg_size'][0]
    print datos['numMsg'][0]	
    print datos['fecha'][0]
    print datos['latIR'][0]
    print datos['lonIR'][0]
    print datos['temperatura'][0]
    print datos['conductividad'][0]
    print datos['humedad'][0]
    print datos['tension'][0]	
    print datos['tiempoGPS'][0]
    print datos['latREAL'][0]
    print datos['lonREAL'][0]
    
    print '  '
    print 'estos son los segundos'
    print '  '
    
   
    

    print datos['status'][1]
    print datos['msg_size'][1]
    print datos['numMsg'][1]   
    print datos['fecha'][1]
    print datos['latIR'][1]
    print datos['lonIR'][1]
    print datos['humedad'][1]
    print datos['temperatura'][1]
    print datos['conductividad'][1]
    print datos['humedad'][1]
    print datos['tension'][1]	
    print datos['tiempoGPS'][1]
    print datos['latREAL'][1]
    print datos['lonREAL'][1]


        
################################################################################################
# FUNCIONES 
################################################################################################

################################################################################################
# read_date lee la fecha del fichero .desc
################################################################################################
def read_date(filename):
    '''
    Reading date on file 
    '''

    FileIn = open(filename,'rb') # apertura fichero
    tit_month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for row in FileIn:
        fecha = str( row.strip().split(';'))

    m=str(fecha[2:5])
    #print fecha
   
    for i in xrange(len(tit_month)):  
        if m == tit_month[i]:
            month= int(i+1)
    if month < 10:
        moisj='0'+str(month)
    else:   
        moisj=str(month)
    day=fecha[6:8]
    #print day
    if day[1] == ' ':
        day = '0'+day[0]
        year=fecha[8:12]
        #print year
        date=str(day)+'/'+str(moisj)+'/'+str(year)
        #print date
        hora=fecha[13:15]
        #print hora
        minu=fecha[16:18]
        #print minu
        seg=fecha[19:21]
        #print seg
        fecha_hora=str(hora)+':'+str(minu)+':'+str(seg)
        date_start=str(date)+' '+str(fecha_hora)
        time=datetime.datetime.strptime(date_start,'%d/%m/%Y %H:%M:%S')
    else:
        year=fecha[9:13]
        #print year
        date=str(day)+'/'+str(moisj)+'/'+str(year)
        #print date
        hora=fecha[14:16]
        #print hora
        minu=fecha[17:19]
        #print minu
        seg=fecha[20:22]
        #print seg
        fecha_hora=str(hora)+':'+str(minu)+':'+str(seg)
        date_start=str(date)+' '+str(fecha_hora)
        time=datetime.datetime.strptime(date_start,'%d/%m/%Y %H:%M:%S')
    
    return time
################################################################################################
# Lee la posición Iridium del fichero .desc
################################################################################################

def read_positionIR(filename):

    f = open(filename,'r')
    linea = f.readline()
    

    if linea[15:18] == 'Lat':
        Lat = np.float(linea[21:28])
        
    if linea[31:35] == 'Long':
        Lon=np.float(linea[37:44])
        
    f.close()
    return Lat,Lon    

################################################################################################
# Lee el número de mensaje enviado del fichero .desc
################################################################################################
    
def read_num_msg(filename):
    
    f=open(filename,'r')
    linea = f.readline()
    pos = np.int_(linea [6:(len(linea)-1)])
  
    
    return pos    

################################################################################################
# Lee el tamaño de mensaje enviado del fichero .desc
################################################################################################
    
def read_size(filename):
    
    f=open(filename,'r')
    linea = f.readline()
    t = np.int_(linea [21:(len(linea)-1)])
  
    
    return t    

################################################################################################
# Lee el status de mensaje enviado del fichero .desc
################################################################################################
    
def read_status(filename):
    
    f=open(filename,'r')
    linea = f.readline()
    sta = linea [16:19]
  
    
    return sta    

################################################################################################
# Lee la posición Real del fichero .sbd
################################################################################################

def read_valores(filename):

    
   
    f = open(filename,'r')
    linea = f.readline()
    
    print linea
    
    s=linea.split()

    #print type (linea)
    tmp = np.float(s[0])
    #print tmp

    

    cond = np.float(s[1]) 
    #print cond 

    
    hum = np.int_(s[2])
    #print hum

   
 
    ten = np.int_(s[3])
    #print ten

   

    tgps =np.float(s[4])/1000
    #print tgps

    longrados = np.float(s[5][0:3])
    #print longrados
    #print linea[j+5:j+12]
    londecimasgrado =(np.float(s[5][3:10]))/60 
    #print londecimasgrado
    #print linea[j+5:j+12]
    lonreal = longrados+londecimasgrado
    if s[5][10] == 'W':
        lonreal=-lonreal
    #print lonreal 

    latgrados = np.float(s[6][0:2])
    #print latgrados
    latdecimasgrado =np.float(s[6][2:9])/60
    #print linea[j+16:j+23]
    #print latdecimasgrado   
    latreal = latgrados+latdecimasgrado
    #print linea[j+23]
    if s[6][9] == 'S':
        latreal=-latreal
    #print latreal
    
  
    f.close()
    
    return  tmp,cond,hum,ten,tgps,latreal,lonreal 


    

if __name__ == '__main__':				
    main()
