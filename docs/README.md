# Sistema Medicare - Gestión Médica

Sistema completo de gestión médica con roles diferenciados para administradores, doctores y pacientes.

##  Características Principales

### ‍ Rol de Administrador
- Gestionar todos los usuarios del sistema
- Agregar nuevos doctores
- Ver estadísticas generales
- Supervisar citas y urgencias

### ‍ Rol de Doctor
- Acceso completo a citas (puede agendar para cualquier paciente)
- Crear y gestionar recetas médicas
- Atender urgencias
- Ver historial de pacientes
- Dashboard con estadísticas diarias

###  Rol de Paciente
- Agendar citas (solo para sí mismo)
- Ver recetas recetadas
- Reportar urgencias
- Buscar doctores por especialidad
- Dashboard personalizado

##  Instalación

### 1. Instalar dependencias

```bash
pip install flask werkzeug --break-system-packages
```

### 2. Ejecutar la aplicación

```bash
cd /home/claude/medicare
python app.py
```

La aplicación estará disponible en: http://localhost:5000

##  Usuarios de Prueba

### Administrador
- Usuario: `admin`
- Contraseña: `admin123`

### Doctores
- Usuario: `drmartinez`
- Contraseña: `doctor123`
- Especialidad: Cardiología

- Usuario: `dracastillo`
- Contraseña: `doctor123`
- Especialidad: Pediatría

### Pacientes
- Usuario: `mariagonzalez`
- Contraseña: `paciente123`

- Usuario: `carlosperez`
- Contraseña: `paciente123`

- Usuario: `analopez`
- Contraseña: `paciente123`

##  Base de Datos

El sistema utiliza SQLite con las siguientes tablas:

1. **usuarios** - Almacena doctores, pacientes y administradores
2. **citas** - Gestiona las citas médicas
3. **recetas** - Almacena recetas médicas
4. **urgencias** - Maneja reportes de urgencias

La base de datos se crea automáticamente en `database/medicare.db` al iniciar la aplicación.

##  Funcionalidades por Módulo

### Citas
- Doctor: Puede agendar citas para cualquier paciente (seleccionar de lista)
- Paciente: Solo puede agendar citas para sí mismo (auto-relleno)
- Ambos pueden ver sus citas respectivas
- Estados: confirmada, completada, cancelada

### Recetas
- Solo doctores pueden crear recetas
- Pacientes solo pueden ver sus recetas
- Campos: medicamento, dosis, frecuencia, duración, indicaciones
- Opción de impresión

### Urgencias
- Pacientes pueden reportar urgencias 24/7
- Niveles de prioridad: baja, media, alta, crítica
- Doctores pueden atender y resolver urgencias
- Estados: pendiente, en_atención, resuelta

### Doctores
- Listado con filtros por nombre y especialidad
- Perfiles detallados de cada doctor
- Disponible para todos los usuarios

##  Seguridad

- Contraseñas hasheadas con werkzeug.security
- Sistema de sesiones con Flask
- Validación de roles para rutas protegidas
- Protección contra inyección SQL con queries parametrizadas

##  Responsive

El sistema es completamente responsive y funciona en:
- Desktop
- Tablets
- Móviles

##  Diseño

- Diseño moderno con gradientes y sombras
- Paleta de colores profesional
- Tipografía Inter
- Componentes reutilizables
- Animaciones suaves

##  Estructura de Archivos

```
medicare/
 app.py                 # Aplicación Flask principal
 database/
    medicare.db       # Base de datos SQLite
 static/
    css/
       site.css      # Estilos CSS
    js/
        site.js       # JavaScript
 templates/
     base.html                    # Template base
     index.html                   # Página de inicio
     login.html                   # Login
     register.html                # Registro
     admin_dashboard.html         # Dashboard admin
     doctor_dashboard.html        # Dashboard doctor
     paciente_dashboard.html      # Dashboard paciente
     admin_usuarios.html          # Gestión usuarios
     admin_agregar_doctor.html    # Agregar doctor
     citas.html                   # Módulo de citas
     recetas.html                 # Módulo de recetas
     doctores.html                # Lista de doctores
     urgencias.html               # Módulo de urgencias
```

##  Soporte

Para soporte técnico:
- Email: soporte@medicare.com
- Teléfono: 849-432-2213
- Emergencias: emergencias@medicare.com

##  Notas Adicionales

- La base de datos se resetea cada vez que se reinicia el servidor (en producción esto no debería ocurrir)
- Se pueden agregar más especialidades editando las opciones en los formularios
- Los horarios de los doctores son fijos pero se pueden personalizar
- El sistema está listo para ser extendido con más funcionalidades

##  Próximas Mejoras Sugeridas

- Sistema de notificaciones por email
- Chat en tiempo real con doctores
- Historial médico completo del paciente
- Sistema de facturación
- Reportes y estadísticas avanzadas
- Integración con calendario
- Videollamadas para consultas remotas

---

**Desarrollado con  para Medicare**
Versión 1.0.0 - Diciembre 2024
