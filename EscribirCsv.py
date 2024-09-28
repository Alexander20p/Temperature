import pandas as pd
import meteomatics_api_peticiones as mt
from datetime import datetime, date, time, timezone
import datetime as dt
def escribir_csv(temp,salida_del_sol,uv,precipitaciones,presion,velocidad_viento,dir_vient):
    df = pd.read_csv("./App_meteorologia/csv.csv")
    fecha = dt.datetime.now(tz=None).replace(second=0, microsecond=0)
    dicionario ={
        "fecha":f"{fecha}",
        "t_2m:C":f"{temp}",
        "sunrise:sql":f"{salida_del_sol}",
        "uv:idx":f"{uv}",
        "precip_1h:mm":f"{precipitaciones}",
        "msl_pressure:hPa":f"{presion}",
        "wind_speed_10m:ms":f"{velocidad_viento}",
        "wind_dir_10m:d":f"{dir_vient}"
    }
    df2 = pd.DataFrame(dicionario,index=[0])
    union = pd.concat([df, df2],ignore_index=False)
    print(union)
    
    union.to_csv("./App_meteorologia/csv.csv",index=False)
mt.pedir_data()
temp,salida_del_sol,uv,precipitaciones,presion,velocidad_viento,dir_vient= mt.pasar_datos_csv_to_var()
print(temp,salida_del_sol,uv,precipitaciones,presion,velocidad_viento,dir_vient)
escribir_csv(temp,salida_del_sol,uv,precipitaciones,presion,velocidad_viento,dir_vient)
print(pd.read_csv("./App_meteorologia/csv.csv"))

