# MCOC2021-P3

 ![🚙_Evaluación_de_Américo_Vespucio_Oriente](https://user-images.githubusercontent.com/88337732/140409349-f666b07a-462f-4a1c-8f28-d169b6601609.png)
 
### Grupo: 
- 4
### Integrantes:
- José Luis Larenas
- Santiago Dussaillant
- Pablo Simón

## Entrega 2

A continuación, en las Figuras 1 a 4, se presentan los resultados obtenidos al correr el código ```p3e2.py```. Para las Figuras 2 a 4, el camino óptimo se ve representado por las líneas rojas, y el tiempo en recorrer dicho camino se encuentra en el título de cada figura.

<p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%202/fig1.png">
  <br><br>
  <b>Figura 1: Mapa de Ciudades.</b><br>
  <br><br>
 </p>
 
  <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%202/fig2.png">
  <br><br>
  <b>Figura 2: Camino Óptimo de 0 a 9.</b><br>
  <br><br>
 </p>
 
  <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%202/fig3.png">
  <br><br>
  <b>Figura 3: Camino Óptimo de 4 a 5.</b><br>
  <br><br>
 </p>
 
  <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%202/fig4.png">
  <br><br>
  <b>Figura 4: Camino Óptimo de 0 a 4.</b><br>
  <br><br>
 </p>
 
_Nota: Figuras 1-4 se encuentran en la carpeta "Figuras Entrega 2"._

## Entrega 3

A continuación, en las Figuras 5 a 7, se presentan los resultados obtenidos al correr los códigos ```p3e3_grupo04_apellido.py``` entregados por Canvas. Las zonas centrales están de color rojo suave (#FFB2B2) y sus zonas vecinas están en gris (#CDCDCD). Además, sobre las zonas centrales y vecinas se superponen las calles respectivas, estas calles se colorean según la siguiente regla según su atributo ```"highway"```

- Si ```highway=="motorway"``` se usa el color ```"red"```.
- Si ```highway=="secondary"``` se usa el color ```"yellow"```.
- Si ```highway=="tertiary"``` se usa el color ```"blue"```.
- Si ```highway=="primary"``` se usa el color ```"green"```.
- Si ```highway=="residential"``` se usa el color ```"black"```.

Las calles que no son pintadas son las siguientes (en Santiago, Chile):
- "footway"
- "service"
- "pedestrian"
- "living_street"
- "cycleway"
- "unclassified"
- "primary_link"
- "motorway_link"
- "steps"
- "secondary_link"
- "path"
- "tertiary_link"

_Obs: existen calles que contienen más de un tipo de calle, por ejemplo, "[footway, steps]"._

  <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%203/fig_larenas.png">
  <br><br>
  <b>Figura 5: Mapa de zonas para Larenas.</b><br>
  <br><br>
 </p>

   <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%203/p3e3_Dussaillant.png">
  <br><br>
  <b>Figura 6: Mapa de zonas para Dussaillant.</b><br>
  <br><br>
 </p>

   <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%203/fig_simon.png">
  <br><br>
  <b>Figura 7: Mapa de zonas para Simón.</b><br>
  <br><br>
 </p>
 
_Nota: Figuras 5-7 se encuentran en la carpeta "Figuras Entrega 3"._

_Obs: La zona 324 tenía problemas al momento de usar la función gps.clip(...) por lo que se decidió omitir esa zona._

## Entrega 4

Para realizar el problema se utilizó el código ```p3e4.py```, para crear dicho código, fue necesario incorporar las funciones de costo:
```
f1 = lambda f: 10.+f/120.
f2 = lambda f: 14.+f/80.
f3 = lambda f: 10.+f/240.
```
Donde f1 corresponde a los arcos r, v, z; f2 corresponde a los arcos s, u, w, y; f3 corresponde a los arcos t, x. Luego, se incorpora la matriz de costos, el grafo ```G = nx.DiGraph()```(se usa nx.DiGraph() ya que la dirección de cada arco influye, nx.Graph no toma en cuenta la dirección de los arcos), los nodos y los arcos. Más adelante, se procede a crear el algoritmo que resolverá el equilibrio de Wardrop, esto es:
```
incrementos = [0.1]*9 + [0.01]*9 + [0.001]*9 + [0.0001]*9 + [0.00001]*9 + [0.000001]*9 + [0.0000001]*9 + [0.00000001]*10
for incremento in incrementos:
        for key in OD:
            origen, destino = key[0], key[1]
            demanda_actual, demanda_objetivo = OD[key], OD_target[key]
            if demanda_actual > 0.:
                path = dijkstra_path(G,origen,destino,weight='costo')
                Nparadas = len(path)
                for i in range(Nparadas-1):
                    o, d = path[i], path[i+1]
                    G.edges[o,d]['flujo'] += incremento*demanda_objetivo
                    G.edges[o,d]['costo'] = G.edges[o,d]['fcosto'](G.edges[o,d]['flujo'])
                OD[key] -= incremento*demanda_objetivo
```
Analizando estas líneas de código, se puede notar que se utilizan distintos incrementos para obtener un resultado más preciso. Luego, se recorre el diccionario creado a partir de la matriz origen-destino para determinar la ruta óptima con "dijkstra_path" (para grafos de mayor tamaño, se hubiera utilizado "astar_path"). Obteniendo la ruta óptima, se procede a recorrer la ruta para modificar el "flujo" y "costo" de cada arco. Esto último se hace de la siguiente manera:

1. Se obtiene el origen y destino de cada arco, es decir, si la ruta es ['A', 'B', 'C'], la primera iteración sería origen='A', destino='B' y en la segunda iteración sería origen='B', destino='C'.
2. El flujo de cada arco aumenta en el incremento mencionado previamente (un incremento que varía c/r a cada iteración) multiplicado por la demanda objetivo (la demanda obtenida por enunciado).
3. El costo de cada arco será igual a las funciones f1, f2, f3 (mencionadas previamente) evaluadas en el flujo obtenido en (2). Importante mencionar que el flujo se aplica a la función f1, f2, f3 correspondiente a la ruta que se esta iterando.
4. A la demanda actual "OD[key]" se le resta el valor que se le agregó al flujo en (2). Dado que se le esta restando valores a la demanda actual, se puede ver que al llegar a 0, el alogritmo finalizará, pues, al tener la demanda actual en 0 implica que se llegó al equilibrio.

Finalmente, se procede a graficar los resultados obtenidos, dichos resultados se pueden ver a continuación en las Figuras 8 a 10:

 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%204/grafo.png">
  <br><br>
  <b>Figura 8: Grafo del problema.</b><br>
  <br><br>
 </p>

   <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%204/flujo.png">
  <br><br>
  <b>Figura 9: Flujo final establecido el equilibrio de Wardrop .</b><br>
  <br><br>
 </p>

   <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%204/costo.png">
  <br><br>
  <b>Figura 10: Costo de las rutas.</b><br>
  <br><br>
 </p>

A partir de los resultados obtenidos, se obtiene la siguiente tabla resumen:

   <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Figuras%20Entrega%204/Tabla%20Resumen.png">
  <br><br>
  <b>Figura 11: Tabla resumen.</b><br>
  <br><br>
 </p>

Observando la Figura 11, se puede ver rápidamente que las rutas 3, 9, 10, 11 y 13 no van a ser utilizadas, debido a que su costo es mucho mayor a las rutas alternativas, y el resto de las rutas para su par OD tienen costos básicamente iguales (difieren en solo algunos casos, y cuando difieren, son errores tan pequeños que no deben tomarse en cuenta, los errores van a tender a 0% a medida que se agreguen más decimales de precisión a los incrementos usados en el código). Finalmente, se puede mencionar que los resultados obtenidos utilizando el código ```p3e4.py``` son resultados prácticamente iguales (errores menores al 1%) a los resultados obtenidos en la solución del "Control 4 - Asignación" de Sistemas de Transporte. Por ende, el código usado para resolver el problema está correcto.

_Nota 1: Figuras 8-11 se encuentran en la carpeta "Figuras Entrega 4"._

_Nota 2: Los resultados obtenidos fueron redondeados a la cuarta décima para visualizar de mejor manera los valores en los gráficos"._

## Entrega 5

_Para realizar esta entrega se usaron todos los archivos encontrados en la carpeta Entrega 5._

**¿Cómo seleccionó las zonas a incluir?**

Las zonas fueron seleccionadas según los siguientes criterios (Estos criterios se encuentran en ```obtenerDatos.py``` en la carpeta Entrega 5):

1. Tiene origen y/o destino una zona donde se encuentra Américo Vespucio Oriente.
2. Tiene una demanda > 100.

Estas zonas se pueden observar a continuación, en la Figura 12:

   <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Entrega%205/fig_entrega_5.png">
  <br><br>
  <b>Figura 12: Zonas seleccionadas.</b><br>
  <br><br>
 </p>

**¿Cuántas zonas quedaron seleccionadas?**

Hay un total de **109** zonas que cumplen con los criterios 1 y 2. Estas son:

[287, 79, 143, 291, 581, 290, 497, 537, 500, 146, 288, 163, 220, 307, 201, 193, 232, 206, 200, 666, 306, 590, 271, 682, 274, 266, 516, 683, 277, 284, 425, 265, 297, 268, 304, 471, 292, 289, 677, 300, 1, 312, 295, 276, 668, 548, 153, 305, 684, 302, 667, 49, 675, 513, 299, 296, 293, 512, 511, 495, 498, 320, 448, 614, 508, 627, 325, 18, 313, 514, 309, 327, 496, 301, 673, 671, 672, 328, 332, 333, 331, 680, 370, 386, 388, 407, 578, 438, 440, 443, 430, 431, 642, 490, 502, 510, 696, 725, 695, 724, 543, 547, 577, 0, 580, 763, 2, 670, 599]

**¿Cuántos viajes deberá asignar?**



**¿Cuáles son los pares OD que espera Ud. que generen mayor flujo en AVO?**

En el código ```obtenerDatos.py```, se puso además, que las zonas con una demanda mayor a 1000 sean las zonas de mayor flujo. Hay un total de **24** zonas que generan mayor flujo en Américo Vespucio Oriente. Estas son:

[[304, 471], [471, 304], [307, 471], [471, 307], [288, 292], [292, 288], [289, 666], [666, 289], [289, 300], [300, 289], [682, 667], [667, 682], [307, 500], [500, 307], [307, 307], [683, 683], [683, 288], [288, 683], [677, 672], [672, 677], [153, 430], [430, 153], [682, 291], [291, 682]]

Estas zonas se pueden observar a continuación, en la Figura 13:

   <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P3-Grupo04/blob/main/Entrega%205/fig_entrega_5_mayor_flujo.png">
  <br><br>
  <b>Figura 13: Zonas de mayor flujo.</b><br>
  <br><br>
 </p>

_Nota: Las Figuras 12 y 13, los códigos usados y los archivos .gpickle, .json y .csv se encuentran en la carpeta "Entrega 5"._
