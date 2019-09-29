Dado un archivo que contiene en cada línea una palabra o conjunto de palabras seguido de un valor numérico, denominado “sentimiento”, y un conjunto de tweets, se pide calcular para cada tweet un valor denominado “sentimiento del tweet”, que se obtiene como la suma de los “sentimientos” de los términos que aparecen en el tweet.

Aquellas palabras o conjunto de palabras que aparecen en un tweet, y no tengan un “sentimiento” asociado en el archivo, se contabilizarán como 0.

Para procesar el archivo hay que tener en cuenta que cada palabra o conjunto de palabras están separadas de su valor mediante el carácter “\t”. El archivo podría almacenarse en un diccionario usando el siguiente trozo de código (figura 9.2.).


---- DADOS DE ENTRADA ----

El programa tendrá 2 parámetros de entrada: 
	- el archivo que contiene los sentimientos de los términos y 
	- el archivo que contiene los tweets. 
Estos parámetros se pueden leer como:
	- input desde el teclado, directamente en el código 
	- o como parámetros con sys.args.


---- RESULTADO A MOSTRAR -----

Como resultado, se debe mostrar por pantalla un valor numérico en cada línea que represente el “sentimiento” de un tweet.

No todos los tweets que se van a considerar tienen contenido, por lo que hay que filtrar aquellos que tienen de los que no tienen.

-- EXEMPLO --

Si se toma como referencia el siguiente tweet:
	- I will go on vacation to the beach.
Supongamos que las siguientes palabras aparecen en el archivo de sentimientos:
	- vacation: 2
	- beach: 1
Ya que el resto de palabras no se encuentran en el archivo de sentimientos, tendríamos un sentimiento del tweet de (2+1) = 3 y, por lo tanto, tendríamos la siguiente salida del programa:

EL SIGUIENTE TWEET: 'I will go on vacation to the beach' TIENE UN SENTIMIENTO ASOCIADO DE: 3

