#  SOLUCIÓN: Tener los 10 Doctores

##  IMPORTANTE

**Los 10 doctores SÍ están en el código `app.py`**

Pero solo se crean cuando la base de datos **NO EXISTE**.

Si ya tienes una BD antigua, no los crea.

---

##  SOLUCIÓN RÁPIDA (Recomendada)

```bash
# Paso 1: Elimina la base de datos antigua
del database\medicare.db

# Paso 2: Inicia la app
python app.py

# Paso 3: ¡Listo! Los 10 doctores están creados
```

---

##  SOLUCIÓN SIN PERDER DATOS

Si NO quieres perder tus datos (citas, pacientes, etc.), usa el script:

```bash
python verificar_doctores.py
```

**El script:**
1. Cuenta cuántos doctores tienes
2. Te muestra cuáles faltan
3. Te pregunta si quieres agregarlos
4. Los agrega automáticamente

---

##  LOS 10 DOCTORES

| # | Username | Nombre | Especialidad |
|---|----------|--------|--------------|
| 1 | drcardiologia | Dr. Carlos Martínez | Cardiología |
| 2 | drpediatria | Dra. Ana Castillo | Pediatría |
| 3 | drtraumatologia | Dr. Roberto López | Traumatología |
| 4 | drneurologia | Dra. Patricia González | Neurología |
| 5 | drendocrinologia | Dr. Miguel Pérez | Endocrinología |
| 6 | drmedicinainterna | Dra. Laura Ramírez | Medicina Interna |
| 7 | drginecologia | Dr. José Herrera | Ginecología |
| 8 | drdermatologia | Dra. Carmen Santos | Dermatología |
| 9 | droftalmologia | Dr. Francisco Ortiz | Oftalmología |
| 10 | drpsiquiatria | Dra. Elena Navarro | Psiquiatría |

**Todos con contraseña:** `doctor123`

---

##  ¿Cómo Verificar que Están?

```bash
python -c "import sqlite3; conn=sqlite3.connect('database/medicare.db'); c=conn.cursor(); c.execute('SELECT COUNT(*) FROM usuarios WHERE role=\"doctor\"'); print(f'Doctores: {c.fetchone()[0]}')"
```

**Debe mostrar:**
```
Doctores: 10
```

---

##  Ver Lista de Doctores

```bash
python -c "import sqlite3; conn=sqlite3.connect('database/medicare.db'); c=conn.cursor(); c.execute('SELECT nombre, especialidad FROM usuarios WHERE role=\"doctor\"'); [print(f'{i+1}. {r[0]} - {r[1]}') for i, r in enumerate(c.fetchall())]"
```

---

##  ¿Por Qué No Aparecen?

**Código en `app.py` líneas 147-165:**
```python
# Crear un doctor por cada especialidad
doctor_password = generate_password_hash('doctor123')
especialidades = [
    ('Dr. Carlos Martínez', 'cardiologia@medicare.com', 'drcardiologia', 'Cardiología', ...),
    ('Dra. Ana Castillo', 'pediatria@medicare.com', 'drpediatria', 'Pediatría', ...),
    # ... 8 doctores más
]

for nombre, email, username, especialidad, telefono, cedula in especialidades:
    c.execute('''INSERT INTO usuarios ...''')
```

**Pero línea 142:**
```python
c.execute("SELECT COUNT(*) FROM usuarios WHERE username = 'admin'")
if c.fetchone()[0] == 0:
    # SOLO ENTRA AQUÍ SI NO HAY ADMIN
    # Crea admin + 10 doctores + 3 pacientes
```

**Conclusión:**
- Si ya tienes admin  No entra al bloque  No crea doctores
- Si eliminas BD  No hay admin  Entra al bloque  Crea todo

---

##  HAZLO AHORA

### Opción A: Empezar de Cero (10 segundos)

```bash
del database\medicare.db
python app.py
```

### Opción B: Mantener Datos (30 segundos)

```bash
python verificar_doctores.py
# Escribe: s
```

---

##  DESPUÉS DE HACERLO

**Verifica:**
```bash
# Login como admin
Usuario: admin
Contraseña: admin123

# Ve a "Usuarios"
# Debes ver:
- 1 Administrador
- 10 Doctores
- 3 Pacientes
Total: 14 usuarios
```

---

**¡ELIMINA LA BD Y EJECUTA LA APP!**

```bash
del database\medicare.db
python app.py
```

**Eso es TODO lo que necesitas hacer.**
