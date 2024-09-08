# Proyecto Django: Blog Web Application

## Descripción del Proyecto

Este es un proyecto web estilo blog desarrollado en Django. La aplicación permite a los usuarios registrarse, iniciar sesión, crear, editar y eliminar blogs. Cada blog incluye un título, subtítulo, cuerpo, autor, fecha y una imagen. Además, la aplicación cuenta con una página "Acerca de mí" y una vista de detalle para cada blog.

### Funcionalidades principales:
- Registro de usuarios.
- Inicio y cierre de sesión.
- Creación, actualización y eliminación de blogs (CRUD completo).
- Vista de listado de blogs con enlaces a los detalles.
- Página "Acerca de mí" en la ruta `/about/`.
- Sistema de mensajería entre usuarios en la ruta `/messages/`.
- Solo los administradores pueden editar o eliminar blogs.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado lo siguiente:

- Python 3.x
- Django 4.x
- Base de datos SQLite (incluida por defecto en Django)

## Instalación y Configuración

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/blog-django.git
   cd blog-django
