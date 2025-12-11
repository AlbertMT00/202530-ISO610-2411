#  Medicare - Sistema Médico v4.8

Sistema de gestión médica completo con citas, recetas, urgencias y gestión de doctores.

##  Estructura del Proyecto

```
medicare/
  README.md           # Esta guía
  app.py              # Aplicación Flask principal
  start.sh            # Script de inicio rápido

  database/           # Base de datos
    medicare.db       # SQLite database

  templates/          # Plantillas HTML (Jinja2)
    base.html         # Template base
    login.html        # Login/Register
    citas.html        # Gestión de citas
    doctores.html     # Lista doctores
    recetas.html      # Recetas médicas
    ...

  static/             # Archivos estáticos
    css/              # Estilos
    js/               # JavaScript
    uploads/          # Archivos subidos

  scripts/            # Scripts de utilidad
    migrate_especialidad.py
    fix_servicio.py
    agregar_doctores.py
    listar_usuarios.py
    ...

  docs/               # Documentación
     README.md         # Documentación principal
     USUARIOS_ACTUALIZADOS.txt  # Lista de usuarios
     USUARIOS_COMPLETOS.md
    
     guias/            # Guías de uso
        INSTALACION.md
        TOUR_VISUAL.md
        COMO_TENER_10_DOCTORES.md
        INDICE.md
    
     historial/        # Historial de versiones
         CAMBIOS.md
         MEJORAS_V2.md
         MEJORAS_V3.md
         VERSION.txt
         ...
```

##  Inicio Rápido

```bash
# 1. Instalar dependencias
pip install flask werkzeug

# 2. Ejecutar migraciones
python scripts/migrate_especialidad.py
python scripts/fix_servicio.py

# 3. Iniciar aplicación
python app.py

# O usar el script de inicio:
bash start.sh
```

##  Usuarios por Defecto

### Admin
- Usuario: `admin`
- Contraseña: `admin123`

### Doctores (19 especialidades)
- Ver: `docs/USUARIOS_ACTUALIZADOS.txt`
- Contraseña: `doctor123`

### Pacientes
- Usuario: `mariagonzalez`, `carlosperez`, `analopez`
- Contraseña: `paciente123`

##  Características v4.8

-  Sidebar sticky (se queda fijo al hacer scroll)
-  Panel de doctor sticky (botón "Agendar cita" siempre visible)
-  Búsqueda inteligente (especialidad y doctor)
-  Auto-fill bidireccional (doctor  especialidad)
-  Botón "Agendar cita" desde perfil funciona correctamente
-  Validación: un paciente = una cita por hora
-  19 especialidades médicas
-  Sistema de urgencias
-  Gestión de recetas (crear, editar, eliminar)
-  Navegación clickeable (logo  inicio, avatar  configuración)
-  Estructura de archivos organizada

##  Documentación

### Archivos Principales
- `docs/README.md` - Documentación completa
- `docs/USUARIOS_ACTUALIZADOS.txt` - Lista de usuarios

### Guías
- `docs/guias/INSTALACION.md` - Instalación detallada
- `docs/guias/TOUR_VISUAL.md` - Tour visual del sistema
- `docs/guias/COMO_TENER_10_DOCTORES.md` - Gestión de doctores

### Historial
- `docs/historial/CAMBIOS.md` - Historial de cambios
- `docs/historial/VERSION.txt` - Control de versiones
- `docs/historial/MEJORAS_V*.md` - Mejoras por versión

##  Scripts Útiles

```bash
# Listar todos los usuarios
python scripts/listar_usuarios.py

# Agregar doctores
python scripts/agregar_doctores.py

# Verificar contraseñas
python scripts/arreglar_passwords.py

# Migrar base de datos
python scripts/migrate_especialidad.py
python scripts/fix_servicio.py
```

##  Acceso

Una vez iniciado, accede a:
```
http://127.0.0.1:5000
```

##  Soporte

Para dudas o problemas:
1. Revisa la documentación en `docs/`
2. Ejecuta `python scripts/listar_usuarios.py` para ver usuarios
3. Verifica que las migraciones estén ejecutadas

---

**Medicare v4.8** - Sistema Médico Completo 
