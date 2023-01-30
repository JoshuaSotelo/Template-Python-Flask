Este repositorio proporciona una plantilla completa para proyectos de Python Flask, plantilla funcional para Heroku, incluyendo las siguientes carpetas y archivos:

Carpeta "views": contiene los controladores de la aplicación, que manejan las solicitudes HTTP y las respuestas.
Carpeta "static": almacena los archivos estáticos, como imágenes, CSS y JavaScript.
Carpeta "templates": contiene las plantillas HTML que se usan para renderizar la página.
Archivo "Procfile": específica los comandos que se deben ejecutar en un servidor web para desplegar la aplicación.
Archivo "app.py": contiene el código principal de la aplicación, incluyendo la creación de la aplicación Flask y la definición de las rutas.
Archivo "models.py": define los modelos de datos de la aplicación, que se usan para interactuar con la base de datos.
Archivo "extensions.py": contiene las extensiones que se usan en la aplicación, como Flask-SQLAlchemy para conectarse a la base de datos.
Archivo "requirements.txt": especifica las dependencias necesarias para ejecutar la aplicación.
Con esta plantilla, los desarrolladores pueden comenzar a construir rápidamente su proyecto de Flask con una estructura organizada y los componentes necesarios para conectarse a la base de datos y renderizar la página.

 Consideraciones
  1-Se necesita rellenar los datos de la db en app.py así como tambien instalar las librerias de requirements.txt para que flask corra 
  2-Se necesita realizar un Entorno Virtual en el root del proyecto para así correr flask con los siguientes comandos
    source nombreDelEntorno/bin/activate
    flask run
   3-El archivo Procfile es para Heroku
