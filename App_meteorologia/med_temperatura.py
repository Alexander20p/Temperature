import requests as rq
def pregunt_temp():
    api = "Tu api key"
    url = f"https://api.weatherstack.com/current?access_key={api}"
    ubicacion = {"query":"tu ciudad"}
    response = rq.get(url,params=ubicacion)
    resultado = response.json()
    resultado = resultado["current"]
    temperatura,humedad,presion,obs_time,desc_tiempo = resultado["temperature"],resultado["humidity"],resultado["pressure"],resultado["observation_time"],resultado["weather_descriptions"]
    return temperatura,humedad,presion,obs_time,desc_tiempo
