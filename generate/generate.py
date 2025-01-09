class generate():
    def __init__():

        # Q = Axv
        # Q = caudal (m³/s o L/s)
        #𝐴 es el área de la sección transversal del conducto (m² o cm²)
        # 𝑣 es la velocidad del fluido (m/s o cm/s)

        # caudal_ent: caudal entrada
        # caudal_sal: caudal salida
        caudal_ent = lambda v, t: v/t
        caudal_sal = lambda v, t: v/t

        #Velocidad de llenado: Si sabes el diámetro de la manguera que se 
        # usa para llenar el tanque, puedes calcular la velocidad a la 
        # que fluye la gasolina.

        # Costo total: Conociendo el precio de la gasolina por litro y el 
        # volumen total, puedes calcular el costo total de llenar el tanque.

        # costo_total = VxP
        # V = volumen (L)
        # P = precio gasolina por litro (USD/L)
        total_cost = lambda v, p: v*p
        
        # Eficiencia del tiempo: Puedes analizar cuánto tiempo toma llenar 
        # diferentes tamaños de tanques con diferentes caudales y encontrar 
        # la manera más eficiente de hacerlo.

        # Consumo de energía: Si el proceso de llenado incluye el uso de una 
        # bomba, puedes calcular el consumo de energía necesario para llenar el tanque.