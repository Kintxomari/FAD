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
lonmin=-55.5 
lonmax=-50
latmin=-43.5
latmax=-38.5

folder= '/home/kintxo/adjuntos/190Seguriti/'
#folder= '/home/kintxo/adjuntos/pruebas/'

############################################# 
# MAIN
#############################################
def main():

    dir_folder=folder
	
	#dir_folder='/home/kintxo/TIC-MOC/Campanya/BoyasInstrumentadas/300234062219190/'
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


    datos = {}.fromkeys( ['fecha','latIR','lonIR','numMsg','msg_size','status','temperatura','conductividad','humedad','tension','tiempoGPS','latREAL','lonREAL','velocidad','date'] )

#CON ESTE FOR INICIALIZO LA VARIABLE

    for key in datos.keys():
        datos[key]=[]

    l=os.listdir(dir_folder)
    l.sort() # esta sentencia ordena los ficheros de entrada de forma que los va leyendo en orden y corresponden las fechas con el orden del fichero, viva Sergio !!!!! ueee
    for infile in l:

    	posiciones=infile[0:22]+'.sbd'# Es el fichero de posiciones y datos .sbd

	ficheropos = folder+posiciones
        detalles=infile[0:22]+'.desc'# Es el fichero que da los detalle
	
	ficherodet = folder+detalles
	
    	#print infile

        if   infile[23:26]=='sbd' :                   #posiciones[0:22] == detalles[0:22]:
        
        
        # LEO LA FECHA DEL FICHERO .desc

            string0="grep  Time "+ficherodet+ "> out0.txt"
            os.system(string0)
			
            string1="awk '{print $6,$7,$9,$8 }' out0.txt > out1.txt"
            os.system(string1)
            t=read_date('out1.txt')
            fecha.append(t)
            
            
    		
       # LEO LA POSICIÓN DEL FICHERO .desc

            string2="grep  Lat " +ficherodet + "> out2.txt"
            os.system(string2)
                                          
            latIRi,lonIRi=read_positionIR('out2.txt')
            latIR.append(latIRi)
            lonIR.append(lonIRi)


      # LEO EL NÚMERO DE MENSAJE DEL FICHERO .desc

            string4="grep  MOMSN  " + ficherodet + "> out4.txt"
            os.system(string4)
            numi = read_num_msg('out4.txt')
            numMsg.append(numi)
            
      # LEO EL TAMAÑO DE MENSAJE DEL FICHERO .desc

            string5="grep  Size " + ficherodet + "> out5.txt"
            os.system(string5)
            sz = read_size('out5.txt')
            size.append(sz)
         
      # LEO EL STATUS DEl MENSAJE DEL FICHERO .desc

            string6="grep  Status "+ ficherodet + "> out6.txt"
            os.system(string6)
            stat = read_status('out6.txt')
            status.append(stat)


       # LEO TODOS LOS VALORES  DEL FICHERO .sbd,TEMPERATURA,CONDUCTIVIDAD,HUMEDAD,TENSION,TIEMPOGPS Y POSICIÓN REAL

            
            string7= """tr "," " " <  """ + ficheropos +  "> out7.txt" # quita todas las comnas y las cambia por espacios. Si hago este comando para que no deje nada no funciona ["tr "," ""]
            os.system(string7)
            string8= "tr -s ' ' <out7.txt > out8.txt" # que todos los espacios se quedan en une solo espacio
            os.system(string8) # ejecucion


            tmpi,condi,humi,tensi,tgpsi,latREALi,lonREALi=read_valores('out8.txt')

            #print 'Fecha= ',t,'Mensaje= ',numi,'lat= ', latREALi,'long= ', latREALi

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
   
    #plotea_posiciones(datos)

    # PLOT SSS MAP 
    cmin=3 # MIN color
    cmax=4 # MAX color
    outputname='figures/SSS-drifters.png'
   

    # PLOT SST MAP  
    cmin=3 # MIN color
    cmax=12 # MAX color
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

        #print datos['numMsg'][i]
        j=k
        if i==0: 
            while datos['lonREAL'][i] == 'nan' or datos['latREAL'][i] == 'nan' :
                
                i= i+1
                #print i
            j=i
           
        i=i+1
        while datos['lonREAL'][i] == 'nan' or  datos['latREAL'][i] == 'nan':
            i= i+1
        k=i 

       
           
        
        delta=(datos['fecha'][k]-datos['fecha'][j])        
        ang1,ang2,dist=distT(datos['lonREAL'][j],datos['latREAL'][j],datos['lonREAL'][k],datos['latREAL'][k])
        #print 'i=', i,'j=',j,'k=', k,'la fecha k=',datos['fecha'][k],'la fecha j=',datos['fecha'][j],'el num mens k =',datos['numMsg'][k],'el num mens j =',datos['numMsg'][j]
        
        fech = datos['fecha'][k]
        vel=dist/delta.seconds
        
            
        velocidad.append(vel)
        date.append(fech)
        #print 'distancia'
        #print dist
        #print 'velocidad'
        #print vel
        #print '#################### '
                
        #print datos['numMsg'][i]
        i=i+1
    

    
    
    datos['velocidad']= np.array(velocidad)
    datos['date']= np.array(date)
    
################################################################################################
#Ploteo
################################################################################################
    #plotea_posiciones(datos,outputname,cmin,cmax,'conductividad','Conductividad')
    #plotea_posiciones(datos,outputname,cmin,cmax,'temperatura','Temperatura')

    plot_mensajes(datos)
    plot_tiempogps(datos)
    plot_tension(datos)
    plot_humedad(datos)

    plot_temperatura(datos)
    plot_conductividad(datos)

    plot_velocidades(datos)

    guarda_netCDF4(datos)
    guardo_diccionario(datos)

    #print ' ################################'
    #print '   '


  
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
        #print time
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
    #print pos
    
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
    linea = filtralinea(linea)
    s=linea.split()
    
    #print len(s)
    if len(s)<4:
        tmp = 'nan'  #tmp,cond,hum,ten,tgps,latreal,lonreal
        cond = 'nan'
        hum = 'nan'
        ten = 'nan'
        tgps = 'nan'
        latreal = 'nan'
        lonreal = 'nan'
    elif len(s)==7:

#print type (linea)
        if (s[0][0]=='x') | (s[0][0]=='`')| (s[0][0]=='|')| (s[0][0]=='')| (s[0][0]=='~')| (s[0][0]=='v')| (s[0][0]=='q')| (s[0][0]==''):
            tmp = 'nan'
        else:
            tmp = np.float(s[0])
    #print tmp
        if (s[1][0]=='x') | (s[1][0]=='`')| (s[1][0]=='|')| (s[1][0]=='')| (s[1][0]=='~')| (s[1][0]=='v'):
            cond = 'nan'
        else:
            cond = np.float(s[1]) 
    #print type (linea)
        

        
    #print cond 

    
        hum = np.int_(s[len(s)-5])
    #print hum

   
 
        ten = np.int_(s[len(s)-4])
    #print ten

   
        
        #print s[len(s)-1],s[len(s)-2],s[len(s)-3],s[len(s)-4],s[len(s)-5]


        tgps =np.float(s[len(s)-3])/1000
        
        if (len(s[len(s)-2])<11):
            lonreal='nan'
        else:
            longrados = np.float(s[len(s)-2][0:3])
        #print longrados
        
            londecimasgrado =(np.float(s[len(s)-2][3:10]))/60 
        #print londecimasgrado
    
            lonreal = longrados+londecimasgrado
            if s[len(s)-2][10] == 'W':
                lonreal=-lonreal
        if (len(s[len(s)-1])<10):
            latreal='nan'
        else:
        #print lonreal 

            latgrados = np.float(s[len(s)-1][0:2])
        #print latgrados
            latdecimasgrado =np.float(s[len(s)-1][2:9])/60
    
        #print latdecimasgrado   
            latreal = latgrados+latdecimasgrado
        
            if s[len(s)-1][9] == 'S':
                latreal=-latreal
        #print latreal
        #print 'temperatura:',tmp,'conductividad:',cond,'humedad:',hum,'tension:',ten,'tiempo_gps:',tgps,'latitud:',latreal,'longitud:',lonreal
    else:
        tmp = 'nan'  
        cond = 'nan'
        hum = 'nan'
        ten = 'nan'
        tgps = 'nan'
        latreal = 'nan'
        lonreal = 'nan'
        #print linea,len(s)
    if cond > 6:
        print linea,'la conductividad es =',cond,len(s)
  
    f.close()
    
    return  tmp,cond,hum,ten,tgps,latreal,lonreal
################################################################################################
#Filtra el ruido de la linea
################################################################################################

def filtralinea(s):
    
    

    return s

	



	

################################################################################################
#Plotea las posiciones
################################################################################################

def plotea_posiciones(data,outputname,cmin,cmax,var,nombre):


    fig1=figure(facecolor='w',figsize=(10,5))
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
    
    
        

    if len(data['lonREAL'])>1: # si el fichero tiene valores validos, len(drifter) > 1 

        pc2=map1.scatter(data['lonREAL'], data['latREAL'], c= data[var], s=20.0, norm = colors.BoundaryNorm(t,ncolors=256, clip = False),edgecolor='none')   
        pc2=map1.plot(data['lonREAL'], data['latREAL'],'.',markersize=5,color=('#228B22'))  
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
#Plotea la temperatura
################################################################################################

def plot_temperatura(data):



    

    fig1=plt.figure('temperatura')

    

    plt.plot(data['fecha'],data['temperatura'],'.',markersize=5,color=('b'))

    title('Temperatura en grados Centigrados')
   
    plt.show()
################################################################################################
#Plotea la conductividad
################################################################################################

def plot_conductividad(data):



    

    fig1=plt.figure('conductividad')

    

    plt.plot(data['fecha'],data['conductividad'],'.',markersize=5,color=('g'))

    title('Conductividad en Siemens por metro')
   
    plt.show()

################################################################################################
#Plotea Velocidades
################################################################################################

def plot_velocidades(data):


    fig1=plt.figure('velocidad')
    plt.plot(data['date'],data['velocidad'],'.',markersize=5,color=('r'))
    title('Velocidad en m/s')
    
        
   

    plt.show()
################################################################################################
#Guarda datos en netCDF4
################################################################################################


def guarda_netCDF4(data):

    Nnt=len(data['latREAL'])
    #print len(data['latREAL'])
    wf=Dataset('300234062219190.nc','w',format='NETCDF4')
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

    fichero = file("300234062219190.dat", "w") 
 
    salida = data 
  
    pickle.dump(salida, fichero)  
  
    fichero.close()  

    

if __name__ == '__main__':				
    main()
