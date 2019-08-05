Criar um script que mostra o seguinte menu:  
````
Ver directorio actual...........[1]   # se mostrarán los archivos del directorio actual.  
Copiar archivos.................[2]   # se le pedirá el nombre del archivo que se quiere copiar y el nombre del archivo donde se quiere copiar.  
Editar archivos.................[3]   # se le pedirá el nombre del archivo que se desea editar y se abrirá el editor vi para editarlo. 
Imprimir archivo................[4]   # se le pedirá el nombre del archivo que se desea imprimir y se imprimirá el mismo.  
Salir del menú..................[5]   # se saldrá del script.  
````
**Solución**
````bash
while true
do
clear

echo "
Ver directorio actual...........[1]

Copiar ficheros.................[2]

Editar ficheros.................[3]

Imprimir fichero................[4]

Salir del menú..................[5]"

read i

case $i in
1) ls -l|more; 
  read z
;;

2) echo "Introduzca [desde] [hasta]"
  read x y
  cp $x $y
  read x
;;

3) echo "¿Nombre de fichero a editar?"
  read x;
  vi $x
;;

4) echo "¿Nombre de fichero a imprimir?"
  read x
  lpr $x
;;

5) clear; break
;;

esac

done
````
