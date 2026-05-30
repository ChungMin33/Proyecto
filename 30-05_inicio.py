"""
BlackJack
El juego comienza con 5 barajas de cartas sin jokers.
Para empezar la partida los jugadores tienen que hacer una apuesta inicial,
posterior a la primera apuesta el dealer repartirá una carta a cada jugardor y tambien a si mismo,
con cada una de ellas dada vuelta para poder verlas, luego repartirá otra ronda de cartas,
esta vez dejando la segunda carta que se reparte para el oculta a la vista de todos.
Cada jugador juega contra la casa, con la peta principal llegar lo mas cercano posible a 21,
para ello los jugadores pueden seguir pidiendo cartas hasta que decidan no querer seguir pidiendo mas cartas.
En caso de que algún jugador exeda los 21, este perderá automaticamente.
luego de que todos los jugadores se hayan asentado con sus cartas, el dealer,
dará vuelta la carta que tenía oculta, en caso de que la suma de las cartas del dealer sea < 17,
el forzosamente tendrá que seguir pidiendo cartas hasta vencer al o a los jugadores que mas se hayan acercado al 21.
en caso de que el dealer exeda los 21, todos los jugadores que estén jugando todavía ganarán.




necesidades pra programar: 
- almacen de cartas
- contador de cartas disponibles
- sistema repartidor de cartas
- conteo de apuesta
"""
#cartas 
diamonts = ["DA","D2","D3","D4","D5","D6","D7","D8","D9","DT","DJ","DQ","DK"]
cloves = ["CA","C2","C3","C4","C5","C6","C7","C8","C9","CT","CJ","CQ","CK"]
hearts = ["HA","H2","H3","H4","H5","H6","H7","H8","H9","HT","HJ","HQ","HK"]
spades = ["SA","S2","S3","S4","S5","S6","S7","S8","S9","ST","SJ","SQ","SK"]
masos_total = [diamonts,cloves,hearts,spades]




