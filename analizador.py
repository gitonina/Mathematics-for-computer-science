# -*- coding: utf-8 -*-
"""Tarea 3 discretas.ipynb

Automatically generated by Colaboratory.


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    return lineas

import re

def same_group(line1, line2):
    # Verificar si ambas líneas contienen "=" o "print"
    if re.search(r'=|print', line1) and (re.search(r'=|print', line2) or re.search(r'if', line2)): # While ?
        # Obtener la indentación de las líneas
        indent1 = len(line1) - len(line1.lstrip())
        indent2 = len(line2) - len(line2.lstrip())

        # Verificar si las líneas tienen la misma indentación
        if indent1 == indent2:
            return True

    return False

# Función para obtener los nodos de líneas
def obtener_nodos(lineas):
    # lineas = [elemento.strip() for elemento in lineas if elemento.strip()]
    nodos = []
    nodo_actual = []

    for i in range(len(lineas) - 1):
        if same_group(lineas[i], lineas[i + 1]):
            nodo_actual.append(lineas[i])
        else:
            nodo_actual.append(lineas[i])

            # Excluir el bloque "else" como nodo independiente
            if not re.search(r'else', lineas[i]):
                nodos.append(nodo_actual)

            nodo_actual = []

    # Agregar la última línea al último nodo
    nodo_actual.append(lineas[-1])

    # Excluir el bloque "else" como nodo independiente
    if not re.search(r'else', lineas[-1]):
        nodos.append(nodo_actual)

    return nodos

def contar_arcos(nodos):
    cantidad_nodos = len(nodos)
    cantidad_arcos = cantidad_nodos

    for nodo in nodos:
        if any(re.search(r'if|while', linea) for linea in nodo):
            cantidad_arcos += 1

    return cantidad_arcos

def crear_grafo(nodo_lista): # Arreglar !!
    grafo = {}

    for i in range(len(nodo_lista)):
        nodo = i + 1
        ultimo_nodo = len(nodo_lista)
        grafo[nodo] = []

        if any("if" in code for code in nodo_list[i]):
            next_nodo = i + 1

            if next_nodo < len(nodo_list):
                grafo[nodo].append(next_nodo + 1)

                # Arreglar
                if next_nodo + 2 < len(nodo_list) and any("if" in code for code in nodo_list[next_nodo + 1]):
                    grafo[nodo].append(next_nodo + 6)

                elif next_nodo + 1 < len(nodo_list) and any("if" in code for code in nodo_list[next_nodo]):
                    grafo[nodo].append(next_nodo + 4)

                else: grafo[nodo].append(next_nodo + 2)

        else: # Arreglar :(
          if nodo != ultimo_nodo:
            grafo[nodo].append(ultimo_nodo)

    return grafo

# Ejemplo
nodo_list = [
    ['x = 0', 'if es_especial(x):'],
    ['    x = 5'],
    ['    y = 5'],
    ['print(x + y)']
]


# Definir el grafo
grafo = crear_grafo(nodo_list)

# Imprimir el grafo
for nodo, connections in grafo.items():
    print(f"nodo {nodo}: Conexiones {connections}")


# Lo saqué de Chat GPT
def dfs(grafo, inicio, fin, camino=[]):
    camino = camino + [inicio]  # Agregar el nodo actual al camino

    if inicio in fin:  # Si se alcanza uno de los nodos finales, añadir el camino al resultado
        return [camino]

    if inicio not in grafo:  # Si el nodo no está en el grafo, retornar camino vacío
        return []

    caminos = []  # Almacenar todos los caminos posibles

    for nodo in grafo[inicio]:  # Explorar los nodos adyacentes
        if nodo not in camino:  # Evitar ciclos en el grafo
            new_caminos = dfs(grafo, nodo, fin, camino)  # Llamada recursiva para encontrar caminos
            caminos.extend(new_caminos)  # Agregar los caminos encontrados al resultado

    return caminos


# Definir los nodos de inicio y fin
inicio_nodo = 1 # Siempre el primero
fin_nodos = [node for node, connections in grafo.items() if not connections] # Los que no tienen conexiones (obviar Nodo fin)

# Encontrar todos los caminos posibles
all_caminos = dfs(grafo, inicio_nodo, fin_nodos)

# Imprimir todos los caminos encontrados
for camino in all_caminos:
    print(camino)

print(all_caminos)

for camino in all_caminos:
    nodos_seleccionados = [nodo_list[nodo-1] for nodo in camino]
    print(nodos_seleccionados)

lista = obtener_nodos(lineas3)

print(lista)

variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','(a', '(b', '(c', '(d', '(e', '(f', '(g', '(h', '(i', '(j', '(k', '(l', '(m', '(n', '(o', '(p', '(q', '(r', '(s', '(t', '(u', '(v', '(w', '(x', '(y', '(z', 'a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)', 'h)', 'i)', 'j)', 'k)', 'l)', 'm)', 'n)', 'o)', 'p)', 'q)', 'r)', 's)', 't)', 'u)', 'v)', 'w)', 'x)', 'y)', 'z)', '(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)', '(j)', '(k)', '(l)', '(m)', '(n)', '(o)', '(p)', '(q)', '(r)', '(s)', '(t)', '(u)', '(v)', '(w)', '(x)', '(y)', '(z)']


def encontrar_variables_indefinidas(lista):
    variables_definidas = set()
    variables_usadas = set()
    variables_indefinidas = []
    listas_indefinidas = []

    for sublist in lista:
        for item in sublist:
            if "=" in item:
                for letra in item:
                  if letra in variables:
                    variables_definidas.add(letra)

            else:
                for item in sublist:
                   palabras = item.split()
                   for letra in palabras:
                    if letra in variables:
                       variables_usadas.add(letra)

        variables_usadas = {elem.replace('(', '').replace(')', '') for elem in variables_usadas}

        vi = list(variables_usadas - variables_definidas)
        variables_indefinidas += vi
        listas_indefinidas.append(sublist)

    return variables_indefinidas

def encontrar_variables_indefinidas_por_lista(listas):
    variables_indefinidas_por_lista = []

    for lista in listas:
        variables_indefinidas = encontrar_variables_indefinidas(lista)
        if variables_indefinidas:
            variables_indefinidas_por_lista.append((variables_indefinidas, lista))

    return variables_indefinidas_por_lista

listas = [
    [['x = 0', 'if es_especial(x):'], ['    x = 5'], ['print(x + y)']],
    [['x = 0', 'if es_especial(x):'], ['    y = 5'], ['print(x + y)']]
]

variables_indefinidas_por_lista = encontrar_variables_indefinidas_por_lista(listas)

for variables_indefinidas, camino in variables_indefinidas_por_lista:
    print("Variables indefinidas:", variables_indefinidas)
    print("Camino:", camino)

lineas1 = [
    "x = 1",
    "print(x)"
]

lineas2 = [
    "x = 5",
    "y = x + 2",
    "z = f(x, y)",
    "print(x + y + z)"
]

lineas3 = [
    "x = 0",
    "if x > 5:",
    "    y = 3",
    "else:",
    "    y = 4"
]

lineas4 = [
    "x = 0",
    "while x < 10:",
    "    print(x)",
    "    x = x + 1",
    "y = x + 3"
]

lineas5 = [
    "x = 0",
    "while x < 10:",
    "    if x > 5:",
    "        print(x)",
    "    else:",
    "        print('x es menor que 6')",
    "    x = x + 1"
]

lineas6 = [
    "x = 0",
    "if es_especial(x):",
    "    x = 5",
    "else:",
    "    y = 5",
    "print(x + y)"
]

nodos1 = obtener_nodos(lineas1)
nodos2 = obtener_nodos(lineas2)
nodos3 = obtener_nodos(lineas3)
nodos4 = obtener_nodos(lineas4)
nodos5 = obtener_nodos(lineas5)
nodos6 = obtener_nodos(lineas6)

# Imprimir los nodos
print("nodos del código 1:")
for i, nodo in enumerate(nodos1):
    print(f"nodo {i+1}:")
    for linea in nodo:
        print(linea)
    print()

print("nodos del código 2:")
for i, nodo in enumerate(nodos2):
    print(f"nodo {i+1}:")
    for linea in nodo:
        print(linea)
    print()

print("nodos del código 3:")
for i, nodo in enumerate(nodos3):
    print(f"nodo {i+1}:")
    for linea in nodo:
        print(linea)
    print()

print("nodos del código 4:")
for i, nodo in enumerate(nodos4):
    print(f"nodo {i+1}:")
    for linea in nodo:
        print(linea)
    print()

print("nodos del código 5:")
for i, nodo in enumerate(nodos5):
    print(f"nodo {i+1}:")
    for linea in nodo:
        print(linea)
    print()

print("nodos del código 6:")
for i, nodo in enumerate(nodos6):
    print(f"nodo {i+1}:")
    for linea in nodo:
        print(linea)
    print()

cantidad_nodos1 = len(nodos1) + 1
cantidad_nodos2 = len(nodos2) + 1
cantidad_nodos3 = len(nodos3) + 1
cantidad_nodos4 = len(nodos4) + 1
cantidad_nodos5 = len(nodos5) + 1
cantidad_nodos6 = len(nodos6) + 1

arcos1 = contar_arcos(nodos1)
arcos2 = contar_arcos(nodos2)
arcos3 = contar_arcos(nodos3)
arcos4 = contar_arcos(nodos4)
arcos5 = contar_arcos(nodos5)
arcos6 = contar_arcos(nodos6)

# Complejidad ciclomatica = arcos - nodos + 2 * componentes conexos
complejidad1 = arcos1 - cantidad_nodos1 + 2
complejidad2 = arcos2 - cantidad_nodos2 + 2
complejidad3 = arcos3 - cantidad_nodos3 + 2
complejidad4 = arcos4 - cantidad_nodos4 + 2
complejidad5 = arcos5 - cantidad_nodos5 + 2
complejidad6 = arcos6 - cantidad_nodos6 + 2

componentes = 1

print(f"Cantidad de nodos del código 1: {cantidad_nodos1}")
print(f"Cantidad de nodos del código 2: {cantidad_nodos2}")
print(f"Cantidad de nodos del código 3: {cantidad_nodos3}")
print(f"Cantidad de nodos del código 4: {cantidad_nodos4}")
print(f"Cantidad de nodos del código 5: {cantidad_nodos5}")
print(f"Cantidad de nodos del código 6: {cantidad_nodos6}")

print()

print(f"Cantidad de arcos del código 1: {arcos1}")
print(f"Cantidad de arcos del código 2: {arcos2}")
print(f"Cantidad de arcos del código 3: {arcos3}")
print(f"Cantidad de arcos del código 4: {arcos4}")
print(f"Cantidad de arcos del código 5: {arcos5}")
print(f"Cantidad de arcos del código 6: {arcos6}")

def analizar():
  nombre_archivo = input("Archivo: ")
  lineas = leer_archivo(nombre_archivo) # Abrir archivo

  nodos = obtener_nodos(lineas) # Obtener lista con todos los nodos por separado

  cantidad_nodos = len(nodos) + 1 # Número de nodos
  cantidad_arcos = contar_arcos(nodos) # Número de arcos
  complejidad = cantidad_arcos - cantidad_nodos + 2 # Complejidad
  componentes = 1 # El número de componentes conexos siempre será 1

  grafo = crear_grafo(nodos) # Crear un grafo con los nodos
  inicio_nodo = 1
  fin_nodos = [node for node, connections in grafo.items() if not connections]
  todos_los_caminos = dfs(grafo, inicio_nodo, fin_nodos) # Encontrar todos los caminos posibles
  variables_indefinidas_por_camino = encontrar_variables_indefinidas_por_lista(todos_los_caminos) # Buscar variables indefinidas en cada camino

  print("CFG")
  print("Nodos:", cantidad_nodos)
  print("Arcos:", cantidad_arcos)
  print("Componentes conexos:", componentes)
  print("Variables indefinidas")
  for variables_indefinidas, camino in variables_indefinidas_por_camino:
      print("Variables indefinidas:", variables_indefinidas)
      print("Camino:", camino)
  print("Complejidad ciclomática")
  print(complejidad)
