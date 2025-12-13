#!/usr/bin/env python3
"""
Script para arreglar columna servicio en tabla citas
"""
import sqlite3

def fix_servicio():
    conn = sqlite3.connect('database/medicare.db')
    c = conn.cursor()
    
    try:
        print("Creando nueva tabla citas sin restricción NOT NULL en servicio...")
        
        # Crear nueva tabla sin la restricción
        c.execute('''
            CREATE TABLE IF NOT EXISTS citas_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER NOT NULL,
                doctor_id INTEGER NOT NULL,
                servicio TEXT,
                especialidad TEXT,
                fecha DATE NOT NULL,
                hora TIME NOT NULL,
                motivo TEXT,
                estado TEXT DEFAULT 'confirmada',
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (paciente_id) REFERENCES usuarios (id),
                FOREIGN KEY (doctor_id) REFERENCES usuarios (id)
            )
        ''')
        
        # Copiar datos
        c.execute('''
            INSERT INTO citas_new 
            SELECT id, paciente_id, doctor_id, servicio, especialidad, fecha, hora, motivo, estado, fecha_creacion
            FROM citas
        ''')
        
        # Eliminar tabla vieja
        c.execute('DROP TABLE citas')
        
        # Renombrar nueva tabla
        c.execute('ALTER TABLE citas_new RENAME TO citas')
        
        conn.commit()
        print(" Tabla citas arreglada exitosamente")
        
    except Exception as e:
        print(f" Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    fix_servicio()
