#  SOLUCIÓN AL ERROR "table usuarios has no column named cedula"

##  El Problema

```
sqlite3.OperationalError: table usuarios has no column named cedula
```

**Causa:** Tu base de datos fue creada con la versión anterior y no tiene las nuevas columnas.

---

##  SOLUCIÓN RÁPIDA (Recomendada)

### Opción 1: Script Automático

```bash
python fix_db.py
```

Este script:
1. Te pregunta si quieres eliminar la BD actual
2. La elimina de forma segura
3. Te dice qué hacer después

**Después ejecuta:**
```bash
python app.py
```

---

### Opción 2: Manual

```bash
# Windows:
del database\medicare.db
python app.py

# Linux/Mac:
rm database/medicare.db
python app.py
```

---

##  ¿Perderé mis datos?

**SÍ**, pero puedes crear nuevos rápidamente:

### Datos que se pierden:
-  Citas que hayas creado
-  Recetas personalizadas
-  Usuarios personalizados

### Datos que se recrean automáticamente:
-  Usuario admin: `admin` / `admin123`
-  10 doctores (uno por especialidad): `drcardiologia` / `doctor123`
-  3 pacientes de ejemplo: `mariagonzalez` / `paciente123`

---

##  Paso a Paso COMPLETO

### PASO 1: Elimina la BD antigua

```bash
python fix_db.py
```

**O manualmente:**
```bash
del database\medicare.db
```

### PASO 2: Inicia la aplicación

```bash
python app.py
```

**Verás:**
```
* Running on http://127.0.0.1:5000
```

### PASO 3: Abre el navegador

```
http://localhost:5000
```

### PASO 4: Inicia sesión

```
Usuario: admin
Contraseña: admin123
```

---

##  ¿Cómo sé que funcionó?

### 1. No hay errores en la consola
```
* Running on http://127.0.0.1:5000
(Sin errores de SQLite)
```

### 2. Puedes iniciar sesión
```
Login exitoso  Dashboard
```

### 3. Los doctores muestran estados
```
Lista de doctores:
Dr. Carlos Martínez - Disponible 🟢
Dra. Ana Castillo - Disponible 🟢
...
```

### 4. Puedes crear citas
```
Formulario de citas  Sin errores
```

---

##  Verificación Completa

### Test 1: Estructura de BD

```bash
python -c "import sqlite3; conn=sqlite3.connect('database/medicare.db'); c=conn.cursor(); c.execute('PRAGMA table_info(usuarios)'); print([col[1] for col in c.fetchall()])"
```

**Debe mostrar:**
```python
['id', 'nombre', 'email', 'username', 'password', 'role', 'especialidad', 
 'telefono', 'cedula', 'foto_perfil', 'fecha_registro', 'estado', 
 'estado_doctor', 'hora_inicio', 'hora_fin']
```

### Test 2: Usuarios creados

```bash
python -c "import sqlite3; conn=sqlite3.connect('database/medicare.db'); c=conn.cursor(); c.execute('SELECT username, role FROM usuarios'); print(c.fetchall())"
```

**Debe mostrar:**
```python
[('admin', 'admin'), ('drcardiologia', 'doctor'), ('drpediatria', 'doctor'), ...]
```

---

##  Usuarios Predeterminados

### Admin:
```
Usuario: admin
Contraseña: admin123
```

### Doctores (10):
```
drcardiologia     / doctor123
drpediatria       / doctor123
drtraumatologia   / doctor123
drneurologia      / doctor123
drendocrinologia  / doctor123
drmedicinainterna / doctor123
drginecologia     / doctor123
drdermatologia    / doctor123
droftalmologia    / doctor123
drpsiquiatria     / doctor123
```

### Pacientes (3):
```
mariagonzalez / paciente123
carlosperez   / paciente123
analopez      / paciente123
```

---

##  NO Funciona la Migración

**¿Por qué no usar `migrate_db.py`?**

El problema es que tu BD no tiene la tabla `usuarios` creada correctamente desde el principio. La migración solo agrega columnas a una tabla existente, pero si la tabla misma está mal formada, no puede arreglarse.

**Solución:** Empezar de cero con `fix_db.py` o eliminar manualmente.

---

##  Si Sigue Sin Funcionar

### Error: "Permission denied"

```bash
# Cierra TODOS los procesos de Python
# Ctrl+C en todas las terminales
# Luego intenta de nuevo:
del database\medicare.db
python app.py
```

### Error: "Database is locked"

```bash
# 1. Cierra VS Code o tu editor
# 2. Cierra todas las terminales
# 3. Espera 5 segundos
# 4. Abre nueva terminal
del database\medicare.db
python app.py
```

### Error persiste

```bash
# Elimina también el archivo WAL:
del database\medicare.db
del database\medicare.db-shm
del database\medicare.db-wal
python app.py
```

---

##  Consejo para el Futuro

### Para evitar este problema:

1. **Usa Git** para controlar versiones
2. **Haz backups** antes de actualizar:
   ```bash
   copy database\medicare.db database\backup_$(date).db
   ```
3. **Prueba en desarrollo** antes de producción

---

##  Resumen

```bash
# SOLUCIÓN EN 2 COMANDOS:
python fix_db.py
python app.py

# O EN 2 COMANDOS MANUALES:
del database\medicare.db
python app.py
```

**¡Eso es todo!** 

---

**Medicare v3.2 - Sistema de Gestión Médica**
