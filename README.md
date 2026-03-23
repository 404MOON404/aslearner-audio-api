ASLearner - Audio API 


Descripción

Dentro de nuetra aplicación de lenguaje ASL decidimos agregar estra API RESTful con el objetivo de reforzar el aprendizaje y proporsionar accesibilidad mediante la conversión de texto a voz.
Básicamente hace uso de Edge TTS la cual es una síntesis de voz neuronal que nos permite generar en tiempo real audio claro de alta calidad.
Lo implementamos cono un microservicio independiente, principalmente con el rendimiento de la aplicación en mente ya que así se reduce la carga de procesamiento en el dispositivo móvil del usuario.

Evidencia de despliegue

Enlace a la API desplegada en Render:
https://aslearner-audio-api.onrender.com/docs


Documentación de Endpoints

Verificación del estado del servidor para saber si está levantado y recibiendo peticiones.

Método: GET
Endpoint: /
Respuesta exitosa:
{“mensaje”: “API de audio con Edge TTS activa en Render”}

Text to speech, recibe una cadena JSON y devuelve un .mp3 usando el motor neuronal.

Método: POST
Ruta: /generar-audio
Request body:
{“texto”: “Hola, excelente trabajo con la seña.”}
Respuesta exitosa:
Devuelve el archivo descargable y reproducible con el nombre leccion_asl.mp3 (media_type=“audio/mpeg”)
Respuesta error:
{“detail”= “Error interno (descripción del error)”