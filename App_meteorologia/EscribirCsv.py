import pandas as pd
import med_temperatura as mt
def escribir_csv(temperatura,humedad,presion,obs_time,desc_tiempo):
    df = pd.read_csv("./App_meteorologia/csv.csv")
    dicionario ={
        "fech_obs":obs_time,
        "temperatura":temperatura,
        "humdad":humedad,
        "presion":presion,
        "descripcion_tiemp":desc_tiempo
    }
    df2 = pd.DataFrame(dicionario)
    union = pd.concat([df, df2],ignore_index=False)
    print(union)
    
    union.to_csv("./App_meteorologia/csv.csv",index=False)
        
temperatura,humedad,presion,obs_time,desc_tiempo=mt.pregunt_temp()
escribir_csv(temperatura,humedad,presion,obs_time,desc_tiempo)
print(pd.read_csv("./App_meteorologia/csv.csv"))

