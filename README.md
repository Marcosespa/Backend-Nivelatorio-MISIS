# Backend-Nivelatorio-MISIS

## Descripción

Este proyecto tiene como objetivo desarrollar una aplicación web intuitiva y eficiente para gestionar listas de tareas. La aplicación permitirá a los usuarios crear, organizar y rastrear el progreso de sus actividades diarias.

---

## Componentes Principales

1. **API REST (Flask):**
   - Implementa la lógica de negocio.
   - Proporciona endpoints para gestionar usuarios, tareas y categorías.

2. **Base de Datos (SQL):**
   - Almacena información de usuarios, tareas y sus estados.

3. **Interfaz Web:**
   - Ofrece una experiencia interactiva para los usuarios.
   - Permite la creación, edición y visualización de tareas.

---

## Funcionalidades

### **Gestín de Usuarios:**
- Creación de cuentas.
- Inicio y cierre de sesión.
- Carga de imagen de perfil (con opción por defecto).

### **Gestín de Tareas:**
- Creación, edición y eliminación de tareas.
- Organización en categorías predefinidas.
- Asignación de estados: **Sin Empezar**, **En Progreso**, **Finalizada**.
- Registro de fechas de creación.

### **Interfaz Intuitiva:**
- Diseño amigable para una fácil interacción.
- Visualización clara de tareas y categorías.

---

## Instalación y Ejecución

### **Clonar el repositorio:**
```bash
git clone https://github.com/Marcosespa/Nivelatorio-MISIS.git
```

### **Crear un entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate
```

### **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

### **Iniciar la base de datos:**
```bash
flask db init
flask db migrate -m "Reiniciar migraciones"
flask db upgrade
```


### **Conectarse a la base de datos
```bash
psql -h localhost -U postgres -d bdnivelatorio1

```


### **Ejecutar la aplicación:**
```bash
flask run --host=0.0.0.0 --port=8080
Ver las Tablas en la Base de Datos Conectada:
\dt
```

---

## Estructura del Proyecto

- **`api/`**: Contiene los archivos de la API Flask.
- **`models/`**: Define los modelos de la base de datos (usuarios, tareas, categorías).
- **`static/`**: Almacena archivos estáticos como CSS y JavaScript.
- **`templates/`**: Contiene las plantillas HTML para la interfaz web.

---

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un **issue** para discutir nuevas características o mejoras antes de realizar cambios importantes. También puedes enviar un **pull request**.

---

## Licencia

Este proyecto está licenciado bajo la **MIT License**. Consulta el archivo `LICENSE` para más detalles.
