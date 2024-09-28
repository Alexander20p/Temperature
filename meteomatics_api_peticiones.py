import meteomatics.api as api
from datetime import datetime, date, time, timezone
import datetime as dt
import pandas as pd
def pedir_data():
    ubicaion = []
    nombre = "User"
    contraseña = "Password"
    interval = dt.timedelta(hours=3)
    parameters = ['t_2m:C',"sunrise:sql","uv:idx","precip_1h:mm","msl_pressure:hPa","wind_speed_10m:ms","wind_dir_10m:d"]
    startdate = dt.datetime.now(timezone.utc).replace(second=0, microsecond=0)
    df = api.query_time_series(toledo,startdate,startdate,interval,parameters,nombre, contraseña,)
    df.to_csv("./App_meteorologia/h.csv")
    return 
def pasar_datos_csv_to_var():
    df = pd.read_csv("./App_meteorologia/h.csv")
    temp = df["t_2m:C"]
    salida_del_sol = df["sunrise:sql"]
    uv = df["uv:idx"]
    precipitaciones = df["precip_1h:mm"]
    presion = df["msl_pressure:hPa"]
    velocidad_viento = df["wind_speed_10m:ms"]
    dir_vient = df["wind_dir_10m:d"]
    temp = temp[0]
    salida_del_sol = salida_del_sol[0]
    uv = uv[0]
    precipitaciones = precipitaciones[0]
    presion = presion[0]
    velocidad_viento = velocidad_viento[0]
    dir_vient = dir_vient[0]
    salida_del_sol =dt.datetime.strptime(salida_del_sol,'%Y-%m-%d %H:%M:%S')
    suma = dt.timedelta(hours=2)
    salida_del_sol = salida_del_sol+suma
    return temp,salida_del_sol,uv,precipitaciones,presion,velocidad_viento,dir_vient
