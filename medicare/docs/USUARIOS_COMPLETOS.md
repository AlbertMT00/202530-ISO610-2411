#  USUARIOS DEL SISTEMA MEDICARE - LISTA COMPLETA

##  ADMINISTRADOR

| Usuario | Contraseña | Email | Cédula |
|---------|------------|-------|--------|
| admin | admin123 | admin@medicare.com | 001-0000000-1 |

---

## ‍ DOCTORES (10 - Uno por Especialidad)

| # | Usuario | Contraseña | Nombre | Especialidad | Email | Teléfono | Cédula |
|---|---------|------------|--------|--------------|-------|----------|--------|
| 1 | drcardiologia | doctor123 | Dr. Carlos Martínez | Cardiología | cardiologia@medicare.com | 809-555-0101 | 001-1234567-8 |
| 2 | drpediatria | doctor123 | Dra. Ana Castillo | Pediatría | pediatria@medicare.com | 809-555-0102 | 001-2345678-9 |
| 3 | drtraumatologia | doctor123 | Dr. Roberto López | Traumatología | traumatologia@medicare.com | 809-555-0103 | 001-3456789-0 |
| 4 | drneurologia | doctor123 | Dra. Patricia González | Neurología | neurologia@medicare.com | 809-555-0104 | 001-4567890-1 |
| 5 | drendocrinologia | doctor123 | Dr. Miguel Pérez | Endocrinología | endocrinologia@medicare.com | 809-555-0105 | 001-5678901-2 |
| 6 | drmedicinainterna | doctor123 | Dra. Laura Ramírez | Medicina Interna | medicinainterna@medicare.com | 809-555-0106 | 001-6789012-3 |
| 7 | drginecologia | doctor123 | Dr. José Herrera | Ginecología | ginecologia@medicare.com | 809-555-0107 | 001-7890123-4 |
| 8 | drdermatologia | doctor123 | Dra. Carmen Santos | Dermatología | dermatologia@medicare.com | 809-555-0108 | 001-8901234-5 |
| 9 | droftalmologia | doctor123 | Dr. Francisco Ortiz | Oftalmología | oftalmologia@medicare.com | 809-555-0109 | 001-9012345-6 |
| 10 | drpsiquiatria | doctor123 | Dra. Elena Navarro | Psiquiatría | psiquiatria@medicare.com | 809-555-0110 | 001-0123456-7 |

---

##  PACIENTES (3 de Ejemplo)

| # | Usuario | Contraseña | Nombre | Email | Teléfono | Cédula |
|---|---------|------------|--------|-------|----------|--------|
| 1 | mariagonzalez | paciente123 | María González | maria@correo.com | 809-555-0201 | 001-1111111-1 |
| 2 | carlosperez | paciente123 | Carlos Pérez | carlos@correo.com | 809-555-0202 | 001-2222222-2 |
| 3 | analopez | paciente123 | Ana López | ana@correo.com | 809-555-0203 | 001-3333333-3 |

---

##  RESUMEN

### Total de Usuarios: **14**
- 1 Administrador
- 10 Doctores (uno por especialidad)
- 3 Pacientes de ejemplo

---

##  ESPECIALIDADES CUBIERTAS

1.  Cardiología - Dr. Carlos Martínez
2.  Pediatría - Dra. Ana Castillo
3.  Traumatología - Dr. Roberto López
4.  Neurología - Dra. Patricia González
5.  Endocrinología - Dr. Miguel Pérez
6.  Medicina Interna - Dra. Laura Ramírez
7.  Ginecología - Dr. José Herrera
8.  Dermatología - Dra. Carmen Santos
9.  Oftalmología - Dr. Francisco Ortiz
10.  Psiquiatría - Dra. Elena Navarro

---

##  ACCESO RÁPIDO

### Para Pruebas Rápidas:

**Administrador:**
```
Usuario: admin
Contraseña: admin123
```

**Doctor (Cualquiera):**
```
Usuario: drcardiologia
Contraseña: doctor123
```

**Paciente:**
```
Usuario: mariagonzalez
Contraseña: paciente123
```

---

##  NOTAS IMPORTANTES

### Todos los Doctores:
-  Contraseña: `doctor123`
-  Horario por defecto: 08:00 - 17:00
-  Estado inicial: Disponible
-  Pueden crear citas para cualquier paciente
-  Pueden emitir recetas
-  Pueden atender urgencias

### Todos los Pacientes:
-  Contraseña: `paciente123`
-  Solo pueden crear citas para sí mismos
-  Pueden reportar urgencias 24/7
-  Pueden ver sus recetas

### Administrador:
-  Contraseña: `admin123`
-  Acceso completo al sistema
-  Puede agregar más doctores
-  Puede gestionar usuarios
-  Puede supervisar todo

---

##  CÓMO CREAR MÁS USUARIOS

### Desde la Aplicación (Como Admin):

```
1. Login como admin
2. Ve a "Agregar Doctor"
3. Llena el formulario
4. Selecciona especialidad
5. Asigna horario
6.  Nuevo doctor creado
```

### Pacientes:

```
1. Ve a la página principal
2. Click en "Registrarse"
3. Llena el formulario
4. Selecciona role: Paciente
5.  Nuevo paciente creado
```

---

##  RESETEAR USUARIOS

### Si necesitas empezar de cero:

```bash
del database\medicare.db
python app.py
```

Esto recrea todos los 14 usuarios automáticamente.

---

##  BACKUP DE USUARIOS

### Recomendado antes de cambios:

```bash
copy database\medicare.db database\backup_usuarios.db
```

---

##  ESTADÍSTICAS DEL SISTEMA

### Capacidad del Sistema:
-  Ilimitados usuarios
-  10 especialidades activas
-  Múltiples doctores por especialidad (configurable)
-  Múltiples pacientes
-  Citas ilimitadas

### Usuarios Activos Iniciales:
- 1 Admin
- 10 Doctores (activos)
- 3 Pacientes (activos)

---

##  USUARIOS PARA CAPACITACIÓN

### Recomendado para Demos:

**Mostrar Panel de Admin:**
- Usuario: `admin` / `admin123`

**Mostrar Panel de Doctor:**
- Usuario: `drcardiologia` / `doctor123`

**Mostrar Panel de Paciente:**
- Usuario: `mariagonzalez` / `paciente123`

---

##  VERIFICACIÓN DE USUARIOS

### Comprobar que están todos:

```bash
python -c "import sqlite3; conn=sqlite3.connect('database/medicare.db'); c=conn.cursor(); c.execute('SELECT username, role FROM usuarios'); print('\n'.join([f'{r[0]} - {r[1]}' for r in c.fetchall()]))"
```

**Debe mostrar:**
```
admin - admin
drcardiologia - doctor
drpediatria - doctor
drtraumatologia - doctor
drneurologia - doctor
drendocrinologia - doctor
drmedicinainterna - doctor
drginecologia - doctor
drdermatologia - doctor
droftalmologia - doctor
drpsiquiatria - doctor
mariagonzalez - paciente
carlosperez - paciente
analopez - paciente
```

---

##  ACCESO RÁPIDO SEGÚN ESPECIALIDAD

| Especialidad | Usuario | Contraseña |
|--------------|---------|------------|
| Cardiología | drcardiologia | doctor123 |
| Pediatría | drpediatria | doctor123 |
| Traumatología | drtraumatologia | doctor123 |
| Neurología | drneurologia | doctor123 |
| Endocrinología | drendocrinologia | doctor123 |
| Medicina Interna | drmedicinainterna | doctor123 |
| Ginecología | drginecologia | doctor123 |
| Dermatología | drdermatologia | doctor123 |
| Oftalmología | droftalmologia | doctor123 |
| Psiquiatría | drpsiquiatria | doctor123 |

---

**Medicare v3.3 - Sistema Completo con 14 Usuarios**
 10 Especialidades |  14 Usuarios |  100% Funcional
