#CodigoWebScraping_Revista.py

from datetime import datetime
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5
import pytz
import mplfinance as mpf


print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

else:
    print("MetaTrader5  Initiated")


# Definimos los TimeFrames para su facil acceso en el codigo

M1 = mt5.TIMEFRAME_M1
M2 = mt5.TIMEFRAME_M2
M3 = mt5.TIMEFRAME_M3
M4 = mt5.TIMEFRAME_M4
M5 = mt5.TIMEFRAME_M5
M6 = mt5.TIMEFRAME_M6
M10 = mt5.TIMEFRAME_M10
M12 = mt5.TIMEFRAME_M12
M15 = mt5.TIMEFRAME_M15
M20 = mt5.TIMEFRAME_M20 
M30 = mt5.TIMEFRAME_M30
H1 = mt5.TIMEFRAME_H1
H2 = mt5.TIMEFRAME_H2
H3 = mt5.TIMEFRAME_H3
H4 = mt5.TIMEFRAME_H4
H6 = mt5.TIMEFRAME_H6
H8 = mt5.TIMEFRAME_H8
H12 = mt5.TIMEFRAME_H12
D1 = mt5.TIMEFRAME_D1
W1 = mt5.TIMEFRAME_W1
MN1 = mt5.TIMEFRAME_MN1

#Seleccionamos el TimeFrame que usaremos en este modelo

Time_Frame = M15

#Elejimos el par de Divisas que usaremos en este modelo

par_divisas = "EURUSD"

#Data Time de la primera vela desde donde tomaremos los datos

año_vi = 2022
mes_vi = 9
dia_vi = 19
hora_vi = 10
minuto_vi = 00

#Data Time de la ultima vela hasta donde tomaremos los datos

año_vf = 2022
mes_vf = 9
dia_vf = 20
hora_vf = 3
minuto_vf = 15

   
#Definimos la franja horaria 

timezone = pytz.timezone("Etc/UTC")

#Definimos el punto de inicion y el punto final de los datos a observar dado la franja horaria 

utc_from = datetime(año_vi, mes_vi, dia_vi, hour = hora_vi, minute = minuto_vi, tzinfo=timezone)
utc_to = datetime(año_vf, mes_vf, dia_vf, hour = hora_vf, minute = minuto_vf, tzinfo=timezone)

#Obtenemos los datos del rango deseado dado el par deseado 

rate = mt5.copy_rates_range(par_divisas, Time_Frame, utc_from, utc_to)

mt5.shutdown()


#Creamos un Data Frame de los datos obtenidos

rate_data_frame = pd.DataFrame(rate)

rate_data_frame2 =pd.DataFrame(rate)

#Cambiar el nombre de tick_volume por volume

rate_data_frame.rename({'tick_volume': 'volume'}, axis=1, inplace=True)

#Denotamos los datos de tiempo para la visualizacion

rate_data_frame['time']=pd.to_datetime(rate_data_frame['time'], unit='s')
rate_data_frame=rate_data_frame.set_index('time')

#

rate_data_frame2['time']=pd.to_datetime(rate_data_frame2['time'], unit='s')
n = len(rate_data_frame2)

#Visualizamos los datos

print("\nDatos")
print(rate_data_frame )  

#Definimos la cadena con los valores que deseamos llevar a MT5


Z_1 = 1.00267
Z_2 = 0.99914
Z_3 = 0.99715
Z_4 = 1.00466

Date_Fecha_Inicial = (rate_data_frame2.iloc[0, 0])
Date_Fecha_Final = (rate_data_frame2.iloc[n-1, 0])
