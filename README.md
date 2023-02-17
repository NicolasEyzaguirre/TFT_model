# TFT_model
El proyecto fue basado en el juego Team Figth Tactics creado por riot en 2019, con el fin de predecir las posibles composiciones ganadoras en cada partida, todo esto situado en el SET 7  "DRACONIC LANDS". Tanto el analisis como el modelado se hacen sobre archivos 2022-07-01 sacados de kaggle los cuales lo sacaron de la API de riot games.

Para comprender el modelado en necesario comprender el juego en si por este motivo se explicaran las reglas de una manera corta y concisa

## Reglas:

-Para ganar el juego debes ser el ultimo que sobrevive en la mesa, todos (8 jugadores) parten con 100 puntos de vida y esta va bajando conforme vas perdiendo, el daño vendra en funcion a cuantas fichas el ganador tiene con vida.

-Las fichas que esten en el tablero no las controlaras, solo las posicionaras y ellas actuaran por su cuenta.

-Cada ficha cuenta con un atributo, el cual si juntas una cierta cantidad del mismo tipo se activara un potenciador (dependiendo del atributo este variara) estas sinergias son acumulables.

-Las fichas se compran con el oro que vas ganando por cada ronda, la cantidad variara segun la racha de victoria y derrotas que tengas, y hay que tener en cuenta que cada tres fichas del mismo tipo la ficha asciende.


## Modelado
Al ser un juego y contener variables discretas se exploraron modelos que pudieran manejar datos categoricos siendo los posibles modelos a escoger:
-KNN
-SVM
-LogisticRegresion
-desicion trees 

Los dos primeros modelos quedaron descartados debido a la naturaleza de los datos, ya que estos contienen una grancantidad de variables (136) lo cual ocasiona que haya una disminucion en su presicion de igual manera la cantidad de filas a modelar era de una cantidad similar (49 144) por estos motivos tanto KNN como SVM quedaron descartados. tambien se descarto el desicion tree debido a la cantidad de capas que este tenia siendo 20 para alcanzar un 73% lo cual es 10% menos que la presicion que ubtuvimos con el ultimo que alcanzo un 83%.

El modelado ya se probo con mas data y sigue dando la misma presicion, por lo cual se puede afirmar que ya es usable en un contexto real.

Esas son las coclusiones del proyecto espero que haya sido de su agrado y cualquier feedback es más que bienvenido.