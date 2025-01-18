from dataclasses import dataclass
import numpy as np

@dataclass
class formulas:
    """
    Formulas for calculating the mean and standard deviation of a dataset.
    """

    """
    tiempo de llenado: es el tiempo que demora el sistema en llenar el tanque
    
    tiempo de vaciado: es el tiempo que tarda el tanque en vaciarse
    podemos utilizar la anterior formula para calcularlo
    variables a crear:
    -----------------
    filling_time: tiempo de llenado
    emptying_ ime: tiempo de vaciado
    """
    fe_time = lambda volume, flow: volume/flow

    """
    Costo total: Conociendo el precio de la gasolina por litro y el 
    volumen total, puedes calcular el costo total de llenar el tanque.
    costo_total = VxP
    V = volumen (L)
    P = precio gasolina por litro (USD/L)
    variables a crear:
    -----------------
    total_tank: valor total del tanque lleno
    valor_level: valor del nivel de la gasolina
    """
    total_cost = lambda volume, cost: volume*cost

    """
    Tanques Cilíndricos Horizontales
    Longitud: Entre 2 y 10 metros (aproximadamente 78 a 394 pulgadas)
    Diámetro: Entre 1 y 3 metros (aproximadamente 39 a 118 pulgadas)

    Basado en la API (American Petroleum Institute): La norma API 650 es 
    una de las más utilizadas a nivel mundial para el diseño y construcción 
    de tanques de almacenamiento de petróleo y derivados. Establece requisitos 
    para materiales, diseño, fabricación, pruebas e inspección.
    """
    # formula of volume
    volume = lambda radius, lenght, ullage = 0: (np.pi * (radius**2) * lenght) - ullage

    """
    Tanque rectangulas
    """
    volume_rec = lambda width, height, length: width * height * length

    """
    Tanque esferico
    """
    volume_sphere = lambda radius: (4/3) * np.pi * (radius**3)

    """
    calcular ullage
    o espacio de vapor
    espacio que se deja en el tanque por seguridad del cambio de temperatura
    el porcentaje va de 5% a 10% del volumen (es usado por muchas empresas estos porcentajes)
    """

    ullage = lambda volume, ullage = 10: (volume * ullage)/100