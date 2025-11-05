import random

def predecir_partido(equipo_local: str, equipo_visitante: str) -> dict:
    """
    Por ahora es una predicción dummy.
    Más adelante aquí conectamos el modelo real.
    """
    goles_local = random.randint(0, 3)
    goles_visitante = random.randint(0, 3)
    prob = random.uniform(55, 90)
    return {
        "resultado": f"{equipo_local} {goles_local} - {goles_visitante} {equipo_visitante}",
        "probabilidad": round(prob, 2)
    }
