import random

def predecir_partido(equipo_local, equipo_visitante):
    resultado = f"{equipo_local} {random.randint(0,3)} - {random.randint(0,3)} {equipo_visitante}"
    prob = random.uniform(55, 90)
    return {"resultado": resultado, "probabilidad": round(prob, 2)}
