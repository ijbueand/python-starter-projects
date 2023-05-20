# Examen Final Programación en Python
# Isaías Jesús Bueno Andrades

#%% Ejercicio 1
def unfold(lista):
    resultado = []
    def flatten(lista):
        for item in lista:
            if type(item) == list:
                flatten(item)
            else:
                resultado.append(item)
    flatten(lista)
    return resultado

unfold([1, 2, [3, [4, 5, [5, 6]]]])


#%% Ejercicio 2
     
def training():
    
    '''
    Esta función recoge la distancia recorrida en km
    y el tiempo tomado en min de varias sesiones de
    entrenamiento e imprime en pantalla la velocidad media.
    '''

    dist = 0
    temp = 0
    num_tr = 1
    while True:
        disti = input('Introduzca la distancia recorrida en km: ')
        tempi = input('Introduzca el tiempo tomado en min: ')
        if disti == '' or tempi == '':
            break
        elif float(tempi) > 15:
            num_tr += 1
            try:
                dist += float(disti)
                temp += float(tempi)/60
            except:
                continue
        else:
            continue
    media = dist/temp
    print('\nUsted ha hecho %d entrenamientos con una media de %.2f km/h' % (num_tr, media))
        
training()    

#%% Ejercicio 3

usuarios = {'ijbueand': {'Nombre': 'Isaías', 'Apellidos': 'Bueno Andrades', 'Nick': 'ijbueand', 'Password': 'caca26sand'}}
#nickname

def crea_usuario():
    
    global usuarios
    
    first_name = input('Introduzca su primer nombre: ')
    second_name = input('Introduzca sus apellidos: ')
    
    while True:
        nickname = input('Introduzca un nickname: ')
        if nickname in usuarios:
            print('Está repetido, inténtalo otra vez...')
            continue
        else:
            break
        
    while True:
        passw1 = input('Introduzca una clave con letras y números: ')
        passw2 = input('Repita su clave: ')
        if passw1 == passw2 and passw1.isalpha() == False and passw1.isnumeric() == False and passw1.isalnum() == True:
            break
        else:
            print('Hay un fallo, inténtalo otra vez...')
            continue
        
    usuarios[nickname] = {'Nombre': first_name, 'Apellidos': second_name, 'Nick': nickname, 'Password': passw1}
    
    return

crea_usuario()
    
#%% Ejercicio 4
        
# Como lo hice con el módulo unicode

# def rima_consonante(palabra, n = 4):
#     import unidecode
#     lista_rimas = []
#     for linea in open('palabras.txt', 'r', encoding=('utf8')):
#         linea = unidecode.unidecode(linea.rstrip())
#         if linea[-n] == palabra[-n]:
#             lista_rimas.append(linea)
#     return lista_rimas

def rima_consonante(palabra, n = 4):
    lista_rimas = []
    for linea in open('palabras.txt', 'r', encoding=('utf8')):
        linea = linea.rstrip().lower()
        if linea[-n:] == palabra[-n:]:
            lista_rimas.append(linea)
    return lista_rimas

def vocales(palabra):
    
    lista_vocales = []
    for letra in palabra:
        if letra in 'aeiouáéíóú':
            lista_vocales.append(letra)
            
    return ''.join(lista_vocales)
            
def rima_asonante(palabra, n = 3):
    lista_rimas = []
    palabra_solo_vocales = vocales(palabra)
    for linea in open('palabras.txt', 'r', encoding=('utf8')):
        linea = linea.rstrip().lower()
        linea_solo_vocales = vocales(linea)
        if linea_solo_vocales[-n:] == palabra_solo_vocales[-n:]:
            lista_rimas.append(linea)
    return lista_rimas

rima_consonante('pelícanos')
rima_asonante('pelícanos')

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
