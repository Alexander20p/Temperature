import requests as rq
def pregunt_temp():
    api = "162e3d3b48451b45cb62c1a4d80277ad"
    url = f"https://api.weatherstack.com/current?access_key={api}"
    ubicacion = {"query":"toledo Spain"}
    response = rq.get(url,params=ubicacion)
    resultado = response.json()
    resultado = resultado["current"]
    temperatura,humedad,presion,obs_time,desc_tiempo = resultado["temperature"],resultado["humidity"],resultado["pressure"],resultado["observation_time"],resultado["weather_descriptions"]
    return temperatura,humedad,presion,obs_time,desc_tiempo