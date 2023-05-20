# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:17:05 2022

@author: Isaías Bueno
"""
# Importamos las librerías que necesitemos.
import datetime

# Definimos las funciones que vayamos a usar.
def print_menu():
    print('\nIngredientes:')
    # Mostramos todos los ingredientes del tipo con su precio
    # y con un número para elegirlo.
    for n in ingredientes[tipo]:
        print('%d. %s por %.2f€' % (n, ingredientes[tipo][n]['Nombre'], ingredientes[tipo][n]['Precio']))
    return

# Creamos el archivo de escritura y le ponemos cabecera.
ped = open('pedidos.txt','w')
ped.write('HISTORIAL DE PEDIDOS\n')

# Imprimimos cabecera para el ususario y comenzamos bucle for
# para poder registrar todos los pedidos que el cliente quiera.
print('='*50 + '\n' + '\t\tBIENVENIDOS A PIZZAS ALESSANDRO!' + '\n' + '='*50)
stop = False
total = 0.0
while not stop:
    try:
        now = datetime.datetime.now()
        
        # Creamos un diccionario con los ingredientes y su precio,
        # bajo un indicador numérico que agilizará el proceso de selección.
        # Así es más fácil añadir en un futuro.
        ingredientes = {1: # Aquí van los vegetarianos.
                        {1: {'Nombre': 'Pimiento', 'Precio': 1}, 
                         2: {'Nombre': 'Tofu', 'Precio': 1.5}, 
                         3: {'Nombre': 'Setas', 'Precio': 1}}, 
                        2: # Aquí van los no vegetarianos.
                        {1: {'Nombre': 'Pepperoni', 'Precio': 1}, 
                         2: {'Nombre': 'Jamón', 'Precio': 2}, 
                         3: {'Nombre': 'Salmón', 'Precio': 3}}}
        
        # Pedimos al usuario el tipo de pizza.
        while True:
            print('\nTipos de pizzas disponibles... \n1. Vegetariana \n2. No vegetariana')
            tipo = int(input('\nIntroduzca el número de la que desee: '))
            if tipo not in ingredientes:
                print('\nNo ha seleccionado un tipo existente. Inténtelo de nuevo...')
            else: break
        
        # Pedimos al usuario los ingredientes que quiera.
        print('\nUsted puede elegir hasta 2 ingredientes...')
        ing1, ing2 = 0, 0
        while True:
            print_menu()
            ing1 = int(input('\nIntroduzca el número del primer ingrediente: '))
            if ing1 in ingredientes[tipo]:
                while True:
                    otro_ing = input('\n¿Desea otro ingrediente? (S/N): ')
                    otro_ing = otro_ing.upper()
                    if otro_ing == 'S':
                        print_menu()
                        ing2 = int(input('\nIntroduzca el número del segundo ingrediente: '))
                        # Calculamos el precio de la pizza sabidos los ingredientes.
                        subtotal = (8 + float(ingredientes[tipo][ing1]['Precio']) + float(ingredientes[tipo][ing2]['Precio']))
                        break
                    elif otro_ing == 'N':
                        # Calculamos el precio de la pizza sabidos los ingredientes.
                        subtotal = (8 + float(ingredientes[tipo][ing1]['Precio']))
                        break
                    else: 
                        print('No le he entendido. Repita otra vez...')
                break
            else:
                print('Ingrediente no existente. Pruebe de nuevo...')
                
        # Creamos diccionario de descuentos para poder modificarlo en un futuro.
        descuentos = {1: 0.2, 2: 0.05}
        # Aplicamos los descuentos.
        subtotal *= (1 - descuentos[tipo])
        # Sumamos el subtotal al total
        total += subtotal
        # Guardamos el registro codificado de lo que ha sido pedido
        ped.write('\nFECHA-HORA: %s - ID: %d%d%d - PRECIO: %.2f€' % (now, tipo, ing1, ing2, subtotal))   
        # Mostramos en pantalla cuánto lleva por ahora
        print('\nTotal por ahora: %.2f' % total)
        
        # Preguntamos si quiere otra pizza
        while True:
            otra_piz = input('\n¿Desea otra pizza? (S/N): ')
            otra_piz = otra_piz.upper()
            if otra_piz == 'S':
                print('\n'+'='*60)
                break # Si quiere otra, salimos de este bucle y volvemos al principal
            elif otra_piz == 'N':
                print('\nMuchas gracias por su compra! El total a pagar es %.2f€ \nTardará unos 30 minutitos en llegar.' % total)
                print('\n'+'='*60)
                stop = True
                ped.close()
                break # Si no quiere otra, salimos de este bucle y del principal
            else: 
                print('No le he entendido. Repita otra vez...')
    
    except:
        continue # Para evitar posibles errores como que introduzcan un caracter donde
                 # debería ir un int. En ese caso vuelven al comienzo...
    