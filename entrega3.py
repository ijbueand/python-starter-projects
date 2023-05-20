# MÉTODOS DE MONTECARLO PARA EL CÁLCULO DEL ÁREA DE POLÍGONOS IRREGULARES
# Bueno Andrades, Isaías Jesús
# Camacho Vázquez, Jaime

# Importamos las librerías que necesitemos y definimos las funciones que vamos a usar
import random
import numpy as np

def cross_prod_sign(array_vectors, array_dist_vectors, point): # Como inputs tenemos la lista con los vértices, la lista con los vectores distancia (vértice-vértice) y el punto para ver si está in or out
    dist_vp = [] # Variable local para almacenar la distancia vértice-punto
    for ver in v:
        dist_vp.append(np.subtract(ver, point)) # Calculamos el vector distancia vértice-punto
    sign_array = np.sign(np.cross(array_dist_vectors, dist_vp)) # Hacemos la multiplicación vectorial para cada par de vector distancia y vector vértice-punto
    return sign_array # Nos devuelve una lista con +1, -1 o 0 (si hay un 0 vamos a considerar que el punto está fuera)

# Pedimos el número de vértices
print('='*50)
num_ver = int(input('\n¿Cuántos vértices tiene su polígono?: '))

# Pedimos las coordenadas de los vértices y las guardamos en una lista
print('\nA continuación, se le va a pedir las coordenadas de los vértices...')
v = []
for ver in range(num_ver):
    temp_x = float(input('\nIntroduzca la coordenada en X del vértice %d: ' % (ver+1)))
    temp_y = float(input('Introduzca la coordenada en Y del vértice %d: ' % (ver+1)))
    v.append([temp_x, temp_y])

# Calculamos los vectores que unen las aristas
l = []

for ver in range(num_ver):
    if ver != num_ver-1: # Para los primeros
        l_temp = []
        for item1, item2 in zip(v[ver], v[ver+1]):
            item = item1 - item2
            l_temp.append(item)
        l.append(l_temp)
    else: # Para el último que tiene que restar el primero
        l_temp = []
        for item1, item2 in zip(v[ver], v[0]):
            item = item1 - item2
            l_temp.append(item)
        l.append(l_temp)
        
# La resta de vectores se puede hacer de forma mucho más sencilla
# con la librería numpy y la función subtract. Sin embargo, antes
# de descubrir la librería ingeniamos esta forma para restar y 
# decidimos, al menos, conservarla en esta parte del código para
# dejar constancia de otra forma de proceder.
        
# Queremos generar puntos aleatorios dentro de la cuadrícula

# La cuadrícula tiene que contener el polígono, recogiendo el min(x,y) y el max(x,y)
xs = []
ys = []
for ver in range(num_ver): 
    xs.append(v[ver][0])
for ver in range(num_ver): 
    ys.append(v[ver][1])
    
# La cuadrícula va a ser [min_x-1, max_x+1][min_y-1, max_y+1]
min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)

# Ya podemos generar puntos aleatorios dentro de la cuadrícula
points = 100000
x_points = []
y_points = []
for _ in range(points):
    x_points.append(random.random() * (max_x-min_x) + min_x)
for _ in range(points):
    y_points.append(random.random() * (max_y-min_y) + min_y)
xy_points = zip(x_points, y_points) 

# Vemos si los puntos están dentro o fuera de la figura y hacemos un conteo
point_in = 0
point_out = 0
for point in xy_points:
    sign = cross_prod_sign(v, l, point)
    i = 0
    while i < (num_ver - 1):
        if sign[i] == sign[i+1]: # Para el algoritmo, un punto con signo 0 estaría fuera de la figura. Tiene que estar estríctamente dentro para contarse positivo
            if i == (num_ver - 2):
                point_in += 1
            i += 1
        else:
            point_out += 1
            break

# Calculamos el área de la figura
p = point_in/(point_in+point_out)
a_total = (max_x-min_x)*(max_y-min_y)
a_figura = p * a_total

# Imprimimos el resultado
print('\nEl área de su figura es de %.2f unidades al cuadrado' % a_figura)
print('\n'+'='*50)



    

    