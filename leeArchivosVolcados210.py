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
lonmax=-53
latmin=-44
latmax=-38.5

############################################# 
# MAIN
#############################################
def main():

    dir_folder='/home/kintxo/TIC-MOC/Campanya/BoyasInstrumentadas/300234062218210/'
    #variables del archivo .desc

    fecha=[]
    latIR=[]
    lonIR=[]
    numMsg=[]
    size=[]
    status=[]

    #variables del archivo .sbd
    
    sensor1= []
    temperatura=[]
    humedad=[]
    tension=[]
    tiempoGPS=[]
    latREAL=[]
    lonREAL=[]
    l=[]
    
    

    
#DECLARO UNA VARIABLE DE TIPO DICCIONARIO DONDE VOY A GUARDAR TODOS LOS DATOS


    datos = {}.fromkeys( ['fecha','latIR','lonIR','numMsg','msg_size','status','sensor1','temperatura','humedad','tension','tiempoGPS','latREAL','lonREAL','velocidad','date'] )

     

    for key in datos.keys():  #con este bucle for inicializo el diccionario
        datos[key]=[]
    l=os.listdir(dir_folder)
    l.sort() # esta sentencia ordena los ficheros de entrada de forma que los va leyendo en orden y corresponden las fechas con el orden del fichero, viva Sergio !!!!! ueee
    for infile in l:
        posiciones=infile[0:22]+'.sbd'  # Es el fichero de posiciones y datos .sbd
        detalles=infile[0:22]+'.desc'   # Es el fichero que da los detalles
        #print infile
        if   infile[23:26]=='sbd' :                   #posiciones[0:22] == detalles[0:22]:
        
        
        # LEO LA FECHA DEL FICHERO .desc

            string0="grep  Time  /home/kintxo/TIC-MOC/Campanya/BoyasInstrumentadas/300234062218210/" + detalles + "> out0.txt"
            os.system(string0)
            string1="awk '{print $6,$7,$9,$8 }' out0.txt > out1.txt"
            os.system(string1)
            t=read_date('out1.txt')
            fecha.append(t)
            #print detalles
    
       # LEO LA POSICIÓN DEL FICHERO .desc

            string2="grep  Lat  /home/kintxo/TIC-MOC/Campanya/BoyasInstrumentadas/300234062218210/" + detalles + "> out2.txt"
            os.system(string2)
                                          
            latIRi,lonIRi=read_positionIR('out2.txt')
            latIR.append(latIRi)
            lonIR.append(lonIRi)


      # LEO EL NÚMERO DE MENSAJE DEL FICHERO .desc

            string4="grep  MOMSN  /home/kintxo/TIC-MOC/Campanya/BoyasInstrumentadas/300234062218210/" + detalles + "> out4.txt"
            os.system(string4)
            numi = read_num_msg('out4.txt')
            numMsg.append(numi)

      # LEO EL TAMAÑO DE MENSAJE DEL FICHERO .desc

            string5="grep  Size  /home/kintxo/TIC-MOC/Campanya/BoyasInstrumentadas/300234062218210/" + detalles + "> out5.txt"
            os.system(string5)
            sz = read_size('out5.txt')
            size.append(sz)
         
      # LEO EL STATUS DEl MENSAJE DEL FICHERO .desc

            string6="grep  Status  /home/kintxo/TIC-MOC/Campanya/BoyasInstrumentadas/300234062218210/" + detalles + "> out6.txt"
            os.system(string6)
            stat = read_status('out6.txt')
            status.append(stat)


       # LEO TODOS LOS VALORES  DEL FICHERO .sbd,sensor1,temperatura,HUMEDAD,TENSION,TIEMPOGPS Y POSICIÓN REAL

            
            string7= """tr "," " " <  /home/kintxo/TIC-MOC/Campanya/BoyasInstrumentadas/300234062218210/""" + posiciones +  "> out7.txt" # quita todas las comnas y las cambia por espacios. Si hago este comando para que no deje nada no funciona ["tr "," ""]
            os.system(string7)
            string8= "tr -s ' ' < out7.txt > out8.txt" # que todos los espacios se quedan en une solo espacio
            os.system(string8) # ejecucion


            s1i,s2i,humi,tensi,tgpsi,latREALi,lonREALi=read_valores('out8.txt')

          
            sensor1.append(s1i)
            temperatura.append(s2i)
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



# ESTAS SON LAS VARIABLES QUE ENVÍA LA BOYA'tensionReferencia','sensor1','temperatura''humedad','tension','tiempoGPS','latREAL','lonREAL' 


    
    datos['sensor1']= np.array(sensor1)
    datos['temperatura']= np.array(temperatura)
    datos['humedad']= np.array(humedad)
    datos['tension']= np.array(tension)
    datos['tiempoGPS']= np.array(tiempoGPS)
    datos['latREAL']= np.array(latREAL)
    datos['lonREAL']= np.array(lonREAL)
  
   
    #print max (datos['sensor1'])
    #print min (datos['sensor1'])

    #print max (datos['temperatura'])
    #print min (datos['temperatura'])
    



    # PLOT SSS MAP 
    cmin=0.55 # MIN color
    cmax=0.75 # MAX color
    outputname='figures/SSS-drifters.png'
    

    # PLOT SST MAP  
    cmin=5 # MIN color
    cmax=15 # MAX color
    outputname='figures/SST-drifters.png'
   

##################################################################################################
# Calculo las distancias,los tiempos y las velocidades que es la única variable que guardo
################################################################################################
    

    date=[]
    velocidad=[]
    i=0
    j=0
    k=0
    
    while i < (len(datos['latREAL']))-1:

       
        j=k
        if i==0: 
            while datos['lonREAL'][i] == 'nan' or datos['latREAL'][i] == 'nan' :
                
                i= i+1
            j=i
            
        i=i+1
        while datos['lonREAL'][i] == 'nan' or  datos['latREAL'][i] == 'nan':
           
            i= i+1
        k=i 

       
           

        delta=(datos['fecha'][k]-datos['fecha'][j])        
        ang1,ang2,dist=distT(datos['lonREAL'][j],datos['latREAL'][j],datos['lonREAL'][k],datos['latREAL'][k])
        
        
        fech = datos['fecha'][k]
        vel=dist/delta.seconds
        if vel > 2.5:
            vel = 'nan'
        
        velocidad.append(vel)
        date.append(fech)
        #print 'distancia'
        #print dist
        #print 'velocidad'
        #print vel
        #print '#################### '
                

        i=i+1
    

    
    
    datos['velocidad']= np.array(velocidad)
    datos['date']= np.array(date)
    



################################################################################################
#Ploteo
################################################################################################


    



    plotea_posiciones(datos,outputname,cmin,cmax,'temperatura','Temperatura')
    plotea_posiciones(datos,outputname,cmin,cmax,'sensor1','Tension-Conductividad')

    plot_mensajes(datos)
    plot_tiempogps(datos)
    plot_tension(datos)
    plot_humedad(datos)
    plot_sensor1(datos)
    plot_temperatura(datos)
    plot_velocidades(datos)

    guarda_netCDF4(datos)
    guardo_diccionario(datos)

        
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
    
    #print linea
    
    s=linea.split()

    #print type (linea)
    #if (s[0][0]=='x') | (s[0][0]=='`'):
     #   tmp = 'nan'
    #else:
     #   tensref = np.float(s[0])
    #print tmp

    
    #print len (s)
    s1 = np.float(s[1]) 
    #print cond 

    s2 = 103.34 * (np.float(s[2])) - 281 # esta es la ecuación de regresión que relaciona la tensión con la temperatura

    
    hum = np.int_(s[3])
    #print hum

   
 
    ten = np.int_(s[4])
    #print ten

   

    tgps =np.float(s[5])/1000
    #print tgps

    if len(s)<= 7:

        lonreal='nan'
        latreal='nan'

    else:        
 
        if (len(s[6])<11):
            lonreal='nan'
        else:
            longrados = np.float(s[6][0:3])
            #print longrados
        
            londecimasgrado =(np.float(s[6][3:10]))/60 
            #print londecimasgrado
    
            lonreal = longrados+londecimasgrado
            if s[6][10] == 'W':
                lonreal=-lonreal

        if (len(s[7])<10):
            latreal='nan'
        else:
            #print lonreal 

            latgrados = np.float(s[7][0:2])
            #print latgrados
            latdecimasgrado =np.float(s[7][2:9])/60
    
            #print latdecimasgrado   
            latreal = latgrados+latdecimasgrado
        
            if s[7][9] == 'S':
                latreal=-latreal
        #print latreal
    
    
  
    f.close()
    
    return  s1,s2,hum,ten,tgps,latreal,lonreal 

################################################################################################
#Plotea las posiciones
################################################################################################

def plotea_posiciones(data,outputname,cmin,cmax,var,nombre):


    fig1=figure(facecolor='w',figsize=(10,5))
    ax=plt.gca()


    map1 = Basemap(llcrnrlon=lonmin,urcrnrlon=lonmax,llcrnrlat=latmin, urcrnrlat=latmax, resolution='l',projection='cyl')

    if var=='sensor1':
        t_lab=[0.5,0.525,0.55,0.575,0.6,0.625,0.65,0.675,0.7,0.725,0.75]
        t=[0.5,0.525,0.55,0.575,0.6,0.625,0.65,0.675,0.7,0.725,0.75]
    else:
        # para los ticks de los colores
        t_lab=[5,6,7,8,9,10,11,12,13,14,15]
        t=[5,6,7,8,9,10,11,12,13,14,15]

#0.72414
#0.569279
#13.93515018
#6.05237498


    color_under=([0,0,0.1])
    color_over=([0.4,0.0,0.0])

    # draw continents, paralles and meridians

    meridians_range=np.arange(-180,181,1)
    parallels_range=np.arange(-90,91,1)
    map1.drawmeridians(meridians_range,labels=[1,0,0,1])
    map1.drawparallels(parallels_range,labels=[1,0,0,1])
    map1.drawcoastlines()
    map1.fillcontinents(color=[0.8,0.8,0.8])
    
     
        

    if len(data['lonREAL'])>1: # si el fichero tiene valores validos, len(drifter) > 1 

        pc2=map1.scatter(data['lonREAL'], data['latREAL'], c= data[var], s=20.0, norm = colors.BoundaryNorm(t,ncolors=256, clip = False),edgecolor='none')   
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
        cbar=colorbar(pc2, ticks=t_lab,shrink = 0.6,pad=0.1 ,orientation = 'horizontal', extend = 'both' ) 
        cbar.set_label(var) 
        pc2.cmap.set_over(color_over)
        pc2.cmap.set_under(color_under)
         
    ax.set_aspect('equal')

    for o in fig1.findobj(matplotlib.text.Text):
        o.set_size('15') 
 
    # titulo
    title(nombre,weight='bold',fontsize=15)
    # para mostrar la imagen en el terminal (comentar si se quiere guardar automaticamente)
    plt.show() 

################################################################################################
#Plotea numero mensaje
################################################################################################

def plot_mensajes(data):



    

    fig1=plt.figure('Mensajitos')

    data['numMsg'].sort()
    
   

    plt.plot(data['numMsg'])

    title('mensajes enviados')
    
    plt.show()

################################################################################################
#Plotea la humedad
################################################################################################

def plot_humedad(data):



    

    fig1=plt.figure('Humedad')

    
    plt.plot(data['fecha'],data['humedad'],'.',markersize=5,color=('r'))

    title('Humedad relativa')
    
    plt.show()
################################################################################################
#Plotea la tension
################################################################################################

def plot_tension(data):



    

    fig1=plt.figure('Tension')

    
    plt.plot(data['fecha'],data['tension'],'.',markersize=5,color=('b'))

    title('Valor relativo a la tension ')
   
    plt.show()
################################################################################################
#Plotea el tiempoGPS
################################################################################################

def plot_tiempogps(data):



    

    fig1=plt.figure('tiempoGPS')

    
    plt.plot(data['fecha'],data['tiempoGPS'],'.',markersize=5,color=('g'))

    title('Tiempo de medida GPS en segundos')
   
    plt.show()

################################################################################################
#Plotea el sensor1
################################################################################################

def plot_sensor1(data):



    

    fig1=plt.figure('Tension-Conductividad')

 
    plt.plot(data['fecha'],data['sensor1'],'.',markersize=5,color=('b'))

    title('Conductividad en Tension sin calibrar')
   
    plt.show()
################################################################################################
#Plotea el temperatura
################################################################################################

def plot_temperatura(data):



    

    fig1=plt.figure('Temperatura')

    
    plt.plot(data['fecha'],data['temperatura'],'.',markersize=5,color=('g'))

    title('Temperatura en grados Centigrados')
   
    plt.show()

################################################################################################
#Plotea Velocidades
################################################################################################

def plot_velocidades(data):


    fig1=plt.figure('velocidad')
    a=plt.plot(data['date'],data['velocidad'],'.',markersize=5,color=('b'))
    #a.set_ylim([0,2])
    title('Velocidad en m/s')
    
        
   

    plt.show()
################################################################################################
#Guarda datos en netCDF4
################################################################################################


def guarda_netCDF4(data):

    Nnt=len(data['latREAL'])
    
    wf=Dataset('300234062218210.nc','w',format='NETCDF4')
    Nt=wf.createDimension('Nt',Nnt)
    latitude=wf.createVariable('latitude','f8',('Nt'))
    longitude=wf.createVariable('longitude','f8',('Nt'))
    jday=wf.createVariable('jday','f8',('Nt'))
    
    longitude[:]=data['lonREAL']
    latitude[:]=data['latREAL']
    wf.close()

################################################################################################
#Guarda datos en un fichero legible
################################################################################################

def guardo_diccionario(data):

    fichero = file("300234062218210.dat", "w") 
 
    salida = data 
  
    pickle.dump(salida, fichero)  
  
    fichero.close()  

    

if __name__ == '__main__':				
    main()
