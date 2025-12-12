#  Sistema de Migraciones - Medicare

## ¿Qué son las Migraciones?

Las migraciones permiten **actualizar la estructura de la base de datos sin perder datos existentes**. Es como hacer una "renovación" de tu casa sin tirar todo y empezar de cero.

---

##  Dos Formas de Migrar

### Opción 1: Automática (Recomendada)

**Al iniciar la aplicación, se migra automáticamente:**

```bash
python app.py
```

El sistema detectará automáticamente las columnas faltantes y las agregará. Verás mensajes como:

```
 Migración aplicada: Campo 'cedula' agregado
 Migración aplicada: Campo 'estado_doctor' agregado
 Migración aplicada: Campo 'hora_inicio' agregado
```

### Opción 2: Manual (Más Control)

**Ejecuta el script de migración:**

```bash
python migrate_db.py
```

Este script:
-  Muestra información detallada
-  Aplica todas las migraciones necesarias
-  Te muestra qué cambios se hicieron
-  Permite confirmar antes de cambios mayores

---

##  Migraciones Incluidas

### Versión 2.0  3.0

| Migración | Campo | Tipo | Valor por Defecto |
|-----------|-------|------|-------------------|
| 1 | `cedula` | TEXT UNIQUE | NULL |
| 2 | `foto_perfil` | TEXT | 'default.png' |
| 3 | `estado_doctor` | TEXT | 'disponible' |
| 4 | `hora_inicio` | TEXT | '08:00' |
| 5 | `hora_fin` | TEXT | '17:00' |

---

##  Uso Paso a Paso

### Si Tienes una Base de Datos Antigua:

#### Paso 1: Verifica tu versión
```bash
python migrate_db.py
```

#### Paso 2: Lee el reporte
El script te dirá:
-  Columnas que ya tienes
-  Migraciones que se aplicarán
-  Resultado final

#### Paso 3: Inicia la aplicación
```bash
python app.py
```

---

##  Ventajas de las Migraciones

### Con Migraciones:
-  **Mantienes todos tus datos**
-  Citas existentes se conservan
-  Usuarios se mantienen
-  Recetas no se pierden
-  Solo se agregan las columnas nuevas

### Sin Migraciones (resetear):
-  Pierdes todas las citas
-  Pierdes todos los usuarios personalizados
-  Pierdes todas las recetas
-  Base de datos completamente nueva

---

##  Cómo Funciona

### 1. Detección Automática
```python
# El sistema verifica qué columnas existen
columnas_actuales = ["id", "nombre", "email", "username", "password"]

# Y compara con las columnas necesarias
columnas_necesarias = ["id", "nombre", "email", "username", 
                       "password", "cedula", "estado_doctor", ...]
```

### 2. Aplicación Selectiva
```python
# Solo agrega las que faltan
for columna_faltante in columnas_necesarias:
    if columna_faltante not in columnas_actuales:
        agregar_columna(columna_faltante)
```

### 3. Sin Interrupciones
- Las migraciones se aplican en milisegundos
- No afectan los datos existentes
- Son completamente seguras

---

##  Casos de Uso

### Caso 1: Primera Instalación
```bash
# No hay base de datos
python app.py
#  Se crea nueva con toda la estructura
```

### Caso 2: Actualizar de v1 a v3
```bash
# Tienes BD antigua con usuarios y citas
python migrate_db.py
#  Se agregan columnas nuevas
#  Datos existentes se mantienen

python app.py
#  Todo funciona con datos antiguos + columnas nuevas
```

### Caso 3: Ya estás en v3
```bash
python app.py
#  No hace nada, ya está actualizada
```

---

##  Limitaciones

### SQLite no permite:
-  Eliminar columnas
-  Cambiar tipo de dato
-  Renombrar columnas (directamente)

### Si necesitas cambios mayores:
```bash
# Opción 1: Backup y reseteo
copy database\medicare.db database\medicare_backup.db
del database\medicare.db
python app.py

# Opción 2: Exportar datos, resetear, reimportar
# (Para esto necesitarías un script personalizado)
```

---

##  Verificar Migraciones Aplicadas

### Opción 1: Desde Python
```bash
python migrate_db.py
```

Salida:
```
============================================================
  MIGRACIÓN DE BASE DE DATOS - Medicare v3.0
============================================================

 Base de datos encontrada: database/medicare.db
 Columnas actuales: 14

 Campo 'cedula' ya existe
 Campo 'foto_perfil' ya existe
 Campo 'estado_doctor' ya existe
 Campo 'hora_inicio' ya existe
 Campo 'hora_fin' ya existe

============================================================
 Migración completada exitosamente
 Total de cambios aplicados: 0
 Columnas actuales: 14

Columnas en la tabla usuarios:
  - id
  - nombre
  - email
  - username
  - password
  - role
  - especialidad
  - telefono
  - cedula
  - foto_perfil
  - fecha_registro
  - estado
  - estado_doctor
  - hora_inicio
  - hora_fin

 Puedes iniciar la aplicación: python app.py
============================================================
```

### Opción 2: Usando SQLite
```bash
sqlite3 database/medicare.db ".schema usuarios"
```

---

##  Resumen

### Para Actualizar (CON DATOS):
```bash
python migrate_db.py  # Ver qué se hará
python app.py         # Aplicar y usar
```

### Para Empezar de Cero (SIN DATOS):
```bash
del database\medicare.db
python app.py
```

### Ambas Funcionan
- Primera opción: Mantiene datos 
- Segunda opción: Base limpia 

---

##  Troubleshooting

### Error: "table usuarios has no column named X"

**Solución:**
```bash
python migrate_db.py
```

Si el error persiste:
```bash
del database\medicare.db
python app.py
```

### Error al migrar

**Solución:**
1. Haz backup:
   ```bash
   copy database\medicare.db database\backup.db
   ```

2. Intenta de nuevo:
   ```bash
   python migrate_db.py
   ```

3. Si falla, resetea:
   ```bash
   del database\medicare.db
   python app.py
   ```

---

##  Mejores Prácticas

### 1. **Siempre haz backup antes de migrar**
```bash
copy database\medicare.db database\medicare_backup_$(date).db
```

### 2. **Prueba en desarrollo primero**
- Nunca migres directamente en producción
- Prueba las migraciones en tu PC primero

### 3. **Verifica después de migrar**
```bash
python migrate_db.py  # Ver estado
```

### 4. **Documenta cambios personalizados**
Si modificas la BD manualmente, documenta los cambios

---

**Sistema de Migraciones Medicare v3.0**
¡Actualiza sin perder datos! 
