# INTERFAZ GRÁFICA GENERAL, programa en curso

##### IMPORTACIÓN DE LIBRERÍAS  #############
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import functools

###### LECTURA DE ARCHIVOS DE DATOS #####3
datos=pd.read_csv('Datos2.csv',header=10, delimiter= ";")
dts=pd.read_csv('Datos2.csv', header =1022, delimiter= ";")



##### DEFINICION DE TODAS LAS VARIABLES GLOBALES
######## --------->>>>>> DEFINICION DE LISTAS <<<<<<<<<<------------- #############
# lista de fechas
fecha=datos['Time']
fechas=fecha[0:1009]
fechas10 = []

for i in range (0, 1008, 25):
    fechas10.append(fechas[i])

#definiciÃ³n de las listas de nombres de titulos de los armÃ³nicos
armFaseA=['Phase A-N V-Harmonic 2nd', 'Phase A-N V-Harmonic 3rd',	'Phase A-N V-Harmonic 4th',	'Phase A-N V-Harmonic 5th',	'Phase A-N V-Harmonic 6th',	'Phase A-N V-Harmonic 7th',	'Phase A-N V-Harmonic 8th',	'Phase A-N V-Harmonic 9th',	'Phase A-N V-Harmonic 10th',	'Phase A-N V-Harmonic 11th',	'Phase A-N V-Harmonic 12th',	'Phase A-N V-Harmonic 13th',	'Phase A-N V-Harmonic 14th',	'Phase A-N V-Harmonic 15th',	'Phase A-N V-Harmonic 16th',	'Phase A-N V-Harmonic 17th',	'Phase A-N V-Harmonic 18th',	'Phase A-N V-Harmonic 19th',	'Phase A-N V-Harmonic 20th'
]
armFaseB=['Phase B-N V-Harmonic 2nd',	'Phase B-N V-Harmonic 3rd',	'Phase B-N V-Harmonic 4th',	'Phase B-N V-Harmonic 5th',	'Phase B-N V-Harmonic 6th',	'Phase B-N V-Harmonic 7th',	'Phase B-N V-Harmonic 8th',	'Phase B-N V-Harmonic 9th',	'Phase B-N V-Harmonic 10th',	'Phase B-N V-Harmonic 11th',	'Phase B-N V-Harmonic 12th',	'Phase B-N V-Harmonic 13th',	'Phase B-N V-Harmonic 14th',	'Phase B-N V-Harmonic 15th',	'Phase B-N V-Harmonic 16th',	'Phase B-N V-Harmonic 17th',	'Phase B-N V-Harmonic 18th',	'Phase B-N V-Harmonic 19th',	'Phase B-N V-Harmonic 20th'
]
armFaseC=['Phase C-N V-Harmonic 2nd',	'Phase C-N V-Harmonic 3rd',	'Phase C-N V-Harmonic 4th',	'Phase C-N V-Harmonic 5th',	'Phase C-N V-Harmonic 6th',	'Phase C-N V-Harmonic 7th',	'Phase C-N V-Harmonic 8th',	'Phase C-N V-Harmonic 9th',	'Phase C-N V-Harmonic 10th',	'Phase C-N V-Harmonic 11th',	'Phase C-N V-Harmonic 12th',	'Phase C-N V-Harmonic 13th',	'Phase C-N V-Harmonic 14th',	'Phase C-N V-Harmonic 15th',	'Phase C-N V-Harmonic 16th',	'Phase C-N V-Harmonic 17th',	'Phase C-N V-Harmonic 18th',	'Phase C-N V-Harmonic 19th',	'Phase C-N V-Harmonic 20th'
]

armonicos = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
#listas para nombres de tutulos de tensiones

nombresTensiones=['Phase A-N Avg Volts', 'Phase B-N Avg Volts', 'Phase C-N Avg Volts']
VmedA=[]
VmedB=[]
VmedC=[]

##lista para nombres de la duración de eventos y su porcentaje respecto a la tensión ideal
nombresDuraciones=["Phase A-N Duration (secs)", "Phase B-N Duration (secs)", "Phase C-N Duration (secs)"]
nombresUmbrales=['Phase A-N Threshold (V)', 'Phase B-N Threshold (V)', 'Phase C-N Threshold (V)']
VporcA=[]
VporcB=[]
VporcC=[]
DA = []
DB = []
DC = []

##definiciÃ³n de listas donde se guardan los promedios de los armÃ³nicos
# en donde la posiciÃ³n 0 tiene el promedio del 2nd arm, la 1 la del 3dr...

promArmA=[]
promArmB=[]
promArmC=[]

#Se definen las listas para los valores de thd en las tensiones para cada fase
nombresTHD=['Phase A-N Voltage THD', 'Phase B-N Voltage THD', 'Phase C-N Voltage THD']
THDA=[]
THDB=[]
THDC=[]

#### listas para histograma
clases = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #lista con las clases
porcfaseA = []
porcfaseB = []
porcfaseC = []



################     DEFINICION DE FUNCIONES GLOBALES    ##############################

# funciÃ³n para grÃ¡fica de armÃ³nicos
#funciÃ³n que convierte las listas de strings en listas de floats y delimita a 1010 nÃºmeros
def convertidor(nombre): #le entra el nombre de la columna
    listas=datos[nombre] #genera una lista que tiene todos los datos de la columna
    lista=[] #aquÃ­ se guarda la lista solo con los datos necesarios y en convertidos a floats 
    
    for i in range(0, 1009): #contador de 0 a 1009
        viejo=listas[i] #asigna a viejo el string con el % a cada dato de la columna
        numero=float(viejo[:-1]) #quita % del string para convertirlo a float
        lista.append(numero) #aÃ±ade el elemento a lista
    promedio = sum(lista)/len(lista) # genera el promedio de la lista
    return (promedio) #asigna el promedio a la salida

#funciÃ³n para convertir una lista de strings a floats
def cambiar(nombre):
    listas=datos[nombre] #genera una lista que tiene todos los datos de la columna
    lista=[] #aquÃ­ se guarda la lista solo con los datos necesarios y en convertidos a floats 
    
    for i in range(0, 1009): #contador de 0 a 1009
        numero=float(listas[i]) #quita % del string para convertirlo a float
        lista.append(numero) #aÃ±ade el elemento a lista
    return (lista) #devuelve una lista con floats

#Función que devuelve el numero de valores de tension que se encuentran
#en el rango permitido
def enRango(lista):
    cont=0 #contador de valores dentro de rango
    for i in range(0,1009):
        if (126>=lista[i]>=114):
            cont=cont+1
    return cont

#Función que devuelve el numero de valores de tension que se encuentran
#fuera del rango tolerable y fallos por consecutivos
def detectorCons(lista):
    contFuera=0 #contador fuera de rango tolerable
    contCons=0 #contador de fallos consecutivos
    falla=0 #booleana que indica si falla o no
    for i in range(0,1009):
        if ((127<lista[i] or lista[i]<110) and contCons==0):
            contFuera=contFuera+1
            if ((lista[i]<=104.4 or lista[i]>=135.6)):
                 contCons=contCons+1
        elif ((127<lista[i] or lista[i]<110) and contCons!=0):
            contFuera=contFuera+1
            if ((lista[i]<=104.4 or lista[i]>=135.6)):
                falla=1
        elif (127>=lista[i]>=110 and contCons==0):
            contCons=0
    return falla,contFuera
            
def porcentajesTablaVol(lista):   #
    l=len(lista)
    porcDentro=(enRango(lista)/l)*100
    falla,numFuera=detectorCons(lista)
    porcFuera=(numFuera/l)*100
    return porcDentro,porcFuera,falla

VmedA=cambiar(nombresTensiones[0])
VmedB=cambiar(nombresTensiones[1])
VmedC=cambiar(nombresTensiones[2])

## funciones para THD. Intervalos de distorsion armonica total dentro de rango
#funcion que recibe una columna con datos con % y devuelve la misma columna sin %
def cambiarModif(nombre): #le entra el nombre de la columna
    listas=datos[nombre] #genera una lista que tiene todos los datos de la columna
    lista=[] #aquÃ­ se guarda la lista solo con los datos necesarios y en convertidos a floats 
    
    for i in range(0, 1009): #contador de 0 a 1009
        viejo=listas[i] #asigna a viejo el string con el % a cada dato de la columna
        numero=float(viejo[:-1]) #quita % del string para convertirlo a float
        lista.append(numero) #aÃ±ade el elemento a lista
    return (lista) #devuelve la columna sin el %

#Función que devuelve el numero de valores de tension que se encuentran
#en el rango permitido
def dentroTHD(lista):
    cont=0 #contador de valores dentro de rango
    for i in range(0,1009):
        if (lista[i]<=5):
            cont=cont+1
    return cont

#Función que devuelve el numero de valores de THD que se encuentran
#fuera del rango tolerable
def fueraTHD(lista):
    contFuera=0 #contador fuera de rango tolerable
    for i in range(0,1009):
        if (lista[i]>5):
            contFuera=contFuera+1
    return contFuera
            
def porcentajesTablaTHD(lista):
    l=len(lista)
    porcDentro=(dentroTHD(lista)/l)*100
    numFuera=fueraTHD(lista)
    porcFuera=(numFuera/l)*100
    return porcDentro,porcFuera

#funcion para sacar los porcemtajes
def porcentaje(fase):
    porc = []
    for j in range(len(fase)):
        po = (fase[j]/120)*100
        porc.append(po)
    return(porc)

def cambiarF47(nombre):
    listas=dts[nombre] #genera una lista que tiene todos los datos de la columna
    lista=[] #aquí se guarda la lista solo con los datos necesarios y en convertidos a floats 
    
    for i in range(0, 13): #contador de 0 a 1009
        numero=float(listas[i]) #quita % del string para convertirlo a float
        lista.append(numero) #añade el elemento a lista
    return (lista) #asigna el promedio a la salida

    
################# funciones para la gráfica de promedios diarios de tension   ########

def cambiarStr(nombre):
    listas=datos[nombre] #genera una lista que tiene todos los datos de la columna
    lista=[] #aquí se guarda la lista solo con los datos necesarios y en convertidos a floats 
    
    for i in range(0, 1009): #contador de 0 a 1009
        numero=listas[i] #quita % del string para convertirlo a float
        lista.append(numero) #añade el elemento a lista
    return (lista) #devuelve la lista con floats

#Función que toma 3 listas de voltaje promedio para cada fase y devuelve 3 listas
#del voltaje promedio en cada fase para cada intervalo de 10 minutos en un total de 24 horas
#Y promediado en los 7 dias de las semana
def buscadorTiempo(listaA,listaB,listaC):
    listaTiempo=cambiarStr('Time') #genera la lista con las horas
    contMinutos=0 
    contHoras=0
    listaPromA=[]
    listaPromB=[]
    listaPromC=[]
    PromInitA=0 
    PromInitB=0
    PromInitC=0
    while (contMinutos<=50 and contHoras<=23): #tiene como limite las 23:50 h
        sumA=0
        sumB=0
        sumC=0
        n=0
        for i in range(0,1009): #revisa todas las horas y las compara con los valores de los contadores
            hora=listaTiempo[i] #se guarda en una variable string el tiempo en la posición i
            if (int(hora[10:12])==contHoras and int(hora[13:15])==contMinutos):
                sumA=sumA+listaA[i] #suma los voltajes en fase A para la hora indicada por los contadores
                sumB=sumB+listaB[i] #suma los voltajes en fase B para la hora indicada por los contadores
                sumC=sumC+listaC[i] #suma los voltajes en fase C para la hora indicada por los contadores
                n=n+1 #guarda los datos sumados para sacar el promedio
        if (contHoras==0 and contMinutos==0): #esto es para poder guardar el promedio a las 00:00 que es necesario ponerlo al final
            PromInitA=sumA/n
            PromInitB=sumB/n
            PromInitC=sumC/n  
        listaPromA.append(sumA/n)
        listaPromB.append(sumB/n)
        listaPromC.append(sumC/n)
        contMinutos=contMinutos+10
        if (contMinutos==60):
            contHoras=contHoras+1
            contMinutos=0
    listaPromA.append(PromInitA)
    listaPromB.append(PromInitB)
    listaPromC.append(PromInitC)
    return listaPromA,listaPromB,listaPromC


######################################### funciones para histograma   ############
#funcion para sacar los porcemtajes de las de las fases en cada clase
def porcentajeclases(fase):
    porc = []
    for j in range(len(fase)):
        po = (fase[j]/1009)*100
        porc.append(round(po,2))
    return(porc)

def datos_histograma():
    #inicializacion de variables para la cantidad de intervalos por clase en cada fase
    clase1A = 0
    clase2A = 0
    clase3A = 0
    clase4A = 0
    clase5A = 0
    clase6A = 0
    clase7A = 0
    clase8A = 0
    clase9A = 0
    
    clase1B = 0
    clase2B = 0
    clase3B = 0
    clase4B = 0
    clase5B = 0
    clase6B = 0
    clase7B = 0
    clase8B = 0
    clase9B = 0
    
    clase1C = 0
    clase2C = 0
    clase3C = 0
    clase4C = 0
    clase5C = 0
    clase6C = 0
    clase7C = 0
    clase8C = 0
    clase9C = 0
    
    
    #asignacion de la cantidad de intervalos por clase a cada fase
    for i in range(len(VmedA)):
        if VmedA[i] <= 104.4:
            clase1A += 1
        if 104.4 < VmedA[i] <= 109.2:
            clase2A += 1
        if 109.2 < VmedA[i] <= 111.6:
            clase3A += 1
        if 111.6 < VmedA[i] <= 114:
            clase4A += 1
        if 114 < VmedA[i] <= 126:
            clase5A += 1
        if 126 < VmedA[i] <= 128.4:
            clase6A += 1
        if 128.4 < VmedA[i] <= 130.8:
            clase7A += 1
        if 130.8 < VmedA[i] <= 135.6:
            clase8A += 1
        if 135.6 < VmedA[i]:
            clase9A += 1
            
    for i in range(len(VmedB)):
        if VmedB[i] <= 104.4:
            clase1B += 1
        if 104.4 < VmedB[i] <= 109.2:
            clase2B += 1
        if 109.2 < VmedB[i] <= 111.6:
            clase3B += 1
        if 111.6 < VmedB[i] <= 114:
            clase4B += 1
        if 114 < VmedB[i] <= 126:
            clase5B += 1
        if 126 < VmedB[i] <= 128.4:
            clase6B += 1
        if 128.4 < VmedB[i] <= 130.8:
            clase7B += 1
        if 130.8 < VmedB[i] <= 135.6:
            clase8B += 1
        if 135.6 < VmedB[i]:
            clase9B += 1
    
    for i in range(len(VmedC)):
        if VmedC[i] <= 104.4:
            clase1C += 1
        if 104.4 < VmedC[i] <= 109.2:
            clase2C += 1
        if 109.2 < VmedC[i] <= 111.6:
            clase3C += 1
        if 111.6 < VmedC[i] <= 114:
            clase4C += 1
        if 114 < VmedC[i] <= 126:
            clase5C += 1
        if 126 < VmedC[i] <= 128.4:
            clase6C += 1
        if 128.4 < VmedC[i] <= 130.8:
            clase7C += 1
        if 130.8 < VmedC[i] <= 135.6:
            clase8C += 1
        if 135.6 < VmedC[i]:
            clase9C += 1
    
       
    #listas con la cantidad de intervalos para cada fase
    faseA = [clase1A, clase2A, clase3A, clase4A, clase5A, clase6A, clase7A, clase8A, clase9A]
    faseB = [clase1B, clase2B, clase3B, clase4B, clase5B, clase6B, clase7B, clase8B, clase9B]
    faseC = [clase1C, clase2C, clase3C, clase4C, clase5C, clase6C, clase7C, clase8C, clase9C]

    
    
    #asignacion de los porcentajes a las listas
    porcfaseA = porcentajeclases(faseA)
    porcfaseB = porcentajeclases(faseB)
    porcfaseC = porcentajeclases(faseC)
    
    return faseA, faseB, faseC, porcfaseA, porcfaseB, porcfaseC


faseA,faseB,faseC,porcfaseA, porcfaseB,porcfaseC= datos_histograma()
###############################################  FUNCIONES QUE SON LLAMADAS POR LOS BOTONES###########33
###########################        BOTON 1             ###############3########
    
def boton1(): #genera la tabla de intervalos de distorción armonica dentro de rango
    VmedA=cambiar(nombresTensiones[0])
    VmedB=cambiar(nombresTensiones[1])
    VmedC=cambiar(nombresTensiones[2])
    
    dentroRangoA,fueraRangoA,fallaA=porcentajesTablaVol(VmedA)
    dentroRangoB,fueraRangoB,fallaB=porcentajesTablaVol(VmedB)
    dentroRangoC,fueraRangoC,fallaC=porcentajesTablaVol(VmedC)
    
    if (fallaA==1):
        fallaAA='Fallo por consecutivos'
    elif (fallaA==0 and fueraRangoA>5):
        fallaAA='Incorrecto'
    else:
        fallaAA='Correcta'
    
    
    if (fallaB==1):
        fallaBB='Fallo por consecutivos'
    elif (fallaB==0 and fueraRangoB>5):
        fallaBB='Incorrecto'
    else:
        fallaBB='Correcta'
        
        
    if (fallaC==1):
        fallaCC='Fallo por consecutivos'
    elif (fallaC==0 and fueraRangoC>5):
        fallaCC='Incorrecto'
    else:
        fallaCC='Correcta'
    
    
    #Codigo para realizar la tabla
    title_text = 'INTERVALOS DE TENSIÓN PROMEDIO DENTRO DE RANGO'
    fig_background_color = 'skyblue'
    fig_border = 'steelblue'
    data =  [
                [          'Detalle'],
                [ 'Tensión en fase A dentro del rango (%)',str(round(dentroRangoA,2))+'%' ],
                ['Tensión en fase A fuera del rango (%)', str(round(fueraRangoA,3))+'%'],
                ['Evaluación de la tensión en fase A', fallaAA],
                [ 'Tensión en fase B dentro del rango (%)', str(round(dentroRangoB,2))+'%'],
                ['Tensión en fase B fuera del rango (%)',  str(round(fueraRangoB,3))+'%'],
                ['Evaluación de la tensión en fase B',  fallaBB],
                [ 'Tensión en fase C dentro del rango (%)',  str(round(dentroRangoC,2))+'%'],
                ['Tensión en fase C fuera del rango (%)',  str(round(fueraRangoC,3))+'%'],
                ['Evaluación de la tensión en fase C',  fallaCC],
            ]
    # Pop the headers from the data array
    column_headers = data.pop(0)
    row_headers = [x.pop(0) for x in data]
    # Table data needs to be non-numeric text. Format the data
    # while I'm at it.
    cell_text = []
    
    for row in data:
        cell_text.append(row)
    # Get some lists of color specs for row and column headers
    rcolors = plt.cm.BuPu(np.full(len(row_headers), 0.1))
    ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))
    # Create the figure. Setting a small pad on tight_layout
    # seems to better regulate white space. Sometimes experimenting
    # with an explicit figsize here can produce better outcome.
    plt.figure(linewidth=2,
               edgecolor=fig_border,
               facecolor=fig_background_color,
               tight_layout={'pad':1},
               figsize=(18,9)
              )
    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
                          rowLabels=row_headers,
                          rowColours=rcolors,
                          rowLoc='right',
                          colColours=ccolors,
                          colLabels=column_headers,
                          loc='center')
    # Scaling is the only influence we have over top and bottom cell padding.
    # Make the rows taller (i.e., make cell y scale larger).
    the_table.scale(1, 1.5)
    # Hide axes
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # Hide axes border
    plt.box(on=None)
    # Add title
    plt.suptitle(title_text)
    # Add footer
    #plt.figtext(0.95, 0.05, footer_text, horizontalalignment='right', size=6, weight='light')
    # Force the figure to update, so backends center objects correctly within the figure.
    # Without plt.draw() here, the title will center on the axes and not the figure.
    plt.draw()
    # Create image. plt.savefig ignores figure edge and face colors, so map them.
    fig = plt.gcf()
    plt.savefig('pyplot-table-demo.png',
                #bbox='tight',
                edgecolor=fig.get_edgecolor(),
                facecolor=fig.get_facecolor(),
                dpi=150
                )

#####################        BOTON 2     #########################
#GENERA UNA VENTANA SECUNDARIA QUE LLAMA A CADA UNA DE LAS SIG 3 FUNCIONES
## GRAFICA TENSIONES FASE A
def graficaVnA(): #muestra la gráfica de la fase A de las tensiones promedio (BOTON 2)
    plt.figure(figsize=(18,9)) #tamaÃ±o de la imagen
    plt.ylim(0,150) #limites de datos mostrados en Y
    plt.plot(fechas, VmedA, label= r'$Promedio de tensiones$') #generador grafica
    plt.xticks(np.linspace(0, 1009, len(fechas10)), fechas10, rotation=45) #datos en X
    plt.xlabel('Fechas y horas') #etiqueta eje x
    plt.ylabel('Tensión promedio (V)') #etiqueta eje y
    plt.title('Gráfica de tensiones promedio con respecto al tiempo') #titulo grÃ¡fica
    plt.grid(True) #generador de malla
    plt.axhline(114, color='b', lw=1, label= r'$max$')
    plt.axhline(126, color='r', lw=1, label= r'$min$')
    plt.legend(['Vmed','Limite superior', 'Limite inferior'], loc=4)
   
    ## GRAFICA TENSIONES FASE B
def graficaVnB(): # muestra la gráfica de la fase B de las tensiones promedio (BOTON 2)
    plt.figure(figsize=(18,9)) #tamaÃ±o de la imagen
    plt.ylim(0,150) #limites de datos mostrados en Y
    plt.plot(fechas, VmedB, label= r'$Promedio de tensiones$') #generador grafica
    plt.xticks(np.linspace(0, 1009, len(fechas10)), fechas10, rotation=45) #datos en X
    plt.xlabel('Fechas y horas') #etiqueta eje x
    plt.ylabel('Tensión promedio (V)') #etiqueta eje y
    plt.title('Gráfica de tensiones promedio con respecto al tiempo') #titulo grÃ¡fica
    plt.grid(True) #generador de malla
    plt.axhline(114, color='b', lw=1, label= r'$max$')
    plt.axhline(126, color='r', lw=1, label= r'$min$')
    plt.legend(['Vmed','Limite superior', 'Límite inferior'], loc=4)

    # GRAFICA TENSIONES FASE C
def graficaVnC(): # muestra la gráfica de la fase C de las tensiones promedio (BOTON 2)
    plt.figure(figsize=(18,9)) #tamaÃ±o de la imagen
    plt.ylim(0,150) #limites de datos mostrados en eje Y
    plt.plot(fechas, VmedC, label= r'$Promedio de tensiones$') #generador grafica
    plt.xticks(np.linspace(0, 1009, len(fechas10)), fechas10, rotation=45) #datos en X
    plt.xlabel('Fechas y horas') #etiqueta eje x
    plt.ylabel('Tensión promedio (V)') #etiqueta eje y
    plt.title('Gráfica de tensiones promedio con respecto al tiempo') #titulo grÃ¡fica
    plt.grid(True) #generador de malla
    plt.axhline(114, color='b', lw=1, label= r'$max$')
    plt.axhline(126, color='r', lw=1, label= r'$min$')
    plt.legend(['Vmed','Limite superior', 'Lí­mite inferior'], loc=4)

##########################               BOTON 3   ############################
## TABLA DE INTERVALOS DE DISTOCION ARMONICA TOTAL DENTRO DE RANGO
def boton3():
    THDA=cambiarModif(nombresTHD[0])
    THDB=cambiarModif(nombresTHD[1])
    THDC=cambiarModif(nombresTHD[2])
    
    dentroRangoA,fueraRangoA=porcentajesTablaTHD(THDA)
    dentroRangoB,fueraRangoB=porcentajesTablaTHD(THDB)
    dentroRangoC,fueraRangoC=porcentajesTablaTHD(THDC)
    
    
    if (fueraRangoA>5):
        fallaAA='Incorrecto'
    else:
        fallaAA='Correcta'
    
    if (fueraRangoB>5):
        fallaBB='Incorrecto'
    else:
        fallaBB='Correcta'
        
    if (fueraRangoC>5):
        fallaCC='Incorrecto'
    else:
        fallaCC='Correcta'
     
        
    #Codigo para realizar la tabla
    title_text = 'INTERVALOS DE DISTORSIÓN ARMÓNICA TOTAL DENTRO DE RANGO'
    fig_background_color = 'skyblue'
    fig_border = 'steelblue'
    data =  [
                [          'Porcentaje'],
                [ 'THDV en fase A dentro del rango',str(round(dentroRangoA,2))+'%' ],
                ['THDV en fase B dentro del rango', str(round(fueraRangoA,3))+'%'],
                ['Evaluación de THDV en fase A', fallaAA],
                [ 'THDV en fase B dentro del rango', str(round(dentroRangoB,2))+'%'],
                ['THDV en fase B fuera del rango',  str(round(fueraRangoB,3))+'%'],
                ['Evaluación de THDV en fase B',  fallaBB],
                [ 'THDV en fase C dentro del rango',  str(round(dentroRangoC,2))+'%'],
                ['THDV en fase C fuera del rango',  str(round(fueraRangoC,3))+'%'],
                ['Evaluación de THDV en fase C',  fallaCC],
            ]
    # Pop the headers from the data array
    column_headers = data.pop(0)
    row_headers = [x.pop(0) for x in data]
    # Table data needs to be non-numeric text. Format the data
    # while I'm at it.
    cell_text = []
    for row in data:
        cell_text.append(row)
    # Get some lists of color specs for row and column headers
    rcolors = plt.cm.BuPu(np.full(len(row_headers), 0.1))
    ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))
    # Create the figure. Setting a small pad on tight_layout
    # seems to better regulate white space. Sometimes experimenting
    # with an explicit figsize here can produce better outcome.
    plt.figure(linewidth=2,
               edgecolor=fig_border,
               facecolor=fig_background_color,
               tight_layout={'pad':1},
               figsize=(10,7)
              )
    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
                          rowLabels=row_headers,
                          rowColours=rcolors,
                          rowLoc='right',
                          colColours=ccolors,
                          colLabels=column_headers,
                          loc='center')
    # Scaling is the only influence we have over top and bottom cell padding.
    # Make the rows taller (i.e., make cell y scale larger).
    the_table.scale(1, 1.5)
    # Hide axes
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # Hide axes border
    plt.box(on=None)
    # Add title
    plt.suptitle(title_text)
    # Add footer
    #plt.figtext(0.95, 0.05, footer_text, horizontalalignment='right', size=6, weight='light')
    # Force the figure to update, so backends center objects correctly within the figure.
    # Without plt.draw() here, the title will center on the axes and not the figure.
    plt.draw()
    # Create image. plt.savefig ignores figure edge and face colors, so map them.
    fig = plt.gcf()
    plt.savefig('pyplot-table-demo.png',
                #bbox='tight',
                edgecolor=fig.get_edgecolor(),
                facecolor=fig.get_facecolor(),
                dpi=150
                )

##############################       BOTON 4    #########################3
    
def armonicoBarra(): #muestra la grafica del espectro de armónicos de tension media
    for i in range (0,19):
        A=convertidor(armFaseA[i])
        B=convertidor(armFaseB[i])
        C=convertidor(armFaseC[i])
        promArmA.append(A)
        promArmB.append(B)
        promArmC.append(C)
        
    x = np.arange(len(armonicos))
    width = 0.2
    plt.figure(figsize=(15,6))
    plt.rc('font', size=20)
    plt.bar(x - width, promArmA, width, label = "fase A")
    plt.bar(armonicos, promArmB, width, label = "fase B")
    plt.bar(x + width, promArmC, width, label = "fase C")
    plt.xlabel("Orden de armónico")
    plt.ylabel("Promedio de tensión nominal")
    plt.title("Espectro de los armónicos de tensión")
    plt.rc('font', size=10)
    plt.legend()
    plt.show()


################################        BOTON 5       ##################################

def semiF47():
    ## variables para la curva semi F-47
    #algoritmo que llama a la función (cambiar) y añade las listas a VmedA, B y C.
    VpA=cambiarF47(nombresUmbrales[0])
    VpB=cambiarF47(nombresUmbrales[1])
    VpC=cambiarF47(nombresUmbrales[2])
    DA = cambiarF47(nombresUmbrales[0])
    DB = cambiarF47(nombresDuraciones[1])
    DC = cambiarF47(nombresDuraciones[2])
    VporcA = porcentaje(VpA)
    VporcB = porcentaje(VpB)
    VporcC = porcentaje(VpC)
    
    xF47 = [0.0166, 0.2, 0.5, 10, 10000]
    yF47 = [50, 70, 80, 90, 90]
    
    plt.figure(figsize=(15,6))
    plt.rc('font', size=20)
    plt.plot(xF47, yF47, drawstyle = "steps-post")
    plt.plot(DA, VporcA, "ro")
    plt.plot(DB, VporcB, "go")
    plt.plot(DC, VporcC, "mo")
    plt.xscale("log")
    plt.xlabel("Duración (s)")
    plt.ylabel("Porcentaje de variación de tensión")
    plt.title("Variaciones de tensión")
    plt.show()

#########################3######        BOTON 6 ######################################
    
##########################  tabla de histograma
    
def tabla_histograma():
    title_text = 'TABLA PARA HISTOGRAMA DE TENSIÓN PROMEDIO SEGÚN LA NORMA'
    fig_background_color = 'skyblue'
    fig_border = 'steelblue'
    
    data =  [
                [1,2,3,4,4,5,6,7],
                [1,'1',  'Vn<=87', faseA[0],   faseB[0],   faseC[0], str(porcfaseA[0])+'%',str(porcfaseB[0])+'%',str(porcfaseC[0])+'%'],
                [2,'2',  '87<Vn<=91', faseA[1],   faseB[1],   faseC[1], str(porcfaseA[1])+'%',str(porcfaseB[1])+'%',str(porcfaseC[1])+'%'],
                [3,'3',  '91<Vn<=93',  faseA[2],   faseB[2],   faseC[2], str(porcfaseA[2])+'%',str(porcfaseB[2])+'%',str(porcfaseC[2])+'%'],
                [4,'4', '93<Vn<95',  faseA[3],   faseB[3],   faseC[3], str(porcfaseA[3])+'%',str(porcfaseB[3])+'%',str(porcfaseC[3])+'%'],
                [5,'5', '95<=Vn<=105',  faseA[4],   faseB[4],   faseC[4], str(porcfaseA[4])+'%',str(porcfaseB[4])+'%',str(porcfaseC[4])+'%'],
                [6,'6', '105<Vn<=107',  faseA[5],   faseB[5],   faseC[5], str(porcfaseA[5])+'%',str(porcfaseB[5])+'%',str(porcfaseC[5])+'%'],
                [7,'7', '107<Vn<=109',  faseA[6],   faseB[6],   faseC[6], str(porcfaseA[6])+'%',str(porcfaseB[6])+'%',str(porcfaseC[6])+'%'],
                [8,'8', '109<Vn<=113',  faseA[7],   faseB[7],   faseC[7], str(porcfaseA[7])+'%',str(porcfaseB[7])+'%',str(porcfaseC[7])+'%'],
                [9,'9', '113<Vn',  faseA[8],   faseB[8],   faseC[8], str(porcfaseA[8])+'%',str(porcfaseB[8])+'%',str(porcfaseC[8])+'%'],
                [10,'--','TOTAL ', sum(faseA) ,   sum(faseB),  sum(faseC), str(sum(porcfaseA))+'%',str(sum(porcfaseB))+'%',str(sum(porcfaseC))+'%']
            ]
    # Pop the headers from the data array      str(round(dentroRangoA,2))+'%'
    
    column_headers = data.pop(0)
    #column_headers = data.pop(1)
    row_headers = [x.pop(0) for x in data]
    
    # Table data needs to be non-numeric text. Format the data
    # while I'm at it.
    cell_text = []
    for row in data:
        cell_text.append(row)
    
    
    
    fig=plt.figure(linewidth=2,
               edgecolor=fig_border,
               facecolor=fig_background_color,
               #tight_layout={'pad':1},
               figsize=(18,6)
              )
    
    ax=plt.subplot(111)
    ax.axis('off') 
    
    colors = [["#56b5fd"]]
    colors3= [["#56b5fd","#56b5fd","#56b5fd"]]
    colorst= [
                ["#56b5fd","#56b5fd","w","w","w","w","w","w"],
                ["#56b5fd","#56b5fd","w","w","w","w","w","w"],
                ["#56b5fd","#56b5fd","w","w","w","w","w","w"],
                ["#56b5fd","#56b5fd","w","w","w","w","w","w"],
                ["#56b5fd","#56b5fd","w","w","w","w","w","w"],
                ["#56b5fd","#56b5fd","w","w","w","w","w","w"],
                ["#56b5fd","#56b5fd","w","w","w","w","w","w"],
                ["#56b5fd","#56b5fd","w","w","w","w","w","w"],
                ["#56b5fd","#56b5fd","w","w","w","w","w","w"],
                ["#56b5fd","#56b5fd","w","w","w","w","w","w"]
            ]
    
    
    t1=plt.table(cellText=[['Clase']],
                         cellColours=colors,
                         loc='bottom',
                         bbox=[0, 0.6, 0.125, 0.3]
                         )
    
    
    
    plt.table(cellText=[['Tensión']],
                          cellColours=colors,
                         loc='bottom',
                         bbox=[0.125, 0.75, 0.125, 0.15]
                         )
    
    plt.table(cellText=[['Rango (%)']],
                         cellColours=colors,
                         loc='bottom',
                         bbox=[0.125, 0.6, 0.125, 0.15]
                         )
    
    
    plt.table(cellText=[['Cantidad de intervalos']],
                         cellColours=colors, 
                         loc='bottom',
                         bbox=[0.250, 0.75, 0.374, 0.15]
                         )
    
    plt.table(cellText=[['L1', 'L2','L3']],
                         cellColours=colors3,
                         loc='bottom',
                         bbox=[0.250, 0.6, 0.374, 0.15]
                         )
    
    plt.table(cellText=[['Porcentajes de intervalos']],
                          cellColours=colors,
                         loc='bottom',
                         bbox=[0.625, 0.75, 0.374, 0.15]
                         )
    
    plt.table(cellText=[['L1', 'L2','L3']],
                         cellColours=colors3,
                         loc='bottom',
                         bbox=[0.625, 0.6, 0.374, 0.15]
                         )
    
    table=plt.table(cellText=cell_text,
                         cellColours=colorst,
                         loc='bottom',
                         bbox=[0, 0, 1, 0.6]
                         )
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1.5, 1.5)  
    plt.suptitle(title_text)
    plt.show()


########################### grafica- Histograma


def grafica_histograma():   
    #generacion de la grafica de barras de porcentajes
    x = np.arange(len(clases))
    width = 0.2
    plt.figure(figsize=(15,6))
    plt.rc('font', size=20)
    plt.bar(x - width, porcfaseA, width, label = "fase A")
    plt.bar(clases, porcfaseB, width, label = "fase B")
    plt.bar(x + width, porcfaseC, width, label = "fase C")
    plt.xlabel("Clases")
    plt.ylabel("Porcentaje del total de intervalos")
    plt.legend()
    plt.show()



################################        BOTON 7     ###################33##########3
    
def boton7(): ## esta funcion genera las 3 gráficas de tensiones medias juntas
    PromDiasA,PromDiasB,PromDiasC=buscadorTiempo(VmedA,VmedB,VmedC)
    horasDiarias=['0:00', '2:00', '4:00', '6:00', '8:00', '10:00', '12:00', '13:00', '14:00', '16:00', '18:00', '20:00', '22:00', '0:00']
    ejex=np.linspace(0, 144, 145)
    plt.figure(figsize=(18,9)) #tamaÃ±o de la imagen
    plt.ylim(0,150) #limites de datos mostrados en Y
    plt.xlabel('Horas') #etiqueta eje x
    plt.ylabel('Tensión promedio Diaria (V)') #etiqueta eje y
    plt.legend(['VfaseA','VfaseB', 'VfaseC'], loc=4)
    plt.grid(True) #generador de malla
    plt.title('Curva del perfil diario de tensión') #titulo grÃ¡fica
    plt.plot(ejex, PromDiasA, ejex, PromDiasB, ejex, PromDiasC, label= r'$Promedio de tensiones Diario$') #generador grafica
    plt.xticks(np.linspace(0, 144, 13), horasDiarias, rotation=45) #datos en X
    plt.grid(True) #generador de malla
   
        
 ## funciones para mostrar ventanas 
#############################################3
def mostrarSecundaria():
    miFrame.pack_forget()
    secundaria.pack(side="left", fill="both", expand=True)

# esta funcion se usa unicamente para abrir una ventana con las opciones de 
# generar una gráfica para las tensiones promedio de las fases A, B y C
def VentanaSecundaria(master, callback=None, args=(), kwargs={}): ## ventana secundaria general
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    #boton gráfica
    botonA = tk.Button(main_frame, text="Gráfica de Tensión Fase A", command=graficaVnA)
    botonA.grid(row=1,column=2,padx=10,pady=10)
    #boton gráfica
    botonB = tk.Button(main_frame, text="Gráfica de Tensión Fase B", command=graficaVnB)
    botonB.grid(row=2,column=2,padx=10,pady=10)
    #boton gráfica
    botonC = tk.Button(main_frame, text="Gráfica de Tensión Fase C", command=graficaVnC)
    botonC.grid(row=3,column=2,padx=10,pady=10)
    
    #Boton volver
    boton_volver = tk.Button(main_frame, text="Volver", command=callback)
    boton_volver.grid(row=4,column=2,padx=10,pady=10)
    return main_frame

def mostrarPrincipal():   ## FUNCION PARA ABRIR VENTANA PRINCIPAL
    secundaria.pack_forget()
    secundaria2.pack_forget()
    miFrame.pack(expand=True)
    
def mostrarsecundaria2():
    miFrame.pack_forget()
    secundaria2.pack(side="left", fill="both", expand=True)

def ventanasecundaria2(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    #boton gráfica
    botonA = tk.Button(main_frame, text="Tabla para histograma de tensión promedio", command=tabla_histograma)
    botonA.grid(row=1,column=2,padx=10,pady=10)
    #boton gráfica
    botonB = tk.Button(main_frame, text="Histograma de tensión promedio", command=grafica_histograma)
    botonB.grid(row=2,column=2,padx=10,pady=10)
    
    #Boton volver
    boton_volver = tk.Button(main_frame, text="Volver", command=callback)
    boton_volver.grid(row=4,column=2,padx=10,pady=10)
    return main_frame

    
############################## interfaz gráfica (ventanas)  ########################
raiz=tk.Tk()
raiz.title("Interfaz para análisis de datos")
raiz.config(bg="green")
miFrame=tk.Frame(raiz,width=1200,height=600)
mensaje=tk.Label(miFrame,text="Seleccione la opción que desee para realizar el análisis: ",font=("Times New Roman",14))
mensaje.grid(row=0,column=1)
secundaria = VentanaSecundaria(raiz, mostrarPrincipal)  
secundaria2=ventanasecundaria2(raiz, mostrarPrincipal)  
    
   
## llamada principal    
mostrarPrincipal()

########################### calculos y operaciones #####################333

### gráfica del espectro de armónicos de tensión 

#BOTONES HEE HEE
boton_1=tk.Button(miFrame, text="Generar tabla para intervalos de tensión promedio dentro de rango",font=("Times New Roman",14),command=boton1)
boton_1.grid(row=2,column=1,padx=10,pady=10)
boton_2=tk.Button(miFrame, text="Gráficas de tensión promedio junto a sus umbrales",font=("Times New Roman",14),command=mostrarSecundaria)
boton_2.grid(row=3,column=1,padx=10,pady=10)
boton_3=tk.Button(miFrame, text="Intervalos de distorsión armónica total de tensión dentro de rango",font=("Times New Roman",14), command=boton3)
boton_3.grid(row=4,column=1,padx=10,pady=10)
boton_4=tk.Button(miFrame, text="Gráfica del espectro de los armónicos de tensión",font=("Times New Roman",14),command=armonicoBarra)
boton_4.grid(row=5,column=1,padx=10,pady=10)
boton_5=tk.Button(miFrame, text="Variaciones de tensión según la curva SEMI-F47",font=("Times New Roman",14),command=semiF47)
boton_5.grid(row=6,column=1,padx=10,pady=10)
boton_6=tk.Button(miFrame, text="Histograma de tensión promedio",font=("Times New Roman",14),command=mostrarsecundaria2)
boton_6.grid(row=7,column=1,padx=10,pady=10)
boton_7=tk.Button(miFrame, text="Curva de perfil diario de tensión para el periodo de prueba",font=("Times New Roman",14),command=boton7)
boton_7.grid(row=8,column=1,padx=10,pady=10)


raiz.mainloop()
