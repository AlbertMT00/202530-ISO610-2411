#  Instalación Rápida - Sistema Medicare

## Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## Instalación en 3 Pasos

### 1⃣ Instalar dependencias
```bash
pip install flask werkzeug
```

### 2⃣ Navegar a la carpeta
```bash
cd medicare
```

### 3⃣ Iniciar el servidor
```bash
python app.py
```

¡Listo! Abre tu navegador en: **http://localhost:5000**

---

##  Inicio Rápido con Script

### Linux/Mac:
```bash
chmod +x start.sh
./start.sh
```

### Windows:
```bash
python app.py
```

---

##  Usuarios de Prueba

### Administrador
```
Usuario: admin
Contraseña: admin123
```

### Doctor
```
Usuario: drmartinez
Contraseña: doctor123
```

### Paciente
```
Usuario: mariagonzalez
Contraseña: paciente123
```

---

##  Estructura de Archivos

```
medicare/
 app.py               Aplicación principal
 start.sh             Script de inicio
 README.md            Documentación completa
 CAMBIOS.md           Resumen de cambios
 database/            Base de datos SQLite
 static/              CSS y JavaScript
 templates/           Páginas HTML
```

---

##  Solución de Problemas

### Error: "No module named 'flask'"
```bash
pip install flask werkzeug
```

### Error: "Port 5000 already in use"
Cambia el puerto en `app.py` (última línea):
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Cambia 5000 a 5001
```

### La base de datos no se crea
Asegúrate de que la carpeta `database/` tenga permisos de escritura:
```bash
mkdir -p database
chmod 755 database
```

---

##  Más Información

- **README.md** - Documentación completa del sistema
- **CAMBIOS.md** - Lista detallada de todas las funcionalidades
- **app.py** - Código fuente comentado

---

##  Soporte

¿Necesitas ayuda? Revisa:
1. README.md para documentación detallada
2. CAMBIOS.md para ver todas las funcionalidades
3. Los comentarios en app.py para entender el código

---

**¡Disfruta del Sistema Medicare!** 
