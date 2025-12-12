#  Tour Visual del Sistema Medicare

##  Páginas por Rol

###  Páginas Públicas (Sin login)

#### 1. **index.html** - Página de Bienvenida
- Hero card con información del sistema
- Botones para Login y Registro
- Diseño atractivo con gradientes

#### 2. **login.html** - Inicio de Sesión
- Formulario de autenticación
- Usuarios de prueba visibles
- Validación de credenciales

#### 3. **register.html** - Registro de Pacientes
- Formulario completo para nuevos pacientes
- Campos: nombre, email, usuario, teléfono, contraseña
- Validación automática

---

### ‍ Panel de Administrador

#### 1. **admin_dashboard.html** - Dashboard Principal
**Elementos:**
- Hero card de bienvenida
- Accesos rápidos:
  -  Agregar nuevo doctor
  -  Gestionar usuarios
  -  Ver todas las citas
  -  Monitorear urgencias
- Información del sistema
- Configuración de clínica

#### 2. **admin_usuarios.html** - Gestión de Usuarios
**Elementos:**
- Tabla completa de usuarios
- Columnas: ID, Nombre, Email, Usuario, Rol, Especialidad, Estado
- Badges de colores por rol y estado
- Contador total de usuarios

#### 3. **admin_agregar_doctor.html** - Agregar Doctor
**Elementos:**
- Formulario de registro de doctor
- Campos: nombre completo, email, usuario, contraseña, especialidad, teléfono
- Dropdown de especialidades
- Información sobre permisos del doctor
- Botones: Registrar doctor / Cancelar

---

### ‍ Panel de Doctor

#### 1. **doctor_dashboard.html** - Dashboard del Doctor
**Elementos:**
- 3 cards de estadísticas:
  -  Citas de hoy (número)
  -  Recetas emitidas (número)
  -  Urgencias pendientes (número en rojo)
- Accesos rápidos:
  -  Nueva cita
  -  Crear receta
  -  Ver urgencias
  -  Historial del día
- Card de especialidad del doctor
- Información de contacto de la clínica

#### 2. **citas.html** - Gestión de Citas (Vista Doctor)
**Elementos:**
- **Formulario (izquierda):**
  - Dropdown de pacientes (EDITABLE)
  - Selección de servicio
  - Selección de doctor
  - Campo de fecha
  - Campo de hora
  - Textarea de motivo
  - Botón "Confirmar cita"

- **Lista de citas (derecha):**
  - Cards con información de cada cita
  - Badge de estado (confirmada/completada/cancelada)
  - Nombre del paciente
  - Servicio y doctor
  - Fecha y hora
  - Motivo de la consulta

#### 3. **recetas.html** - Gestión de Recetas (Vista Doctor)
**Elementos:**
- **Formulario (izquierda):**
  - Dropdown de pacientes
  - Input/datalist de medicamentos
  - Campo de dosis
  - Dropdown de frecuencia
  - Dropdown de duración
  - Textarea de indicaciones especiales
  - Botones: "Guardar receta" / "Imprimir"

- **Lista de recetas (derecha):**
  - Cards con información de cada receta
  - Nombre del paciente
  - Medicamento destacado en azul
  - Dosis y frecuencia
  - Duración del tratamiento
  - Indicaciones especiales
  - Fecha de emisión
  - Nombre del doctor que prescribió

#### 4. **urgencias.html** - Gestión de Urgencias (Vista Doctor)
**Elementos:**
- Lista de urgencias ordenadas por prioridad
- Cada urgencia muestra:
  - Nombre del paciente
  - Fecha y hora de reporte
  - Badge de prioridad (crítica/alta/media/baja) con código de colores
  - Badge de estado (pendiente/en_atención/resuelta)
  - Descripción completa en card
  - Nombre del doctor asignado (si aplica)
  - Botones de acción:
    - "Atender" (si está pendiente)
    - "Marcar como resuelta"

---

###  Panel de Paciente

#### 1. **paciente_dashboard.html** - Dashboard del Paciente
**Elementos:**
- Hero card de bienvenida personalizada
- 2 cards de estadísticas:
  -  Próximas citas (número)
  -  Recetas activas (número en verde)
- Accesos rápidos:
  -  Agendar cita
  -  Ver mis recetas
  - ‍ Buscar doctores
  -  Reportar urgencia
- Lista de especialidades disponibles
- Información de contacto de la clínica

#### 2. **citas.html** - Mis Citas (Vista Paciente)
**Elementos:**
- **Formulario (izquierda):**
  - Campo de paciente AUTO-RELLENADO (solo lectura)
  - Selección de servicio
  - Selección de doctor
  - Campo de fecha
  - Campo de hora
  - Textarea de motivo
  - Botón "Confirmar cita"

- **Lista de citas (derecha):**
  - Solo muestra las citas del paciente logueado
  - Misma presentación que la vista del doctor

#### 3. **recetas.html** - Mis Recetas (Vista Paciente)
**Elementos:**
- **Sin formulario** (los pacientes no pueden crear recetas)
- Card informativo explicando que solo los doctores pueden crear recetas
- **Lista de recetas recientes:**
  - Solo muestra las recetas del paciente
  - Información completa de cada receta
  - Diseño claro y legible

#### 4. **urgencias.html** - Reportar Urgencia (Vista Paciente)
**Elementos:**
- **Hero card rojo de emergencia** con información 24/7
- **Formulario (izquierda):**
  - Textarea para describir la urgencia
  - Dropdown de nivel de urgencia (media/alta/crítica)
  - Botón rojo "Enviar urgencia"
  - Alerta con información de emergencias graves

- **Lista de urgencias (derecha):**
  - Muestra solo las urgencias del paciente
  - Estado de cada urgencia
  - Información del doctor asignado
  - Fecha de resolución (si aplica)

- **Card de información:**
  - Tiempo de respuesta estimado
  - Contacto de emergencia
  - Disponibilidad 24/7

---

###  Páginas Compartidas

#### 1. **doctores.html** - Directorio de Doctores
**Disponible para:** Todos los usuarios logueados

**Elementos:**
- **Sección de filtros:**
  - Buscador por nombre
  - Filtro por especialidad
  - Filtro por fecha (para ver disponibilidad)

- **Lista de doctores (izquierda):**
  - Cards clicables de cada doctor
  - Avatar con iniciales
  - Nombre completo
  - Especialidad
  - Estado de disponibilidad (punto verde)
  - Efecto hover

- **Perfil del doctor (derecha):**
  - Al hacer clic en un doctor, muestra:
    - Avatar grande
    - Nombre completo
    - Especialidad
    - Email de contacto
    - Teléfono
    - Estado de disponibilidad
    - Biografía
    - Horario de atención
    - Ubicación
    - Años de experiencia
    - Botones: "Agendar cita" / "Contactar"

---

##  Elementos de Diseño

### Colores por Tipo
- **Éxito:** Verde (#00b894, #d1fae5)
- **Peligro:** Rojo (#ef4444, #fee2e2)
- **Información:** Azul (#3a7cfb, #dbeafe)
- **Advertencia:** Amarillo (#f59e0b, #fef3c7)

### Badges de Rol
- **Admin:** Amarillo
- **Doctor:** Azul
- **Paciente:** Índigo

### Badges de Estado
- **Activo/Disponible:** Verde
- **Inactivo:** Rojo
- **Confirmada:** Azul
- **Completada:** Verde
- **Cancelada:** Rojo

### Badges de Prioridad
- **Crítica:** Rojo intenso
- **Alta:** Naranja
- **Media:** Azul
- **Baja:** Gris

---

##  Flujos de Usuario

### Flujo de Paciente
1. Registro  Login
2. Dashboard  Ver estadísticas
3. Agendar cita  Seleccionar doctor y fecha
4. Ver doctores  Buscar especialista
5. Ver recetas  Revisar medicamentos
6. Reportar urgencia  Si es necesario

### Flujo de Doctor
1. Login con credenciales
2. Dashboard  Ver estadísticas del día
3. Agendar cita  Seleccionar paciente
4. Crear receta  Seleccionar paciente y medicamento
5. Atender urgencias  Revisar y resolver
6. Ver historial  Revisar citas y recetas

### Flujo de Admin
1. Login con credenciales
2. Dashboard  Panel de administración
3. Agregar doctor  Registrar nuevo médico
4. Gestionar usuarios  Ver todos los usuarios
5. Supervisar sistema  Monitorear operaciones

---

##  Navegación

### Sidebar (Izquierda)
- Logo Medicare con corazón
- Título y subtítulo
- Menú de navegación según rol
- Botón "Salir"

### Topbar (Superior)
- Título de la página actual
- Avatar del usuario
- Nombre completo
- Rol (badge)

---

##  Características Visuales

- **Animaciones:** Transiciones suaves en hover
- **Sombras:** Cards con depth visual
- **Gradientes:** Hero cards llamativos
- **Responsive:** Adaptable a todos los dispositivos
- **Iconos:** Emojis para mejor UX
- **Tipografía:** Inter font (moderna y legible)
- **Espaciado:** Generoso para facilitar lectura

---

**¡Sistema completamente diseñado y funcional!** 
