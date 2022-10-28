# PILB: Proxy Inverso + Balanceador de Carga

Integrantes: 
- Yhilmar Andres Chaverra Castaño
- Stiven Yepes Vanegas


## Introdicción
Un proxy inverso se entiende como aquel que recibe (intercepta) cada una de las peticiones del cliente y la envía a un servidor con la capacidad de procesar la petición para finalmente enviar la respuesta al cliente. Por otro lado, un balanceador de carga, es la entidad encargada de distribuir las peticiones entrantes por parte de los clientes hacia un conjunto de servidores. Para cada petición, debe posteriormente, debe retornar la respuesta al cliente.
En este proyecto implementamos un proxy inverso y su balanceador de carga con las caracteristicas anteriormente mencionadas. Ademas, implementamos algunas características extra como un proceso log y manejo de caché.

## Desarrollo 
Toda esta implementación fue desplegada en la nube de Amazon Web Services, empleando instancias EC2 para la instalación y configuración de los servidores y el proxy.

### Proxy
En nuestro proyecto encontrara un directorio de proxy donde encontrara el archivo proxy.py, este archivo es el que actuara como nuestro intermediario y conectara al cliente con los 3 servidores en nuestra simulacion, este archivo se desplegara en una instancia EC2 para su simulacion, este proxy recibe las peticiones http enviadas por el host, las reviza y guarda un registro de la peticion en el archivo register.log, luego toma la peticion y la envia a cada servidor usando el algoridmo Round Robin, esto para siempre buscar el servidor menos congestionado. despues espera la respuesta del servidor para reenviarla al host, la registra y hace su respectivo envio.

### Servidores
En nuestro proyecto implementamos un servidor http, este tiene un archivo llamado server.py el cual recibe peticiones que llegan desde el host redirigidas por el proxy, en este caso accediendo al / del proyecto nos entrega un archivo index.html, ademas, este servidor tambien tiene la capacidad de guardar las respuestas que entrega a travez de un archivo en el directorio /cache, esto con el fin evitar hacer consultas redundantes. este cache implementado con una restriccion TTL, la cual establece un tiempo de duracion de la memoria en disco, y permite evitar almanecamiento en cache innecesario este codigo esta desplegado en 3 instancias de EC2 en la nuve de AWS.

![Image text](https://github.com/esyepesv/PILB/blob/main/Image/Diagramas%20Telematica.png)

## conclusiones


## Referencias 
