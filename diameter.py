import math

def calcular_diametro_tuberia(flujo_m3s, velocidad_ms):
    if velocidad_ms <= 0:
        raise ValueError("La velocidad debe ser mayor que cero.")
    
    diametro_m = math.sqrt((4 * flujo_m3s) / (math.pi * velocidad_ms))
    return diametro_m
