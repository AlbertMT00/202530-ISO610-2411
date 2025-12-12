#!/usr/bin/env python3
"""
Script de migración: Agregar columna especialidad a tabla citas
"""
import sqlite3

def migrate():
    conn = sqlite3.connect('database/medicare.db')
    c = conn.cursor()
    
    try:
        # Verificar si la columna ya existe
        columns = c.execute('PRAGMA table_info(citas)').fetchall()
        column_names = [col[1] for col in columns]
        
        if 'especialidad' not in column_names:
            print("Agregando columna 'especialidad' a tabla citas...")
            c.execute('ALTER TABLE citas ADD COLUMN especialidad TEXT')
            conn.commit()
            print(" Columna agregada exitosamente")
        else:
            print(" La columna 'especialidad' ya existe")
            
    except Exception as e:
        print(f" Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    migrate()
