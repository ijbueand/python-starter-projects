'''
Los datos han sido recogidos en la finca
experimental #2 de la cooperativa APRO,
en Asunción (Paraguay).
'''

# Creamos los atributos correspondientes al set de datos
ciudad = 'Asunción'
finca = 2
cooperativa = 'APRO'

def consulta_dia(display = False):
    
    '''
    Pide al usuario introducir un año, mes y día, y devuelve
    una lista con las medidas de ese día. 
    Además, si display = True, se muestra por pantalla un 
    listado con todas las medidas que se han realizado ese día.
    '''
    
    global hms # Definimos hms como global para poder imprimirla más tarde fuera de la función
    hms = input('\nIntroduzca un año, mes y día (ej. 01-Jun-2022): ')
    lst = []
    for line in open('sensor_data.txt'):
        if hms in line:
            lst.append(line) # Recorremos el fichero y almacenamos en una variable las líneas que cumplan la condición
    if display == True:
        for items in lst:
            split_items = items.split(' ')
            print('%s --> %s' % (split_items[1], split_items[2]), end = '') # Imprime los resultados si display es True
    
    return lst

def consulta_media_dia():
    
    '''
    Pide al usuario introducir un año, mes y día, y devuelve
    la medición media para ese día.
    '''
    
    lst = consulta_dia() # Llamamos a la primera función
    medidas = []
    for items in lst:
        split_items = items.split(' ') # Separamos por espacios para quedarnos con las medidas
        medidas.append(float(split_items[2]))  
    avg = sum(medidas)/len(medidas) # Calculamos la media
    
    return avg

def calibra_medida(x, a = 0.012, b = 0.4):
    
    '''
    Recibe una medida x cruda (en mV) y devuelve su traducción
    a valor de humedad h (%). 'a' y 'b' son parámetros experimentales
    con un valor por defecto que se puede ajustar.
    '''

    h = 100 * (a * x + b)
    
    return h

def consulta_media_dia_cal():
    
    '''
    Pide al usuario introducir un año, mes y día, y devuelve
    la medición media para ese día en valor de humedad h (%).
    '''
    
    x = consulta_media_dia()
    cal_avg = calibra_medida(x)
    
    return cal_avg
    
def consulta_riego():
    
    '''
    Pide al usuario introducir un año, mes y día, y devuelve
    el número de riegos para ese día.
    '''
    
    import scipy as sp # Importamos la librería scipy para usar luego find_peaks
    lst = consulta_dia()
    medidas = []
    for items in lst:
        split_items = items.split(' ')
        medidas.append(float(split_items[2]))
    
    # La función find_peaks nos va a encontrar los picos en las medidas.
    # Devuelve los índices de los picos en la lista.
    # Ponemos la prominencia en 2.5 para que sólo recoja los picos debidos
    # a los riegos y no al ruido.
    # Los datos que nos interesan están en riegos[0], ya que en riegos[1]
    # la función crea un diccionario que no nos interesa.
    
    riegos = sp.signal.find_peaks(medidas, prominence = 2.5)
    
    print('\nEl día %s se realizaron %d riegos:\n' % (hms, len(riegos[0])))
    n = 1
    for index in riegos[0]:
        split_items = lst[index].split(' ')
        hora = split_items[1]
        print('- Riego %d a las %s' % (n, hora))
        n += 1
    
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    