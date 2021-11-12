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
