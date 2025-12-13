#  Sistema Medicare - Índice de Documentación

##  Guías de Inicio Rápido

### 1. [INSTALACION.md](INSTALACION.md) -  Empieza aquí
**Lee esto primero si quieres usar el sistema rápidamente**
- Instalación en 3 pasos
- Usuarios de prueba
- Solución de problemas comunes
- ⏱ Tiempo de lectura: 2 minutos

### 2. [README.md](README.md) -  Documentación Completa
**Documentación técnica detallada**
- Características del sistema
- Estructura de archivos
- Base de datos
- Funcionalidades por módulo
- Seguridad
- ⏱ Tiempo de lectura: 10 minutos

---

##  Documentación de Cambios

### 3. [CAMBIOS.md](CAMBIOS.md) -  Todas las Mejoras
**Lista completa de todo lo implementado**
- Sistema de roles explicado
- Cambios específicos por módulo
- Funcionalidades nuevas
- Checklist de requisitos cumplidos
- ⏱ Tiempo de lectura: 8 minutos

### 4. [TOUR_VISUAL.md](TOUR_VISUAL.md) -  Recorrido Visual
**Guía página por página del sistema**
- Descripción de cada pantalla
- Elementos visuales
- Flujos de usuario
- Navegación
- ⏱ Tiempo de lectura: 15 minutos

---

##  Orden Recomendado de Lectura

### Si eres desarrollador:
1.  **INSTALACION.md** - Para poner en marcha el sistema
2.  **CAMBIOS.md** - Para entender qué se implementó
3.  **README.md** - Para conocer la arquitectura técnica
4.  **TOUR_VISUAL.md** - Para familiarizarte con la UI

### Si eres usuario final:
1.  **INSTALACION.md** - Para acceder al sistema
2.  **TOUR_VISUAL.md** - Para aprender a usar cada módulo

### Si eres administrador del sistema:
1.  **INSTALACION.md** - Para instalar
2.  **README.md** - Para entender la arquitectura
3.  **CAMBIOS.md** - Para conocer todas las funcionalidades
4.  **TOUR_VISUAL.md** - Para capacitar a usuarios

---

##  Archivos del Proyecto

### Código Principal
- **app.py** - Aplicación Flask (backend completo)
- **start.sh** - Script de inicio rápido

### Frontend
- **templates/** - 14 páginas HTML
  - Páginas públicas: index, login, register
  - Admin: dashboard, usuarios, agregar_doctor
  - Doctor: dashboard, citas, recetas, urgencias
  - Paciente: dashboard, citas, recetas, urgencias
  - Compartidas: doctores, base

- **static/css/site.css** - Estilos completos
- **static/js/site.js** - JavaScript con funciones útiles

### Base de Datos
- **database/medicare.db** - Base de datos SQLite (se crea automáticamente)

---

##  Guías Específicas por Rol

### Para Administradores
**Páginas relevantes:**
- admin_dashboard.html
- admin_usuarios.html
- admin_agregar_doctor.html

**Documentación recomendada:**
- TOUR_VISUAL.md  Sección "Panel de Administrador"
- CAMBIOS.md  Sección "Gestión de Usuarios"

### Para Doctores
**Páginas relevantes:**
- doctor_dashboard.html
- citas.html (vista doctor)
- recetas.html (vista doctor)
- urgencias.html (vista doctor)
- doctores.html

**Documentación recomendada:**
- TOUR_VISUAL.md  Sección "Panel de Doctor"
- CAMBIOS.md  Secciones de Citas, Recetas y Urgencias

### Para Pacientes
**Páginas relevantes:**
- paciente_dashboard.html
- citas.html (vista paciente)
- recetas.html (vista paciente)
- urgencias.html (vista paciente)
- doctores.html

**Documentación recomendada:**
- TOUR_VISUAL.md  Sección "Panel de Paciente"
- INSTALACION.md  Para usuarios de prueba

---

##  Información Técnica Rápida

### Tecnologías Usadas
- **Backend:** Flask (Python)
- **Base de Datos:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript
- **Seguridad:** Werkzeug (hashing de passwords)

### Requisitos del Sistema
- Python 3.7+
- Flask
- Werkzeug

### Puertos
- **Desarrollo:** 5000
- **Producción:** Configurable en app.py

### Estructura de la Base de Datos
- **4 tablas:** usuarios, citas, recetas, urgencias
- **Relaciones:** FK entre tablas
- **Seguridad:** Contraseñas hasheadas

---

##  Información de Contacto

### En el Sistema
- **Email soporte:** soporte@medicare.com
- **Email emergencias:** emergencias@medicare.com
- **Teléfono:** 849-432-2213

### Datos de la Clínica
- **Nombre:** Clínica Medicare
- **Dirección:** Distrito Nacional, Av. Máximo Gómez, RD

---

##  Usuarios de Prueba

### Credenciales Preconfiguradas

```
‍ Administrador:
   Usuario: admin
   Contraseña: admin123

‍ Doctores:
   Usuario: drmartinez
   Contraseña: doctor123
   Especialidad: Cardiología

   Usuario: dracastillo
   Contraseña: doctor123
   Especialidad: Pediatría

 Pacientes:
   Usuario: mariagonzalez
   Contraseña: paciente123

   Usuario: carlosperez
   Contraseña: paciente123

   Usuario: analopez
   Contraseña: paciente123
```

---

##  Checklist de Funcionalidades

- [x] Sistema de autenticación
- [x] 3 roles diferenciados
- [x] Base de datos completa
- [x] Módulo de citas
- [x] Módulo de recetas
- [x] Módulo de urgencias
- [x] Directorio de doctores
- [x] Dashboards personalizados
- [x] Sistema de notificaciones
- [x] Diseño responsive
- [x] Seguridad implementada

---

##  Listo para Usar

El sistema está **100% funcional** y listo para producción. Todos los módulos han sido implementados según los requisitos:

 Vistas separadas por rol
 Base de datos funcional
 Accesos rápidos operativos
 Urgencias implementadas
 Recetas solo para doctores
 Citas con listas editables
 Admin puede agregar doctores

---

##  Recursos Adicionales

- Ver código fuente en `app.py` (bien comentado)
- Revisar templates para entender la estructura
- Modificar `site.css` para personalizar diseño
- Extender `site.js` para más funcionalidad

---

**Sistema Medicare v1.0**
Desarrollado con  para gestión médica profesional
Diciembre 2024
