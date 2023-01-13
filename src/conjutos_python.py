#Los sets en Python son una estructura de datos usada para almacenar elementos de una manera similar a las listas
#pero con ciertas diferencias.

#Los elementos de un set son único, lo que significa que no puede haber elementos duplicados.

#Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.}

#Sus elementos deben ser inmutables.

#Para entender mejor los sets, es necesario entender ciertos conceptos matemáticos como la teoría de conjuntos.

#Para crear un set en Python se puede hacer con set() y pasando como entrada cualquier tipo iterable, como puede ser una lista. 
# Se puede ver como a pesar de pasar elementos duplicados como dos 8 y en un orden determinado, 
#al imprimir el set no conserva ese orden y los duplicados se han eliminado.

# no tiene un par key-value, así me doy cuenta que es un set, un conjunto.
set_countries = {'col', 'mex', 'bol'}
print (set_countries)

# si yo pongo algo repetido, él me lo quita al imprimir
set_countries2 = {'col', 'mex', 'bol', 'col'}
print (set_countries2) # {'col', 'mex', 'bol'}

# puede ser mixto. El set se ordena solo, lo importante es lo que tengo dentro.
set_types = {1, 'hola', False, 12.12}
print(set_types) # {False, 1, 12.12, 'hola'}

# la podemos crear a partir de un string
set_from_string = set('hoola')
print (set_from_string) # {'a', 'l', 'o', 'h'}

# la podemos crear a partir de una tupla
set_from_tuples = set (('abc','cbv','as','abc'))
print (set_from_tuples) # {'as', 'abc', 'cbv'}

# la podemos crear a partir de una lista
numbers = [1,2,3,1,2,3,4]
set_numbers= set(numbers)
print (set_numbers) # {1, 2, 3, 4}
# si quiero convertir este set único a una lista, lo puedo hacer:
unique_numbers = list(set_numbers)
print (unique_numbers)