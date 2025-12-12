#!/usr/bin/env python3
"""
Script para agregar 8 doctores más con especialidades adicionales
"""
import sqlite3
from werkzeug.security import generate_password_hash

def agregar_mas_doctores():
    conn = sqlite3.connect('database/medicare.db')
    c = conn.cursor()
    
    # 8 doctores más con especialidades diferentes
    doctores_adicionales = [
        {
            'nombre': 'Dra. Gabriela Mendoza',
            'email': 'neurologia@medicare.com',
            'username': 'drneurologia2',
            'password': 'doctor123',
            'especialidad': 'Neurología',
            'telefono': '809-555-0120'
        },
        {
            'nombre': 'Dr. Héctor Ramírez',
            'email': 'traumatologia@medicare.com',
            'username': 'drtraumatologia2',
            'password': 'doctor123',
            'especialidad': 'Traumatología',
            'telefono': '809-555-0121'
        },
        {
            'nombre': 'Dra. Valeria Ortiz',
            'email': 'endocrinologia@medicare.com',
            'username': 'drendocrinologia2',
            'password': 'doctor123',
            'especialidad': 'Endocrinología',
            'telefono': '809-555-0122'
        },
        {
            'nombre': 'Dr. Rodrigo Jiménez',
            'email': 'medicinainterna@medicare.com',
            'username': 'drmedicinainterna2',
            'password': 'doctor123',
            'especialidad': 'Medicina Interna',
            'telefono': '809-555-0123'
        },
        {
            'nombre': 'Dra. Lucía Herrera',
            'email': 'ginecologia@medicare.com',
            'username': 'drginecologia2',
            'password': 'doctor123',
            'especialidad': 'Ginecología',
            'telefono': '809-555-0124'
        },
        {
            'nombre': 'Dr. Alberto Díaz',
            'email': 'dermatologia@medicare.com',
            'username': 'drdermatologia2',
            'password': 'doctor123',
            'especialidad': 'Dermatología',
            'telefono': '809-555-0125'
        },
        {
            'nombre': 'Dra. Natalia Cruz',
            'email': 'oftalmologia@medicare.com',
            'username': 'droftalmologia2',
            'password': 'doctor123',
            'especialidad': 'Oftalmología',
            'telefono': '809-555-0126'
        },
        {
            'nombre': 'Dr. Javier Moreno',
            'email': 'psiquiatria@medicare.com',
            'username': 'drpsiquiatria2',
            'password': 'doctor123',
            'especialidad': 'Psiquiatría',
            'telefono': '809-555-0127'
        }
    ]
    
    try:
        for doctor in doctores_adicionales:
            # Verificar si el usuario ya existe
            existe = c.execute('SELECT id FROM usuarios WHERE username = ?', 
                             (doctor['username'],)).fetchone()
            
            if existe:
                print(f"  Usuario {doctor['username']} ya existe, saltando...")
                continue
            
            # Hash de la contraseña
            password_hash = generate_password_hash(doctor['password'])
            
            # Insertar doctor
            c.execute('''
                INSERT INTO usuarios (nombre, email, username, password, role, especialidad, telefono, estado)
                VALUES (?, ?, ?, ?, 'doctor', ?, ?, 'activo')
            ''', (
                doctor['nombre'],
                doctor['email'],
                doctor['username'],
                password_hash,
                doctor['especialidad'],
                doctor['telefono']
            ))
            
            print(f" Doctor agregado: {doctor['nombre']} - {doctor['especialidad']}")
        
        conn.commit()
        print(f"\n ¡Doctores adicionales agregados exitosamente!")
        print("\n Resumen Final:")
        
        # Contar total de doctores
        total = c.execute('SELECT COUNT(*) FROM usuarios WHERE role = "doctor"').fetchone()[0]
        print(f"Total de doctores en el sistema: {total}")
        
        # Listar todas las especialidades con cantidad de doctores
        especialidades = c.execute('''
            SELECT especialidad, COUNT(*) as cantidad
            FROM usuarios 
            WHERE role = "doctor" 
            GROUP BY especialidad
            ORDER BY especialidad
        ''').fetchall()
        
        print(f"\n Especialidades disponibles ({len(especialidades)}):")
        for i, (esp, cant) in enumerate(especialidades, 1):
            print(f"{i:2d}. {esp:25s} ({cant} doctor{'es' if cant > 1 else ''})")
        
    except Exception as e:
        print(f" Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    print(" Agregando 8 doctores adicionales al sistema Medicare...")
    print("=" * 60)
    agregar_mas_doctores()
