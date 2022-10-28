# PILB: Proxy Inverso + Balanceador de Carga

Integrantes: 
- Yhilmar Andres Chaverra Castaño
- Stiven Yepes Vanegas


## Introducción
Un proxy inverso se entiende como aquel que recibe (intercepta) cada una de las peticiones del cliente y la envía a un servidor con la capacidad de procesar la petición para finalmente enviar la respuesta al cliente. Por otro lado, un balanceador de carga, es la entidad encargada de distribuir las peticiones entrantes por parte de los clientes hacia un conjunto de servidores. Para cada petición, debe posteriormente, retornar la respuesta al cliente.
En este proyecto implementamos un proxy inverso y su balanceador de carga con las características anteriormente mencionadas. Además, implementamos algunas características extra como un proceso log y manejo de caché.

## Desarrollo 
Toda esta implementación fue desplegada en la nube de Amazon Web Services, empleando instancias EC2 para la instalación y configuración de los servidores y el proxy.

### Proxy
En nuestro proyecto encontrara un directorio de proxy donde encontrara el archivo proxy.py, este archivo es el que actuara como nuestro intermediario y conectara al cliente con los 3 servidores en nuestra simulación, este archivo se desplegara en una instancia EC2 para su simulación, este proxy recibe las peticiones HTTP enviadas por el host, las revisa y guarda un registro de la petición en el archivo register.log, luego toma la petición y la envia a cada servidor usando el algoritmo Round Robín, esto para siempre buscar el servidor menos congestionado. después espera la respuesta del servidor para reenviarla al host, la registra y hace su respectivo envio.

### Servidores
En nuestro proyecto implementamos un servidor HTTP, este tiene un archivo llamado server.py el cual recibe peticiones que llegan desde el host redirigidas por el proxy, en este caso accediendo al / del proyecto nos entrega un archivo index.html, además, este servidor también tiene la capacidad de guardar las respuestas que entrega a través de un archivo en el directorio /cache, esto con el fin evitar hacer consultas redundantes. Este caché implementado con una restricción TTL, la cual establece un tiempo de duración de la memoria en disco, y permite evitar almacenamiento en caché innecesario este código está desplegado en 3 instancias de EC2 en la nube de AWS.

![Image text](https://github.com/esyepesv/PILB/blob/main/Image/Diagramas%20Telematica.png)

## Instrucciones de ejecución
### Librerías Utilizadas En Nuestro Proyecto:

os (manejo de archivos)

time (tiempo real para la caché)

Sockets (comunicación entre dispositivos)

logging (manejo del archivo .log para registros detallados)

### Comandos Utilizados
Python 3.10.8

Ejecutar los servidores: python3 server1.py

ejecutar el proxy: python3 proxy.py

peticiones realizadas a través del navegador: http://(Direccion IP pública del proxy):PUERTO

## Conclusiones
En el desarrollo de esta práctica pudimos poner en práctica muchísimos conceptos en cuando a la implementación de un proxy inverso, al manejo de sockets y al envio de peticiones HTTP a través de redes simuladas, pudimos concluir que la utilidad de un proxy para efectos de manejo de peticiones, filtrado, balanceo, y administración de una red es fundamental, además pudimos establece en una infraestructura de trabajo robusta y bastante aplicable a la vida laboral como lo es la plataforma de AWS y las instancias EC2


## Referencias 
Codigo de laboratorio del profesor Juan Carlos Montoya: (MultiHilos) https://github.com/ST0255/st0255-20222/tree/main/LabSocketsMultiThread

Implementacion de un servidor HTTP con sockets (Alejandro Alvarez) : https://www.youtube.com/watch?v=TTE-ZxN3XkA
