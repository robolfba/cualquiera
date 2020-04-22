lista_inicial = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
lista_nueva = []
print (lista_inicial)
for i in lista_inicial:
    name, space, tupla = i.partition(" ")
    x = int(tupla.split(',')[0]) #asignamos a x el primer valor de tupla y lo convertimos a int
    y = int(tupla.split(',')[1]) #idem pero con y
    tuple = (x,y) #Asignamos una variable tupla
    lista_nueva.extend([tuple]) #agregamos tupla a la lista
print('sin orden:' ,lista_nueva)
print(sorted(lista_nueva))

# La dificultad que me surgio en este ejercicio, fue que al momento de comparar los numeros, para ordenarlos,
# solo utilizaba el primer digito, por lo tanto (en este caso), el numero mayor ('410,134') no quedaba en ultimo
# lugar. Entendi que el problema en la comparacion estaba en que el numero no era un entero, sino un string.
# Lo resolvi, copiando los valores dentro de una tupla y conviritiendolos a enteros. De esta forma la comparacion
# se pudo realizar.