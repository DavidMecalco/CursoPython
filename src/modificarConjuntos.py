set_countries = {'col', 'mex', 'bol'}
#Len es para mostrar el tamaño del conjunto, arreglo
size = len(set_countries)
print(size)

#para saber si se encuentra en espeficico de un elemento
print('col' in set_countries)

#agregar elemento al conjunto
set_countries.add('pe')
print(set_countries)

#En los conjuntos no se pueden agregar dos veces el mismo elemento
set_countries.add('pe')
print(set_countries)

#Actualizar un conjunto
set_countries.update({'ar', 'ecua'})
print(set_countries)

#elemintar un elemento del conjunto
set_countries.remove('col')
print(set_countries)

set_countries.discard('arg')
print(set_countries)

#La diferencia entre remove y discard es que si no se enuentra el elemento
#remove, nos dara un error de indexación y discard, omitara si no se encuentra el elemento

#limpiar todo el conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))