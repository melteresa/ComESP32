# ComESP32

## En nuestro proyecto del ESP32 con WebSockets, ¿quién actúa como Host (Servidor) y quién como Cliente? Define brevemente qué responsabilidad tiene cada uno en la comunicación.

La respuesta es 
Host: Computadora del profesor
Cliente: Computadoras de los estudiantes 
El Host, se encarga de crear y mantener la conexión, enviar datos y recibir comandos. El Cliente inicia la conexión, envía solicitudes, recibe la información y la muestra en la interfaz.

## Explica con tus palabras qué representaría la Dirección IP y qué representaría el Puerto. ¿Por qué es necesario especificar ambos para que el programa funcione?

La respuesta es: la Dirección IP sirve para saber a donde apunto para consumir el servicio y el Puerto especifica el servicio que se quiere consumir. 
Es necesario especificar ambos porque la IP indica a qué equipo conectarse y el puerto indica a qué programa dentro de ese equipo debe enviarse la comunicación.