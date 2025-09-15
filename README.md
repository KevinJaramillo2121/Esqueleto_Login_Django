Esqueleto de Autenticación con Django (esqueleto_login_Django)
![Django](https://img.shields.io/badge/Django-092E

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the

Este repositorio contiene un proyecto base de Django robusto y reutilizable que implementa un sistema de autenticación de usuarios completo. Está diseñado para ser el punto de partida para nuevos proyectos web, ahorrando tiempo en la configuración inicial de la gestión de usuarios.

✨ Características Principales
Este esqueleto de proyecto viene preconfigurado con las siguientes funcionalidades esenciales:

Registro de Usuarios (Sign Up): Permite a nuevos usuarios crear una cuenta de forma segura.

Inicio de Sesión (Login): Autenticación de usuarios existentes con manejo de sesiones.

Cierre de Sesión (Logout): Permite a los usuarios finalizar su sesión de manera segura.

Recuperación de Contraseña (Password Reset): Flujo completo para que los usuarios puedan restablecer su contraseña a través de un enlace enviado a su correo electrónico.

Cambio de Contraseña: Una vista para que los usuarios autenticados puedan cambiar su contraseña actual.

Base de Datos PostgreSQL: Configurado para usar PostgreSQL, una base de datos potente y lista para producción.

Gestión de Secretos: Implementa python-decouple para una gestión segura de claves y credenciales fuera del control de versiones.

🚀 Cómo Empezar
Sigue estos pasos para clonar y configurar el proyecto en tu máquina local.

1. Prerrequisitos
Asegúrate de tener instalados los siguientes programas en tu sistema:

Python 3.8+

Git

PostgreSQL

2. Clonar el Repositorio
Abre tu terminal y clona este repositorio en una nueva carpeta.

bash
git clone https://github.com/KevinJaramillo2121/Esqueleto_Login_Django.git nuevo-proyecto
cd nuevo-proyecto
3. Configurar el Entorno
Es una buena práctica trabajar dentro de un entorno virtual para aislar las dependencias del proyecto.

bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
4. Instalar Dependencias
Instala todos los paquetes de Python necesarios con un solo comando.

bash
pip install -r requirements.txt
5. Configurar la Base de Datos y Variables de Entorno
Este proyecto utiliza un archivo .env para gestionar las variables sensibles.

a. Prepara tu base de datos PostgreSQL:
Abre psql y crea una base de datos y un usuario para este nuevo proyecto.

sql
CREATE DATABASE nombre_de_tu_db;
CREATE USER usuario_de_tu_db WITH PASSWORD 'tu_clave_segura';
GRANT ALL PRIVILEGES ON DATABASE nombre_de_tu_db TO usuario_de_tu_db;
b. Crea el archivo .env:
En la raíz del proyecto, crea un archivo llamado .env y añade la siguiente configuración, reemplazando los valores con tus propias credenciales.

text
# Ejemplo de archivo .env

# ¡MUY IMPORTANTE! Genera una nueva clave secreta para cada proyecto.
# Puedes usar un generador online o la utilidad de Django.
SECRET_KEY="tu_nueva_clave_secreta_aqui"

# Configuración de la base de datos
DB_NAME="nombre_de_tu_db"
DB_USER="usuario_de_tu_db"
DB_PASSWORD="tu_clave_segura"
DB_HOST="localhost"
DB_PORT="5432"

# Para desarrollo, los correos se imprimen en consola.
# Para producción, deberás configurar un servicio como SendGrid o Gmail.
EMAIL_BACKEND="django.core.mail.backends.console.EmailBackend"
6. Ejecutar Migraciones y Crear Superusuario
Aplica el esquema de la base de datos y crea una cuenta de administrador.

bash
# Aplica las migraciones para crear las tablas en la base de datos
python manage.py migrate

# Crea un superusuario para acceder al panel de administración de Django
python manage.py createsuperuser
7. ¡Lanzar el Servidor!
¡Ya está todo listo! Inicia el servidor de desarrollo de Django.

bash
python manage.py runserver
Ahora puedes acceder a la aplicación en http://127.0.0.1:8000/.

⚙️ Estructura del Proyecto
text
esqueleto_login_Django/
├── core/                   # Carpeta principal del proyecto Django
│   ├── settings.py         # Configuración del proyecto
│   └── urls.py             # URLs principales del proyecto
├── accounts/               # App dedicada a la gestión de usuarios
│   ├── forms.py            # Formularios personalizados (ej. registro)
│   ├── urls.py             # URLs específicas de la app 'accounts'
│   └── views.py            # Vistas (ej. vista de registro)
├── templates/              # Plantillas HTML globales
│   ├── base.html
│   ├── home.html
│   └── registration/       # Plantillas para el sistema de autenticación
├── .gitignore              # Archivos y carpetas a ignorar por Git
├── manage.py               # Utilidad de línea de comandos de Django
├── requirements.txt        # Lista de dependencias de Python
└── README.md               # Este archivo :)
下一步 (Próximos Pasos)
Con la autenticación ya resuelta, puedes enfocarte en construir las funcionalidades principales de tu aplicación. Utiliza el decorador @login_required o el LoginRequiredMixin para proteger tus vistas y restringir el acceso solo a usuarios autenticados.