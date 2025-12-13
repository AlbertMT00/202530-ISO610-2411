#  Solución de Problemas - Medicare

##  Error: "no such column: cedula"

### Causa del Error
Este error ocurre cuando tienes una base de datos antigua sin el campo `cedula` y el nuevo código intenta usar ese campo.

###  Solución Rápida

#### Opción 1: Usar el script de reseteo (Recomendado)

```bash
# 1. Detén el servidor (Ctrl+C si está corriendo)

# 2. Ejecuta el script de reseteo
python reset_db.py

# 3. Cuando te pregunte, escribe: s

# 4. Inicia la aplicación nuevamente
python app.py
```

#### Opción 2: Eliminar manualmente

```bash
# 1. Detén el servidor (Ctrl+C)

# 2. Elimina la base de datos antigua
# En Windows:
del database\medicare.db

# En Linux/Mac:
rm database/medicare.db

# 3. Inicia la aplicación (creará una nueva BD)
python app.py
```

#### Opción 3: Desde VS Code

1. Ve a la carpeta `database` en el explorador
2. Clic derecho en `medicare.db`
3. Selecciona "Delete" o "Eliminar"
4. Ejecuta `python app.py` en la terminal

---

##  ¿Qué Hace el Reset?

-  **Elimina** la base de datos antigua
-  **Crea** una nueva con la estructura actualizada
-  **Genera** los 10 doctores (uno por especialidad)
-  **Crea** usuarios de prueba con cédulas
-  **Agrega** campos nuevos (cedula, foto_perfil)

---

##  Importante

**Nota:** Al resetear la base de datos:
- Se perderán todas las citas existentes
- Se perderán todas las recetas
- Se perderán todos los usuarios creados
- Se crearán los usuarios de prueba por defecto

**Si tienes datos importantes:**
1. Haz backup de `database/medicare.db` antes de eliminar
2. O usa las migraciones en producción (no en desarrollo)

---

##  Usuarios Después del Reset

### Admin
```
Usuario: admin
Contraseña: admin123
Cédula: 001-0000000-1
```

### Doctores (10 total)
```
Usuario: drcardiologia
Contraseña: doctor123
Cédula: 001-1234567-8
```

### Pacientes
```
Usuario: mariagonzalez
Contraseña: paciente123
Cédula: 001-1111111-1
```

---

##  Otros Errores Comunes

### Error: "Port 5000 already in use"

**Solución:**
```python
# Cambia el puerto en app.py (última línea)
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Error: "No module named 'flask'"

**Solución:**
```bash
pip install flask werkzeug
```

### Error: "Permission denied" al eliminar BD

**Solución:**
1. Cierra VS Code completamente
2. Elimina el archivo manualmente desde el explorador de Windows
3. Vuelve a abrir VS Code

---

##  Verificar que Funciona

Después del reset, verifica:

1. **Inicia la aplicación**
   ```bash
   python app.py
   ```

2. **Deberías ver:**
   ```
   * Running on http://127.0.0.1:5000
   ```

3. **Abre el navegador:**
   ```
   http://localhost:5000
   ```

4. **Inicia sesión:**
   - Usuario: `admin`
   - Contraseña: `admin123`

5. **Si entras al dashboard  ¡Todo funciona! **

---

##  ¿Aún Tienes Problemas?

Revisa:
1. Que Python esté instalado: `python --version`
2. Que Flask esté instalado: `pip show flask`
3. Que estés en la carpeta correcta: `cd medicare`
4. Que no haya otro proceso usando el puerto 5000

---

**¡Con esto debería funcionar perfectamente!** 
