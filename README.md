# Gestión de Tareas - Aplicación Web

Este proyecto es una aplicación web para la gestión de listas de tareas, desarrollada como parte de un ejercicio de nivelación para el curso **Desarrollo de Soluciones Cloud**. La aplicación permite a los usuarios crear, organizar y monitorear el progreso de sus tareas diarias.

---

## Características Principales

### **Autenticación de Usuarios**
- Registro de nuevos usuarios.
- Inicio de sesión con JWT (JSON Web Tokens).

### **Gestión de Tareas**
- Crear, actualizar, eliminar y obtener tareas.
- Organizar tareas en categorías.
- Asignar estados a las tareas (Sin Empezar, En Progreso, Finalizada).

### **Gestión de Categorías**
- Crear, eliminar y obtener categorías.

### **Base de Datos**
- Almacenamiento estructurado de usuarios, tareas y categorías.

### **Despliegue**
- La aplicación está empaquetada en un contenedor Docker.
- Se puede ejecutar en una máquina virtual con Ubuntu.

---

## Tecnologías Utilizadas

### **Backend**
- Python 3.12
- Flask (Framework web)
- Flask-JWT-Extended (Autenticación con JWT)
- SQLAlchemy (ORM para la base de datos)
- SQLite (Base de datos)

### **Frontend**
- Tecnología libre (puede ser HTML/CSS/JavaScript o un framework como Vue.js o Angular).

### **Despliegue**
- Docker
- AWS Academy (Máquina virtual con Ubuntu)

---

## Estructura del Proyecto

/proyecto /app init.py models.py routes.py auth.py config.py run.py requirements.txt Dockerfile README.md

---

## Configuración del Proyecto

### **Requisitos Previos**
- Python 3.12 o superior.
- Docker (opcional, para empaquetar la aplicación).
- Postman (para probar los endpoints).

### **Instalación**

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
2. **rea un entorno virtual::**
   ```bash
   python -m venv venv
   
Activa el entorno virtual:
En Windows:
venv\Scripts\activate
En Linux/Mac:
source venv/bin/activate
Instala las dependencias:
pip install -r requirements.txt
Configura la base de datos: Ejecuta el siguiente comando para crear las tablas:
python
Dentro del intérprete de Python, ejecuta:
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
Ejecuta la aplicación:
python run.py
La aplicación estará disponible en http://localhost:8080.
Ejecución con Docker

Construye la imagen Docker:
docker build -t mi-aplicacion .
Ejecuta el contenedor:
docker run -p 8080:8080 mi-aplicacion
La aplicación estará disponible en http://localhost:8080.
Endpoints de la API

Autenticación
Registro de Usuario:
Método: POST
URL: /registro
Body:
{
  "nombre_usuario": "usuario1",
  "contrasena": "password123",
  "imagen_perfil": "https://ejemplo.com/foto.jpg"
}
Inicio de Sesión:
Método: POST
URL: /login
Body:
{
  "nombre_usuario": "usuario1",
  "contrasena": "password123"
}
Tareas
Obtener Tareas de un Usuario:
Método: GET
URL: /usuarios/{id}/tareas
Crear Tarea:
Método: POST
URL: /tareas
Body:
{
  "texto_tarea": "Hacer la compra",
  "fecha_creacion": "2023-10-01",
  "id_usuario": 1,
  "id_categoria": 1
}
Actualizar Tarea:
Método: PUT
URL: /tareas/{id}
Body:
{
  "texto_tarea": "Hacer la compra y pagar las cuentas",
  "estado": "En progreso"
}
Eliminar Tarea:
Método: DELETE
URL: /tareas/{id}
Categorías
Crear Categoría:
Método: POST
URL: /categorias
Body:
{
  "nombre": "Trabajo",
  "descripcion": "Tareas relacionadas con el trabajo"
}
Obtener Todas las Categorías:
Método: GET
URL: /categorias
Eliminar Categoría:
Método: DELETE
URL: /categorias/{id}
Pruebas con Postman

Importa la colección de Postman que se encuentra en la carpeta postman del proyecto.
Ejecuta los endpoints en el siguiente orden:
Registro de usuario.
Inicio de sesión.
Crear tarea.
Obtener tareas.
Actualizar tarea.
Eliminar tarea.
Crear categoría.
Obtener categorías.
Eliminar categoría.
Despliegue en AWS Academy

Accede al laboratorio de AWS Academy.
Aprovisiona una máquina virtual con Ubuntu.
Copia los archivos del proyecto a la máquina virtual usando scp:
scp -r /ruta/del/proyecto usuario@ip_maquina:/ruta/destino
Conéctate a la máquina virtual por SSH:
ssh usuario@ip_maquina
Ejecuta la aplicación en la máquina virtual:
docker build -t mi-aplicacion .
docker run -p 8080:8080 mi-aplicacion
Accede a la aplicación desde tu navegador usando la IP de la máquina virtual:
http://ip_maquina:8080