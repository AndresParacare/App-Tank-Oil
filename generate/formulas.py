from dataclasses import dataclass

@dataclass
class formulas:
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

    """"""