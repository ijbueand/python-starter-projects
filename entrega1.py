#%% EJERCICIO 1.A
print('Escriba una duración y recíbala en segundos...\n')
d = int(input('¿Cuántos días duró?: '))
h = int(input('¿Cuántas horas duró?: '))
m = int(input('¿Cuántos minutos duró?: '))
s = int(input('¿Cuántos segundos duró?: '))
S = s + m*60 + h*3600 + d*86400 # Pasamos todo a segundos y lo sumamos
print('\nEl resultado corresponde a ' + str(S) + ' segundos.')

#%% EJERCICIO 1.B
s = int(input('Escriba una duración en segundos y recíbala en DD:HH:MM:SS... '))
d = s//86400 # Nos quedamos con la parte entera
r = s%86400 # Almacenamos el resto para convertirlo en horas
h = r//3600 # Seguimos con la cadena hasta llegar a segundos
r = r%3600
m = r//60
r = r%60
s = r # El resto serían los segundos
t = str(d) + ':' + str(h) + ':' + str(m) + ':' + str(r)
print('\nEl resultado es ' + t )

#%% EJERCICIO 2.A
stop = False
suc = [0,1] # Creamos la sucesión con los dos primeros términos
while not stop:
    N = int(input('Entregue un entero N mayor que 2 para generar una lista con los N primeros términos de la sucesión de Fibonacci: '))
    if N > 2:
        for i in range(2,N):
            suc.append(suc[i-2]+suc[i-1])
        print('El resultado es:', suc)
        stop = True # Si se introduce un número correcto y se ejecuta el if, acaba el while
    else:
        print('Su número no es mayor que 2. Inténtelo de nuevo...\n')
        # Se repetiría el while para dar otra oportunidad al usuario

#%% EJERCICIO 2.B
phi_real = (1+5**.5)/2
suc = [0,1] # Creamos la sucesión con los dos primeros términos
for i in range(2,52):
    suc.append(suc[i-2]+suc[i-1])
phi_estimated = suc[51]/suc[50]
print('El número aureo real es ' + str(phi_real) + ', mientras que el estimado es ' + str(phi_estimated) + ', con un error absoluto de aproximación de ' + str(abs(phi_real-phi_estimated)))

#%% EJERCICIO 3
stop = False
while not stop: # Bucle while para repetir si el número es incorrecto
    n = float(input('Introduzca un número natural para calcular su factorial: '))
    factorial = 1 # Por defecto 1, que es el factorial de 0 y 1
    if n%1 == 0 and n >= 0: # Los naturales tienen resto 0 al dividirse entre 1 y son positivos
        n = int(n) #Convertimos el float en int para poder usarlo en el rango
        if n == 0 or n == 1:
            print('El factorial de su número es', factorial)
            stop = True
        else:
            for i in range(1,n+1):
                factorial *= i
            print('El factorial de su número es', factorial)
            stop = True # Acabamos el bucle while
    else: 
        print('Su número no es natural... Inténtelo de nuevo...\n')

#%% EJERCICIO 4

print('Introduzca su secuencia de movimiento como el ejemplo: "UP 3, RIGHT 4, DOWN 2, RIGHT 2, UP 3"')
o_seq = input('Secuencia: ')
s_seq = o_seq.split(' ') # Separamos por los espacios
d_list = [d for d in s_seq[::2]] # Almacenamos las direcciones (impares en s_seq)
m_list = [s for s in s_seq[1::2]] # Almacenamos los módulos (pares en s_seq)
m_list = [m_list[i].replace(',','') for i in range(len(m_list))] # Eliminamos las comas si las hubiese para luego poder convertir en int
position = [0,0] # Partimos de la posición (0,0), con el eje X a la izq. y el Y a la der.
for i in range(len(m_list)):
    if d_list[i] == 'RIGHT': 
        position[0] += int(m_list[i])
    elif d_list[i] == 'LEFT': 
        position[0] -= int(m_list[i])
    elif d_list[i] == 'UP': 
        position[1] += int(m_list[i])
    elif d_list[i] == 'DOWN': 
        position[1] -= int(m_list[i])
print('Su posición actual es [X, Y]: ', position)
    
#%% EJERCICIO 5
    
string = input('Introduzca lo que quiera: ')
string = string.lower() # Para que sea insensible a mayúsculas y minúsculas
string = string.replace(' ', '') # Para que no cuente los espacios, sólo las letras
abc = {}
for i in string:
    if i not in abc: # Si no está la letra en el diccionario, creamos esa key
        abc[i] = 1
    else: # Si sí está, le sumamos uno
        abc[i] += 1
print('Recuento de letras:')
for letra in abc: # Lo imprimimos bonito como en el enunciado con un bucle
    print(str(letra) + ',' + str(abc[letra]))
        









