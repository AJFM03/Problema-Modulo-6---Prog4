# Problema-Modulo-6---Prog4

🎯 Objetivo
Modificar la aplicación de biblioteca personal para convertirla de una aplicación de línea de comandos a una aplicación web utilizando el framework Flask, manteniendo la lógica funcional original y el uso de KeyDB como almacenamiento en memoria.

📝 Contexto
En esta etapa, los estudiantes llevarán su proyecto al siguiente nivel desarrollando una interfaz web que permita gestionar la biblioteca personal a través de formularios y páginas web. La aplicación debe estar construida con Flask y continuar usando KeyDB como sistema de almacenamiento rápido en memoria.

📌 Requisitos funcionales
La aplicación web debe conservar todas las funcionalidades previamente implementadas:

Agregar nuevo libro
➤ Formulario web para ingresar título, autor, género y estado de lectura.

Actualizar información de un libro
➤ Formulario de edición con los campos del libro cargados previamente.

Eliminar libro existente
➤ Opción visible en la interfaz para eliminar un libro fácilmente.

Ver listado de libros
➤ Página que muestre todos los libros registrados con formato claro y organizado.

Buscar libros
➤ Barra o formulario para filtrar libros por título, autor o género.

🔄 Cambios y objetivos clave
Reestructurar la arquitectura para utilizar Flask como backend.

Definir rutas (@app.route) para cada funcionalidad clave.

Separar vistas (HTML), lógica (Python) y configuración del proyecto.

Continuar utilizando KeyDB con redis-py como backend para los datos.

Utilizar plantillas HTML y CSS. Se puede incluir Bootstrap para mejorar la presentación.

Implementar mensajes visuales (alertas) para operaciones exitosas o con error.

💡 Consideraciones técnicas
Archivo principal: app.py, donde se definen las rutas y se configura la app.

Estructura recomendada:

/templates      → Archivos HTML (Jinja2)
/static         → Archivos CSS/JS
/               → app.py, config.py, .env, requirements.txt
Utilizar dotenv para manejar credenciales en el archivo .env.

Las claves de KeyDB deben ser únicas (libro:<id> o UUIDs).

Validar entradas de formularios (campos vacíos, duplicados, etc.).

Crear un archivo requirements.txt con dependencias como flask, redis, python-dotenv.
