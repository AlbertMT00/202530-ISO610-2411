#!/usr/bin/env python3
"""
Script para agregar la columna 'cedula' a la tabla usuarios
"""
import sqlite3
import os

# Obtener ruta de la base de datos
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database', 'medicare.db')

def agregar_columna_cedula():
    """Agregar columna cedula a la tabla usuarios"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Verificar si la columna ya existe
        cursor.execute("PRAGMA table_info(usuarios)")
        columnas = [col[1] for col in cursor.fetchall()]
        
        if 'cedula' in columnas:
            print("La columna 'cedula' ya existe en la tabla usuarios")
            conn.close()
            return
        
        # Agregar columna cedula
        print("Agregando columna 'cedula' a la tabla usuarios...")
        cursor.execute('''
            ALTER TABLE usuarios 
            ADD COLUMN cedula TEXT
        ''')
        
        conn.commit()
        print("Columna 'cedula' agregada exitosamente")
        
        # Verificar que se agregó correctamente
        cursor.execute("PRAGMA table_info(usuarios)")
        columnas = cursor.fetchall()
        print("\nColumnas actuales en la tabla usuarios:")
        for col in columnas:
            print(f"  - {col[1]} ({col[2]})")
        
        conn.close()
        print("\nMigracion completada exitosamente")
        
    except Exception as e:
        print(f"Error al agregar columna cedula: {e}")
        if conn:
            conn.rollback()
            conn.close()

if __name__ == '__main__':
    agregar_columna_cedula()
