# falto el profe y los pibes van a armar la clase.

# pedir el nombre y la edad de los compañeros que vinieron hoy a clase.
#ejecutando un for para pedir informacion de cada compañero
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
          nombre = input("ingrese el nombre del compañero")
          edad = int(input("ingrese la edad del compañero"))
          compañero = (nombre, edad)
          
          #agregando la informacion a la lista
          compañeros.append(compañero)
          
          #ordenandolos de menor a mayor segun su edad 
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros [x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre para definir al asistente y profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos la tupla
    return asistente,profesor

#desempaquteamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#muestra el resultado
print(f"El profesor es: {profesor} y su asistente es {asistente}")
    
    
    
# compañeros.sort(): La función .sort() ordena la lista en su lugar,
# es decir, modifica la lista original compañeros en lugar de crear una nueva.
# Por defecto, ordena en orden ascendente.

# key=lambda x: x[1]: Este argumento indica a .sort() cómo debe ordenar los elementos de la lista.

# lambda x: x[1] es una función anónima (también llamada lambda) que toma cada elemento x de la lista compañeros.
# Cada elemento x en compañeros es una tupla (nombre, edad), por lo que x[1] accede al segundo valor de cada tupla, que es la edad.

# Así, .sort(key=lambda x: x[1]) organiza los elementos en compañeros según la edad de menor a mayor.
