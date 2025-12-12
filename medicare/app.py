from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from datetime import datetime, timedelta
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = 'medicare_secret_key_2024'
DATABASE = 'database/medicare.db'

# ESPECIALIDADES MÉDICAS - Lista centralizada
ESPECIALIDADES = [
    'Alergología',
    'Anestesiología',
    'Cardiología',
    'Cirugía General',
    'Cirugía Plástica',
    'Dermatología',
    'Endocrinología',
    'Gastroenterología',
    'Geriatría',
    'Ginecología',
    'Hematología',
    'Infectología',
    'Medicina General',
    'Medicina Interna',
    'Nefrología',
    'Neumología',
    'Neurología',
    'Nutrición',
    'Obstetricia',
    'Oftalmología',
    'Oncología',
    'Ortopedia',
    'Otorrinolaringología',
    'Pediatría',
    'Psiquiatría',
    'Radiología',
    'Reumatología',
    'Traumatología',
    'Urología'
]

# Decorador para requerir login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Decorador para requerir rol específico
def role_required(roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('index'))
            if session.get('role') not in roles:
                flash('No tienes permiso para acceder a esta página', 'error')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Inicializar base de datos
def init_db():
    # Si la base de datos existe con estructura antigua, intentar migrar
    if os.path.exists(DATABASE):
        try:
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            
            # Obtener columnas existentes
            c.execute("PRAGMA table_info(usuarios)")
            columnas = [col[1] for col in c.fetchall()]
            
            # Lista de migraciones necesarias
            migraciones = [
                ('cedula', "ALTER TABLE usuarios ADD COLUMN cedula TEXT UNIQUE"),
                ('foto_perfil', "ALTER TABLE usuarios ADD COLUMN foto_perfil TEXT DEFAULT 'default.png'"),
                ('estado_doctor', "ALTER TABLE usuarios ADD COLUMN estado_doctor TEXT DEFAULT 'disponible'"),
                ('hora_inicio', "ALTER TABLE usuarios ADD COLUMN hora_inicio TEXT DEFAULT '08:00'"),
                ('hora_fin', "ALTER TABLE usuarios ADD COLUMN hora_fin TEXT DEFAULT '17:00'")
            ]
            
            # Aplicar cada migración si la columna no existe
            for columna, sql in migraciones:
                if columna not in columnas:
                    try:
                        c.execute(sql)
                        conn.commit()
                        print(f" Migración aplicada: Campo '{columna}' agregado")
                    except sqlite3.OperationalError:
                        pass
            
            conn.close()
        except Exception as e:
            print(f" Error al migrar: {e}")
            print(" Ejecuta 'python migrate_db.py' para migración manual")
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    # Tabla de usuarios (doctores, pacientes, admin)
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('admin', 'doctor', 'paciente')),
        especialidad TEXT,
        telefono TEXT,
        cedula TEXT UNIQUE,
        foto_perfil TEXT DEFAULT 'default.png',
        fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        estado TEXT DEFAULT 'activo' CHECK(estado IN ('activo', 'inactivo')),
        estado_doctor TEXT DEFAULT 'disponible' CHECK(estado_doctor IN ('disponible', 'ocupado', 'descanso', 'fuera_servicio')),
        hora_inicio TEXT DEFAULT '08:00',
        hora_fin TEXT DEFAULT '17:00'
    )''')
    
    # Tabla de citas
    c.execute('''CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER NOT NULL,
        doctor_id INTEGER NOT NULL,
        especialidad TEXT NOT NULL,
        fecha DATE NOT NULL,
        hora TIME NOT NULL,
        motivo TEXT,
        estado TEXT DEFAULT 'confirmada' CHECK(estado IN ('confirmada', 'completada', 'cancelada')),
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (paciente_id) REFERENCES usuarios(id),
        FOREIGN KEY (doctor_id) REFERENCES usuarios(id),
        UNIQUE(doctor_id, fecha, hora)
    )''')
    
    # Tabla de recetas
    c.execute('''CREATE TABLE IF NOT EXISTS recetas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER NOT NULL,
        doctor_id INTEGER NOT NULL,
        medicamento TEXT NOT NULL,
        dosis TEXT NOT NULL,
        frecuencia TEXT NOT NULL,
        duracion TEXT NOT NULL,
        indicaciones TEXT,
        fecha_emision TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (paciente_id) REFERENCES usuarios(id),
        FOREIGN KEY (doctor_id) REFERENCES usuarios(id)
    )''')
    
    # Tabla de urgencias
    c.execute('''CREATE TABLE IF NOT EXISTS urgencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER NOT NULL,
        doctor_id INTEGER,
        descripcion TEXT NOT NULL,
        prioridad TEXT DEFAULT 'media' CHECK(prioridad IN ('baja', 'media', 'alta', 'critica')),
        estado TEXT DEFAULT 'pendiente' CHECK(estado IN ('pendiente', 'en_atencion', 'resuelta')),
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        fecha_resolucion TIMESTAMP,
        FOREIGN KEY (paciente_id) REFERENCES usuarios(id),
        FOREIGN KEY (doctor_id) REFERENCES usuarios(id)
    )''')
    
    # Crear usuario admin por defecto (solo si no existe)
    c.execute("SELECT COUNT(*) FROM usuarios WHERE username = 'admin'")
    if c.fetchone()[0] == 0:
        try:
            admin_password = generate_password_hash('admin123')
            c.execute('''INSERT INTO usuarios (nombre, email, username, password, role, cedula)
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      ('Administrador', 'admin@medicare.com', 'admin', admin_password, 'admin', '001-0000000-1'))
            
            # Crear un doctor por cada especialidad
            doctor_password = generate_password_hash('doctor123')
            especialidades = [
                ('Dr. Carlos Martínez', 'cardiologia@medicare.com', 'drcardiologia', 'Cardiología', '809-555-0101', '001-1234567-8'),
                ('Dra. Ana Castillo', 'pediatria@medicare.com', 'drpediatria', 'Pediatría', '809-555-0102', '001-2345678-9'),
                ('Dr. Roberto López', 'traumatologia@medicare.com', 'drtraumatologia', 'Traumatología', '809-555-0103', '001-3456789-0'),
                ('Dra. Patricia González', 'neurologia@medicare.com', 'drneurologia', 'Neurología', '809-555-0104', '001-4567890-1'),
                ('Dr. Miguel Pérez', 'endocrinologia@medicare.com', 'drendocrinologia', 'Endocrinología', '809-555-0105', '001-5678901-2'),
                ('Dra. Laura Ramírez', 'medicinainterna@medicare.com', 'drmedicinainterna', 'Medicina Interna', '809-555-0106', '001-6789012-3'),
                ('Dr. José Herrera', 'ginecologia@medicare.com', 'drginecologia', 'Ginecología', '809-555-0107', '001-7890123-4'),
                ('Dra. Carmen Santos', 'dermatologia@medicare.com', 'drdermatologia', 'Dermatología', '809-555-0108', '001-8901234-5'),
                ('Dr. Francisco Ortiz', 'oftalmologia@medicare.com', 'droftalmologia', 'Oftalmología', '809-555-0109', '001-9012345-6'),
                ('Dra. Elena Navarro', 'psiquiatria@medicare.com', 'drpsiquiatria', 'Psiquiatría', '809-555-0110', '001-0123456-7')
            ]
            
            for nombre, email, username, especialidad, telefono, cedula in especialidades:
                c.execute('''INSERT INTO usuarios (nombre, email, username, password, role, especialidad, telefono, cedula)
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                          (nombre, email, username, doctor_password, 'doctor', especialidad, telefono, cedula))
            
            # Crear pacientes de ejemplo
            paciente_password = generate_password_hash('paciente123')
            pacientes = [
                ('María González', 'maria@correo.com', 'mariagonzalez', '809-555-0201', '001-1111111-1'),
                ('Carlos Pérez', 'carlos@correo.com', 'carlosperez', '809-555-0202', '001-2222222-2'),
                ('Ana López', 'ana@correo.com', 'analopez', '809-555-0203', '001-3333333-3')
            ]
            
            for nombre, email, username, telefono, cedula in pacientes:
                c.execute('''INSERT INTO usuarios (nombre, email, username, password, role, telefono, cedula)
                             VALUES (?, ?, ?, ?, ?, ?, ?)''',
                          (nombre, email, username, paciente_password, 'paciente', telefono, cedula))
        except sqlite3.IntegrityError:
            pass  # Los usuarios ya existen
    
    conn.commit()
    conn.close()

# Función helper para obtener conexión
def get_db():
    conn = sqlite3.connect(DATABASE, timeout=30, check_same_thread=False, isolation_level=None)
    conn.row_factory = sqlite3.Row
    # Habilitar WAL mode para mejor concurrencia
    conn.execute('PRAGMA journal_mode=WAL')
    # Reducir tiempo de bloqueo
    conn.execute('PRAGMA busy_timeout=30000')
    return conn

# Rutas de autenticación
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db()
        user = conn.execute('SELECT * FROM usuarios WHERE username = ? AND estado = "activo"', (username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['nombre'] = user['nombre']
            session['role'] = user['role']
            session['especialidad'] = user['especialidad']
            if user['role'] == 'doctor':
                session['estado_doctor'] = user['estado_doctor'] or 'disponible'
                session['hora_inicio'] = user['hora_inicio'] or '08:00'
                session['hora_fin'] = user['hora_fin'] or '17:00'
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        telefono = request.form.get('telefono', '')
        cedula = request.form.get('cedula', '')
        
        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'error')
            return render_template('register.html')
        
        # Validar formato de cédula (001-0000000-0)
        if cedula and not validate_cedula(cedula):
            flash('Formato de cédula inválido. Use: 001-0000000-0', 'error')
            return render_template('register.html')
        
        try:
            conn = get_db()
            hashed_password = generate_password_hash(password)
            conn.execute('''INSERT INTO usuarios (nombre, email, username, password, role, telefono, cedula)
                           VALUES (?, ?, ?, ?, ?, ?, ?)''',
                        (nombre, email, username, hashed_password, 'paciente', telefono, cedula))
            conn.commit()
            conn.close()
            flash('Registro exitoso. Por favor inicia sesión', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError as e:
            if 'cedula' in str(e):
                flash('Esta cédula ya está registrada', 'error')
            else:
                flash('El usuario o email ya existe', 'error')
    
    return render_template('register.html')

def validate_cedula(cedula):
    """Valida formato de cédula dominicana: 001-0000000-0"""
    import re
    pattern = r'^\d{3}-\d{7}-\d{1}$'
    return bool(re.match(pattern, cedula))

@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada exitosamente', 'success')
    return redirect(url_for('index'))

# Dashboard según rol
@app.route('/dashboard')
@login_required
def dashboard():
    role = session.get('role')
    
    if role == 'admin':
        return render_template('admin_dashboard.html')
    elif role == 'doctor':
        return render_template('doctor_dashboard.html')
    else:
        return render_template('paciente_dashboard.html')

# Rutas de administración
@app.route('/admin/usuarios')
@role_required(['admin'])
def admin_usuarios():
    conn = get_db()
    usuarios = conn.execute('SELECT * FROM usuarios ORDER BY fecha_registro DESC').fetchall()
    conn.close()
    return render_template('admin_usuarios.html', usuarios=usuarios)

@app.route('/admin/agregar-doctor', methods=['GET', 'POST'])
@role_required(['admin'])
def agregar_doctor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        
        try:
            conn = get_db()
            hashed_password = generate_password_hash(password)
            conn.execute('''INSERT INTO usuarios (nombre, email, username, password, role, especialidad, telefono)
                           VALUES (?, ?, ?, ?, ?, ?, ?)''',
                        (nombre, email, username, hashed_password, 'doctor', especialidad, telefono))
            conn.commit()
            conn.close()
            flash('Doctor agregado exitosamente', 'success')
            return redirect(url_for('admin_usuarios'))
        except sqlite3.IntegrityError:
            flash('El usuario o email ya existe', 'error')
    
    return render_template('admin_agregar_doctor.html', especialidades=ESPECIALIDADES)

@app.route('/admin/usuarios/eliminar/<int:id>', methods=['POST'])
@role_required(['admin'])
def eliminar_usuario(id):
    conn = get_db()
    
    # Verificar que no sea el admin principal
    usuario = conn.execute('SELECT username FROM usuarios WHERE id = ?', (id,)).fetchone()
    
    if usuario and usuario['username'] == 'admin':
        flash('No se puede eliminar el usuario administrador principal', 'error')
        conn.close()
        return redirect(url_for('admin_usuarios'))
    
    try:
        # Eliminar citas relacionadas
        conn.execute('DELETE FROM citas WHERE paciente_id = ? OR doctor_id = ?', (id, id))
        
        # Eliminar recetas relacionadas
        conn.execute('DELETE FROM recetas WHERE paciente_id = ? OR doctor_id = ?', (id, id))
        
        # Eliminar urgencias relacionadas
        conn.execute('DELETE FROM urgencias WHERE paciente_id = ?', (id,))
        
        # Eliminar usuario
        conn.execute('DELETE FROM usuarios WHERE id = ?', (id,))
        conn.commit()
        
        flash('Usuario eliminado exitosamente', 'success')
    except Exception as e:
        flash(f'Error al eliminar usuario: {str(e)}', 'error')
    finally:
        conn.close()
    
    return redirect(url_for('admin_usuarios'))

# Rutas de citas
@app.route('/citas')
@login_required
def citas():
    from datetime import datetime
    fecha_hoy = datetime.now().strftime('%Y-%m-%d')
    
    conn = get_db()
    role = session.get('role')
    user_id = session.get('user_id')
    
    if role == 'doctor':
        # Ver todas las citas del doctor
        citas = conn.execute('''
            SELECT c.*, p.nombre as paciente_nombre, d.nombre as doctor_nombre
            FROM citas c
            JOIN usuarios p ON c.paciente_id = p.id
            JOIN usuarios d ON c.doctor_id = d.id
            WHERE c.doctor_id = ?
            ORDER BY c.fecha DESC, c.hora DESC
        ''', (user_id,)).fetchall()
        
        # Obtener lista de pacientes para el formulario (incluye al doctor mismo)
        pacientes = conn.execute('SELECT id, nombre FROM usuarios WHERE role = "paciente" AND estado = "activo"').fetchall()
        
        # Agregar doctores a la lista (para que puedan agendar para sí mismos)
        doctores_como_pacientes = conn.execute('SELECT id, nombre FROM usuarios WHERE role = "doctor" AND estado = "activo"').fetchall()
        pacientes = list(pacientes) + list(doctores_como_pacientes)
    else:
        # Ver solo las citas del paciente
        citas = conn.execute('''
            SELECT c.*, p.nombre as paciente_nombre, d.nombre as doctor_nombre
            FROM citas c
            JOIN usuarios p ON c.paciente_id = p.id
            JOIN usuarios d ON c.doctor_id = d.id
            WHERE c.paciente_id = ?
            ORDER BY c.fecha DESC, c.hora DESC
        ''', (user_id,)).fetchall()
        pacientes = []
    
    # Obtener lista de doctores
    doctores = conn.execute('SELECT id, nombre, especialidad FROM usuarios WHERE role = "doctor" AND estado = "activo"').fetchall()
    
    # Obtener especialidades que tienen doctores
    especialidades_con_doctores = conn.execute('''
        SELECT DISTINCT especialidad FROM usuarios 
        WHERE role = "doctor" AND estado = "activo"
        ORDER BY especialidad
    ''').fetchall()
    especialidades_activas = [e['especialidad'] for e in especialidades_con_doctores]
    
    conn.close()
    
    return render_template('citas.html', citas=citas, pacientes=pacientes, doctores=doctores, fecha_hoy=fecha_hoy, especialidades=especialidades_activas)


@app.route('/citas/crear', methods=['POST'])
@login_required
def crear_cita():
    role = session.get('role')
    user_id = session.get('user_id')
    conn = None
    
    try:
        if role == 'doctor':
            paciente_id = request.form.get('paciente_id')
            if not paciente_id:
                flash('Debe seleccionar un paciente', 'error')
                return redirect(url_for('citas'))
        else:
            paciente_id = user_id
        
        doctor_id = request.form['doctor_id']
        especialidad = request.form['especialidad']
        fecha = request.form['fecha']
        hora = request.form['hora']
        motivo = request.form.get('motivo', '')
        
        conn = get_db()
        
        # Obtener horario laboral del doctor
        doctor = conn.execute('''
            SELECT hora_inicio, hora_fin FROM usuarios 
            WHERE id = ? AND role = 'doctor'
        ''', (doctor_id,)).fetchone()
        
        # Validar que la hora esté dentro del horario laboral
        if doctor:
            hora_inicio = doctor['hora_inicio'] or '08:00'
            hora_fin = doctor['hora_fin'] or '17:00'
            
            if not (hora_inicio <= hora <= hora_fin):
                flash(f'La hora seleccionada está fuera del horario laboral del doctor ({hora_inicio} - {hora_fin})', 'error')
                return redirect(url_for('citas'))
        
        # Validar que el horario no esté ocupado (reserva de 1 hora)
        from datetime import datetime, timedelta
        
        # Convertir hora a datetime para calcular el rango
        try:
            hora_inicio_cita = datetime.strptime(hora, '%H:%M')
            hora_fin_cita = (hora_inicio_cita + timedelta(hours=1)).strftime('%H:%M')
        except:
            hora_fin_cita = hora
        
        # Verificar si ya existe una cita en ese horario exacto (del doctor)
        cita_exacta = conn.execute('''
            SELECT * FROM citas 
            WHERE doctor_id = ? AND fecha = ? AND hora = ? AND estado != 'cancelada'
        ''', (doctor_id, fecha, hora)).fetchone()
        
        if cita_exacta:
            flash('El doctor tiene citas ya programadas en este horario. Por favor selecciona otra hora.', 'error')
            return redirect(url_for('citas'))
        
        # Verificar si el paciente ya tiene una cita a la misma hora (con cualquier doctor)
        cita_paciente = conn.execute('''
            SELECT * FROM citas 
            WHERE paciente_id = ? AND fecha = ? AND hora = ? AND estado != 'cancelada'
        ''', (paciente_id, fecha, hora)).fetchone()
        
        if cita_paciente:
            flash('Ya tienes una cita programada a esta hora. Por favor selecciona otra hora.', 'error')
            return redirect(url_for('citas'))
        
        conn.execute('''INSERT INTO citas (paciente_id, doctor_id, especialidad, fecha, hora, motivo)
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (paciente_id, doctor_id, especialidad, fecha, hora, motivo))
        conn.commit()
        flash('Cita creada exitosamente', 'success')
        
    except Exception as e:
        if conn:
            conn.rollback()
        flash(f'Error al crear la cita: {str(e)}', 'error')
    finally:
        if conn:
            conn.close()
    
    return redirect(url_for('citas'))

@app.route('/citas/<int:id>/cancelar', methods=['POST'])
@login_required
def cancelar_cita(id):
    try:
        conn = get_db()
        conn.execute('UPDATE citas SET estado = ? WHERE id = ?', ('cancelada', id))
        conn.commit()
        conn.close()
        flash('Cita cancelada exitosamente', 'success')
    except Exception as e:
        flash(f'Error al cancelar la cita: {str(e)}', 'error')
    
    return redirect(url_for('citas'))

@app.route('/citas/<int:id>/completar', methods=['POST'])
@role_required(['doctor'])
def completar_cita(id):
    try:
        conn = get_db()
        conn.execute('UPDATE citas SET estado = ? WHERE id = ?', ('completada', id))
        conn.commit()
        conn.close()
        flash('Cita marcada como completada', 'success')
    except Exception as e:
        flash(f'Error al completar la cita: {str(e)}', 'error')
    
    return redirect(url_for('citas'))

@app.route('/citas/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_cita(id):
    conn = get_db()
    
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora = request.form['hora']
        motivo = request.form.get('motivo', '')
        
        try:
            conn.execute('''UPDATE citas 
                           SET fecha = ?, hora = ?, motivo = ?
                           WHERE id = ?''',
                        (fecha, hora, motivo, id))
            conn.commit()
            conn.close()
            flash('Cita actualizada exitosamente', 'success')
            return redirect(url_for('citas'))
        except Exception as e:
            flash(f'Error al actualizar la cita: {str(e)}', 'error')
    
    cita = conn.execute('SELECT * FROM citas WHERE id = ?', (id,)).fetchone()
    doctores = conn.execute('SELECT id, nombre, especialidad FROM usuarios WHERE role = "doctor" AND estado = "activo"').fetchall()
    conn.close()
    
    return render_template('editar_cita.html', cita=cita, doctores=doctores)

# Rutas de recetas
@app.route('/recetas')
@login_required
def recetas():
    conn = get_db()
    role = session.get('role')
    user_id = session.get('user_id')
    
    if role == 'doctor':
        # Ver todas las recetas del doctor
        recetas = conn.execute('''
            SELECT r.*, p.nombre as paciente_nombre, d.nombre as doctor_nombre
            FROM recetas r
            JOIN usuarios p ON r.paciente_id = p.id
            JOIN usuarios d ON r.doctor_id = d.id
            WHERE r.doctor_id = ?
            ORDER BY r.fecha_emision DESC
        ''', (user_id,)).fetchall()
        
        # Obtener lista de pacientes (incluye doctores para que puedan recetarse)
        pacientes = conn.execute('SELECT id, nombre FROM usuarios WHERE role = "paciente"').fetchall()
        
        # Agregar doctores a la lista
        doctores_como_pacientes = conn.execute('SELECT id, nombre FROM usuarios WHERE role = "doctor"').fetchall()
        pacientes = list(pacientes) + list(doctores_como_pacientes)
    else:
        # Ver solo las recetas del paciente
        recetas = conn.execute('''
            SELECT r.*, p.nombre as paciente_nombre, d.nombre as doctor_nombre
            FROM recetas r
            JOIN usuarios p ON r.paciente_id = p.id
            JOIN usuarios d ON r.doctor_id = d.id
            WHERE r.paciente_id = ?
            ORDER BY r.fecha_emision DESC
        ''', (user_id,)).fetchall()
        pacientes = []
    
    conn.close()
    
    return render_template('recetas.html', recetas=recetas, pacientes=pacientes)

@app.route('/recetas/crear', methods=['POST'])
@role_required(['doctor'])
def crear_receta():
    paciente_id = request.form['paciente_id']
    doctor_id = session.get('user_id')
    medicamento = request.form['medicamento']
    dosis = request.form['dosis']
    frecuencia = request.form['frecuencia']
    duracion = request.form['duracion']
    indicaciones = request.form.get('indicaciones', '')
    
    try:
        conn = get_db()
        conn.execute('''INSERT INTO recetas (paciente_id, doctor_id, medicamento, dosis, frecuencia, duracion, indicaciones)
                       VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (paciente_id, doctor_id, medicamento, dosis, frecuencia, duracion, indicaciones))
        conn.commit()
        conn.close()
        flash('Receta creada exitosamente', 'success')
    except Exception as e:
        flash(f'Error al crear la receta: {str(e)}', 'error')
    
    return redirect(url_for('recetas'))

@app.route('/recetas/<int:id>/editar', methods=['GET', 'POST'])
@role_required(['doctor'])
def editar_receta(id):
    conn = get_db()
    
    if request.method == 'POST':
        medicamento = request.form['medicamento']
        dosis = request.form['dosis']
        frecuencia = request.form['frecuencia']
        duracion = request.form['duracion']
        indicaciones = request.form.get('indicaciones', '')
        
        try:
            conn.execute('''UPDATE recetas 
                           SET medicamento = ?, dosis = ?, frecuencia = ?, duracion = ?, indicaciones = ?
                           WHERE id = ?''',
                        (medicamento, dosis, frecuencia, duracion, indicaciones, id))
            conn.commit()
            flash('Receta actualizada exitosamente', 'success')
            return redirect(url_for('recetas'))
        except Exception as e:
            flash(f'Error al actualizar la receta: {str(e)}', 'error')
    
    # GET - mostrar formulario
    receta = conn.execute('''
        SELECT r.*, 
               p.nombre as paciente_nombre
        FROM recetas r
        JOIN usuarios p ON r.paciente_id = p.id
        WHERE r.id = ?
    ''', (id,)).fetchone()
    
    if not receta:
        flash('Receta no encontrada', 'error')
        return redirect(url_for('recetas'))
    
    # Obtener lista de pacientes y doctores para el formulario
    pacientes = conn.execute('SELECT id, nombre FROM usuarios WHERE role = "paciente"').fetchall()
    doctores_como_pacientes = conn.execute('SELECT id, nombre FROM usuarios WHERE role = "doctor"').fetchall()
    pacientes = list(pacientes) + list(doctores_como_pacientes)
    
    conn.close()
    return render_template('editar_receta.html', receta=receta, pacientes=pacientes)

@app.route('/recetas/<int:id>/eliminar', methods=['POST'])
@role_required(['doctor'])
def eliminar_receta(id):
    try:
        conn = get_db()
        conn.execute('DELETE FROM recetas WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        flash('Receta eliminada exitosamente', 'success')
    except Exception as e:
        flash(f'Error al eliminar la receta: {str(e)}', 'error')
    
    return redirect(url_for('recetas'))

# Rutas de doctores
@app.route('/doctores')
@login_required
def doctores():
    conn = get_db()
    doctores = conn.execute('''
        SELECT id, nombre, especialidad, telefono, email, estado_doctor, hora_inicio, hora_fin
        FROM usuarios 
        WHERE role = "doctor" AND estado = "activo"
        ORDER BY especialidad, nombre
    ''').fetchall()
    
    # Obtener especialidades que tienen doctores
    especialidades_con_doctores = conn.execute('''
        SELECT DISTINCT especialidad FROM usuarios 
        WHERE role = "doctor" AND estado = "activo"
        ORDER BY especialidad
    ''').fetchall()
    especialidades_activas = [e['especialidad'] for e in especialidades_con_doctores]
    
    conn.close()
    return render_template('doctores.html', doctores=doctores, especialidades=especialidades_activas)

# Rutas de urgencias
@app.route('/urgencias')
@login_required
def urgencias():
    conn = get_db()
    role = session.get('role')
    user_id = session.get('user_id')
    
    if role == 'doctor':
        # Ver todas las urgencias
        urgencias = conn.execute('''
            SELECT u.*, p.nombre as paciente_nombre, d.nombre as doctor_nombre
            FROM urgencias u
            JOIN usuarios p ON u.paciente_id = p.id
            LEFT JOIN usuarios d ON u.doctor_id = d.id
            ORDER BY 
                CASE u.prioridad
                    WHEN 'critica' THEN 1
                    WHEN 'alta' THEN 2
                    WHEN 'media' THEN 3
                    WHEN 'baja' THEN 4
                END,
                u.fecha_creacion DESC
        ''').fetchall()
    else:
        # Ver solo urgencias del paciente
        urgencias = conn.execute('''
            SELECT u.*, p.nombre as paciente_nombre, d.nombre as doctor_nombre
            FROM urgencias u
            JOIN usuarios p ON u.paciente_id = p.id
            LEFT JOIN usuarios d ON u.doctor_id = d.id
            WHERE u.paciente_id = ?
            ORDER BY u.fecha_creacion DESC
        ''', (user_id,)).fetchall()
    
    conn.close()
    return render_template('urgencias.html', urgencias=urgencias)

@app.route('/urgencias/crear', methods=['POST'])
@login_required
def crear_urgencia():
    paciente_id = session.get('user_id')
    descripcion = request.form['descripcion']
    prioridad = request.form.get('prioridad', 'media')
    
    try:
        conn = get_db()
        conn.execute('''INSERT INTO urgencias (paciente_id, descripcion, prioridad)
                       VALUES (?, ?, ?)''',
                    (paciente_id, descripcion, prioridad))
        conn.commit()
        conn.close()
        flash('Urgencia registrada exitosamente', 'success')
    except Exception as e:
        flash(f'Error al registrar la urgencia: {str(e)}', 'error')
    
    return redirect(url_for('urgencias'))

@app.route('/urgencias/<int:id>/atender', methods=['POST'])
@role_required(['doctor'])
def atender_urgencia(id):
    doctor_id = session.get('user_id')
    estado = request.form.get('estado', 'en_atencion')
    
    try:
        conn = get_db()
        if estado == 'resuelta':
            conn.execute('''UPDATE urgencias 
                           SET doctor_id = ?, estado = ?, fecha_resolucion = CURRENT_TIMESTAMP
                           WHERE id = ?''',
                        (doctor_id, estado, id))
        else:
            conn.execute('''UPDATE urgencias 
                           SET doctor_id = ?, estado = ?
                           WHERE id = ?''',
                        (doctor_id, estado, id))
        conn.commit()
        conn.close()
        flash('Urgencia actualizada exitosamente', 'success')
    except Exception as e:
        flash(f'Error al actualizar la urgencia: {str(e)}', 'error')
    
    return redirect(url_for('urgencias'))

@app.route('/urgencias/<int:id>/eliminar', methods=['POST'])
@role_required(['admin'])
def eliminar_urgencia(id):
    try:
        conn = get_db()
        conn.execute('DELETE FROM urgencias WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        flash('Urgencia eliminada exitosamente', 'success')
    except Exception as e:
        flash(f'Error al eliminar la urgencia: {str(e)}', 'error')
    
    return redirect(url_for('urgencias'))

# Rutas de Configuración de Perfil
@app.route('/configuracion')
@login_required
def configuracion():
    conn = get_db()
    usuario = conn.execute('SELECT * FROM usuarios WHERE id = ?', (session.get('user_id'),)).fetchone()
    conn.close()
    return render_template('configuracion.html', usuario=usuario)

@app.route('/configuracion/actualizar', methods=['POST'])
@login_required
def actualizar_perfil():
    user_id = session.get('user_id')
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    telefono = request.form.get('telefono')
    cedula = request.form.get('cedula')
    
    # Validar cédula si se proporciona
    if cedula and not validate_cedula(cedula):
        flash('Formato de cédula inválido. Use: 001-0000000-0', 'error')
        return redirect(url_for('configuracion'))
    
    try:
        conn = get_db()
        conn.execute('''UPDATE usuarios 
                       SET nombre = ?, email = ?, telefono = ?, cedula = ?
                       WHERE id = ?''',
                    (nombre, email, telefono, cedula, user_id))
        conn.commit()
        conn.close()
        
        # Actualizar sesión
        session['nombre'] = nombre
        
        flash('Perfil actualizado exitosamente', 'success')
    except sqlite3.IntegrityError as e:
        if 'email' in str(e):
            flash('Este email ya está registrado', 'error')
        elif 'cedula' in str(e):
            flash('Esta cédula ya está registrada', 'error')
    
    return redirect(url_for('configuracion'))

@app.route('/configuracion/cambiar-contrasena', methods=['POST'])
@login_required
def cambiar_contrasena():
    user_id = session.get('user_id')
    password_actual = request.form.get('password_actual')
    password_nueva = request.form.get('password_nueva')
    password_confirmar = request.form.get('password_confirmar')
    
    if password_nueva != password_confirmar:
        flash('Las contraseñas nuevas no coinciden', 'error')
        return redirect(url_for('configuracion'))
    
    # Verificar contraseña actual
    conn = get_db()
    usuario = conn.execute('SELECT password FROM usuarios WHERE id = ?', (user_id,)).fetchone()
    
    if not check_password_hash(usuario['password'], password_actual):
        flash('La contraseña actual es incorrecta', 'error')
        conn.close()
        return redirect(url_for('configuracion'))
    
    # Actualizar contraseña
    hashed_password = generate_password_hash(password_nueva)
    conn.execute('UPDATE usuarios SET password = ? WHERE id = ?', (hashed_password, user_id))
    conn.commit()
    conn.close()
    
    flash('Contraseña actualizada exitosamente', 'success')
    return redirect(url_for('configuracion'))

# API endpoints para datos dinámicos
@app.route('/api/stats')
@login_required
def api_stats():
    conn = get_db()
    role = session.get('role')
    user_id = session.get('user_id')
    
    stats = {}
    
    if role == 'doctor':
        # Estadísticas para doctor
        from datetime import datetime
        fecha_hoy = datetime.now().strftime('%Y-%m-%d')
        
        stats['citas_hoy'] = conn.execute('''
            SELECT COUNT(*) as count FROM citas 
            WHERE doctor_id = ? AND fecha = ? AND estado != 'cancelada'
        ''', (user_id, fecha_hoy)).fetchone()['count']
        
        stats['recetas_pendientes'] = conn.execute('''
            SELECT COUNT(*) as count FROM recetas 
            WHERE doctor_id = ? AND date(fecha_emision) >= date('now', '-30 days')
        ''', (user_id,)).fetchone()['count']
        
        stats['urgencias'] = conn.execute('''
            SELECT COUNT(*) as count FROM urgencias 
            WHERE estado IN ('pendiente', 'en_atencion')
        ''').fetchone()['count']
        
    elif role == 'paciente':
        # Estadísticas para paciente
        from datetime import datetime
        fecha_hoy = datetime.now().strftime('%Y-%m-%d')
        
        stats['proximas_citas'] = conn.execute('''
            SELECT COUNT(*) as count FROM citas 
            WHERE paciente_id = ? AND fecha >= ? AND estado = 'confirmada'
        ''', (user_id, fecha_hoy)).fetchone()['count']
        
        stats['citas_futuras'] = conn.execute('''
            SELECT COUNT(*) as count FROM citas 
            WHERE paciente_id = ? AND fecha > ? AND estado = 'confirmada'
        ''', (user_id, fecha_hoy)).fetchone()['count']
        
        stats['recetas_activas'] = conn.execute('''
            SELECT COUNT(*) as count FROM recetas 
            WHERE paciente_id = ?
        ''', (user_id,)).fetchone()['count']
    
    conn.close()
    return jsonify(stats)

@app.route('/api/horarios-disponibles')
@login_required
def horarios_disponibles():
    doctor_id = request.args.get('doctor_id')
    fecha = request.args.get('fecha')
    
    if not doctor_id or not fecha:
        return jsonify({'error': 'Faltan parámetros'}), 400
    
    conn = get_db()
    
    # Obtener horarios ocupados
    horarios_ocupados_raw = conn.execute('''
        SELECT hora FROM citas 
        WHERE doctor_id = ? AND fecha = ? AND estado != 'cancelada'
    ''', (doctor_id, fecha)).fetchall()
    
    # Obtener horario de trabajo del doctor
    doctor = conn.execute('''
        SELECT hora_inicio, hora_fin FROM usuarios 
        WHERE id = ? AND role = 'doctor'
    ''', (doctor_id,)).fetchone()
    
    conn.close()
    
    # Expandir horarios ocupados para incluir la hora completa (1 hora de duración)
    from datetime import datetime, timedelta
    ocupados = []
    for h in horarios_ocupados_raw:
        hora_str = h['hora']
        ocupados.append(hora_str)
    # Expandir horarios ocupados - solo la hora exacta de la cita
    from datetime import datetime, timedelta
    ocupados = []
    for h in horarios_ocupados_raw:
        hora_str = h['hora']
        # Solo agregar la hora exacta, no la siguiente
        # Si hay cita a las 08:00, solo bloquear 08:00 (08:00-09:00)
        # NO bloquear 09:00 (esa es otra cita diferente)
        ocupados.append(hora_str)
    
    # Eliminar duplicados
    ocupados = list(set(ocupados))
    
    return jsonify({
        'horarios_ocupados': ocupados,
        'hora_inicio': doctor['hora_inicio'] if doctor else '08:00',
        'hora_fin': doctor['hora_fin'] if doctor else '17:00'
    })

@app.route('/doctor/cambiar-estado', methods=['POST'])
@role_required(['doctor'])
def cambiar_estado_doctor():
    nuevo_estado = request.form.get('estado')
    user_id = session.get('user_id')
    
    estados_validos = ['disponible', 'ocupado', 'descanso', 'fuera_servicio']
    
    if nuevo_estado not in estados_validos:
        flash('Estado no válido', 'error')
        return redirect(url_for('dashboard'))
    
    try:
        conn = get_db()
        conn.execute('UPDATE usuarios SET estado_doctor = ? WHERE id = ?', 
                    (nuevo_estado, user_id))
        conn.commit()
        conn.close()
        
        # Actualizar en la sesión
        session['estado_doctor'] = nuevo_estado
        
        estados_textos = {
            'disponible': 'Disponible',
            'ocupado': 'Ocupado',
            'descanso': 'En descanso',
            'fuera_servicio': 'Fuera de servicio'
        }
        
        flash(f'Estado actualizado a: {estados_textos[nuevo_estado]}', 'success')
    except Exception as e:
        flash(f'Error al actualizar estado: {str(e)}', 'error')
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    os.makedirs('database', exist_ok=True)
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
