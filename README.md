# Control de Equipos de Cómputo

Aplicación web **Django 6.1** que implementa un **CRUD** (Create, Read, Update, Delete) para administrar equipos de cómputo, usando **MariaDB** como base de datos y **Bootstrap** en el frontend. Las vistas, plantillas y URL de la aplicación se definen en la app `core`.

Esta guía está enfocada **100% en Windows** (el compañero de equipo que trabaja en el CRUD usa este SO).

> **Nota sobre `ó` en el nombre del proyecto:** el directorio se llama `Control_equipos_cómputo` (con `ó`). Es 100% funcional en Windows; solo ten cuidado al teclear el nombre. Si copias/pegas los comandos de esta guía funcionan igual. Para evitar cualquier problema de acento, evita usar la consola con algunos caracteres raros y escribe el nombre con `AltGr`+`o`, o copia el texto directamente.

---

## 1. Requisitos previos (instalar una sola vez)

### 1.1 Python 3.12+
1. Descarga el instalador desde: https://www.python.org/downloads/
2. **MUY IMPORTANTE:** en la primera pantalla del instalador, marca la casilla **"Add Python to PATH"** (Agregar Python al PATH) y luego *Install Now*.
3. Verifica en una terminal nueva (Símbolo del sistema `cmd` o PowerShell):
   ```cmd
   python --version
   pip --version
   ```
   Debe mostrar algo como `Python 3.12.x`. Si tira error `'python' is not recognized`, cierra y abre **una nueva** terminal (el PATH se recarga solo en ventanas nuevas).

### 1.2 MariaDB (base de datos)
Windows normalmente viene con **MySQL** no con MariaDB, pero el proyecto usa ambas de forma idéntica. Dos opciones:

- **Opción A (recomendada):** instalar **XAMPP** (incluye MariaDB). Descarga desde https://www.apachefriends.org/ e instala. Luego:
  - Abre el **XAMPP Control Panel**.
  - Pulsa **Start** en la fila de **MySQL**. La fila se pone en verde.
  - El servidor queda en `localhost:3306`. Para entrar a la consola de comandos de la BD usa el botón **Shell** del panel y luego `mysql -u root` (sin contraseña por defecto).

- **Opción B:** instalar **MySQL Community Server** directo desde https://dev.mysql.com/downloads/ (deja el puerto 3306).

### 1.3 (Opcional pero recomendado) Editor
Visual Studio Code + la extensión "Python". Abre la carpeta del proyecto ahí.

---

## 2. Estructura del proyecto

```
Control_equipos_cómputo/
├── manage.py                      # CLI de administración de Django
├── requirements.txt               # Dependencias de Python (pip)
├── .env.example                   # Plantilla de configuración (copiar a .env)
├── .env                           # Configuración real (NO versionar)
├── .gitignore                     # Archivos ignorados por git
├── Control_equipos_cómputo/       # Configuración del proyecto Django
│   ├── settings.py                # Configuración: apps, BD, env vars
│   ├── urls.py                    # Rutas raíz (solo /admin/ por ahora)
│   ├── asgi.py
│   └── wsgi.py
└── core/                          # App Django del CRUD
    ├── models.py                  # Modelo(s) (vacío, por definir)
    ├── views.py                   # Vistas (vacío, por implementar)
    ├── admin.py                   # Registro de modelos
    ├── apps.py                    # ConfigCore
    └── migrations/
```

Tech stack: **Python 3.12+ · Django 6.1 · MariaDB/MySQL · mysqlclient · python-dotenv · Bootstrap**.

---

## 3. Configurar la base de datos (MariaDB)

Con XAMPP corriendo (MySQL en verde), abre el **Shell** de XAMPP y escribe:

```sql
CREATE DATABASE control_equipos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

`settings.py` conecta con `charset: utf8mb4`, así que la base debe crearse con ese mismo juego de caracteres para evitar errores con acentos/`ó`.

---

## 4. Instalación paso a paso (Windows) — HAZLO EN ORDEN

Abre una terminal (cmd o PowerShell) y ve a la carpeta raíz del proyecto, donde está `manage.py`:

```cmd
cd "C:\ruta\a\tu\proyecto\Control_equipos_cómputo"
```

### Paso 1 — Crear el entorno virtual (venv)
El **venv** aísla las dependencias de Python para este proyecto y evita que se mezclen con otros proyectos del sistema.

```cmd
python -m venv .venv
```
Esto crea la carpeta `.venv\` dentro del proyecto. **Actívalo** (cada vez que abras una terminal NUEVA debes activarlo de nuevo):

```cmd
.venv\Scripts\activate
```
Verás que la línea de la terminal ahora empieza con `(.venv)`, señal de que el entorno está activo. Para desactivarlo más tarde: `deactivate`.

> Para **PowerShell**, si tira error `running scripts is disabled`, ejecuta una vez:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### Paso 2 — Instalar las dependencias
```cmd
pip install -r requirements.txt
```
Instala: `asgiref`, `Django==6.1`, `sqlparse`, `mysqlclient==2.2.8`, `python-dotenv`.

> **Si falla `mysqlclient`:** depende de binarios de MySQL/MariaDB. La forma más fácil en Windows es instalar el wheel ya compilado. Dentro del entorno virtual (ve a https://pypi.org/project/mysqlclient/), o directamente:
> ```cmd
> pip install mysqlclient==2.2.8
> ```
> Si da error de compilación, instala antes Microsoft C++ Build Tools (https://visualstudio.microsoft.com/visual-cpp-build-tools/) o prueba con `pipwin`/un wheel precompilado.

### Paso 3 — Crear el archivo `.env`
```cmd
copy .env.example .env
```
Luego ábrelo con el Bloc de notas y pon tus credenciales reales:
```ini
DB_ENGINE=django.db.backends.mysql
DB_NAME=control_equipos
DB_USER=root
DB_PASSWORD=        ; XAMPP por defecto root sin contraseña → déjalo vacío
DB_HOST=localhost
DB_PORT=3306

SECRET_KEY=una_clave_secreta_larga_y_aleatoria
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```
En XAMPP el usuario `root` normalmente **no tiene contraseña**, así que deja `DB_PASSWORD=` vacío. Si usas MySQL con contraseña, ponla ahí.

### Paso 4 — Migraciones
```cmd
python manage.py makemigrations
python manage.py migrate
```

### Paso 5 — Superusuario del admin (opcional pero recomendado)
```cmd
python manage.py createsuperuser
```

### Paso 6 — Arrancar el servidor
```cmd
python manage.py runserver
```
Luego abre en tu navegador:
- **Panel admin:** http://127.0.0.1:8000/admin/
- **Raíz del sitio:** http://127.0.0.1:8000/

Para detenerlo: `Ctrl + C` en la terminal.

---

## 5. Estado actual del proyecto (quién continúa el desarrollo)

El CRUD **aún NO está implementado**; esto es lo que hay y lo que falta:

| Componente | Estado actual | Lo que falta |
|-----------|---------------|--------------|
| `core/models.py` | Vacío | Definir modelo `Equipo` con **≥5 campos + id** (ej: `numero_inventario`, `tipo`, `marca`, `modelo`, `estado`, `responsable`, `fecha_adquisicion`) |
| `core/views.py` | Vacío | Vistas CRUD: create, read/list, update, delete (con confirmación) |
| `Control_equipos_cómputo/urls.py` | Solo `/admin/` | Incluir las URL de `core` con `include()` |
| `core/templates` | No existe | Plantillas HTML base + listado + formularios, con Bootstrap |
| `core/admin.py` | Vacío | Registrar los modelos |
| `core/migrations/` | Solo `__init__.py` | Generarlas tras definir el modelo |

**Secuencia para completar el CRUD:** definir modelo → `makemigrations` → `migrate` → crear vistas → crear URL → crear plantillas → registrar en `admin.py`.

---

## 6. Verificación / sanity check (después de cada instalación)

```cmd
python manage.py check
python manage.py migrate
python manage.py runserver
```

---

## 7. Solución de problemas comunes (Windows)

| Problema | Causa probable | Solución |
|----------|----------------|----------|
| `'python' is not recognized` | No marcaste "Add Python to PATH" | Reinstala Python marcando esa casilla y abre terminal nueva |
| `No module named 'MySQLdb'` | `mysqlclient` no instalado | `pip install mysqlclient==2.2.8` dentro del venv activo |
| `Access denied for user 'root'` | Contraseña en `.env` incorrecta | XAMPP root no tiene clave → dejar `DB_PASSWORD=` vacío |
| `Unknown database 'control_equipos'` | Base no creada | Crearla (ver sección 3) |
| `Can't connect ... (2003)` | MariaDB/MySQL no está corriendo | Abrir XAMPP y darle **Start** a MySQL |
| `Invalid HTTP_HOST header` | `ALLOWED_HOSTS` sin tu host | Añadirlo en `.env` (o dejar `DEBUG=True`) |
| PowerShell niega scripts | Execution Policy | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Error de compilación en `pip install mysqlclient` | Faltan herramientas C++ / wheel | Usar un wheel precompilado o instalar VS C++ Build Tools |

---

## 8. Recordatorio rápido (resumen de comandos)

```cmd
cd "C:\ruta\proyecto\Control_equipos_cómputo"
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env        ; editar .env con credenciales
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
    