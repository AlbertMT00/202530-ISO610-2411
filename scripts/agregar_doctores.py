#!/usr/bin/env python3
"""
Script para agregar 9 doctores adicionales al sistema Medicare
"""
import sqlite3
from werkzeug.security import generate_password_hash

def agregar_doctores():
    conn = sqlite3.connect('database/medicare.db')
    c = conn.cursor()
    
    # Lista de 9 nuevos doctores con especialidades diferentes
    nuevos_doctores = [
        {
            'nombre': 'Dr. Luis Fernández',
            'email': 'urologia@medicare.com',
            'username': 'drurologia',
            'password': 'doctor123',
            'especialidad': 'Urología',
            'telefono': '809-555-0111'
        },
        {
            'nombre': 'Dra. Sofía Martínez',
            'email': 'gastroenterologia@medicare.com',
            'username': 'drgastroenterologia',
            'password': 'doctor123',
            'especialidad': 'Gastroenterología',
            'telefono': '809-555-0112'
        },
        {
            'nombre': 'Dr. Ricardo Vega',
            'email': 'neumologia@medicare.com',
            'username': 'drneumologia',
            'password': 'doctor123',
            'especialidad': 'Neumología',
            'telefono': '809-555-0113'
        },
        {
            'nombre': 'Dra. Isabel Romero',
            'email': 'oncologia@medicare.com',
            'username': 'droncologia',
            'password': 'doctor123',
            'especialidad': 'Oncología',
            'telefono': '809-555-0114'
        },
        {
            'nombre': 'Dr. Manuel Torres',
            'email': 'nefrologia@medicare.com',
            'username': 'drnefrologia',
            'password': 'doctor123',
            'especialidad': 'Nefrología',
            'telefono': '809-555-0115'
        },
        {
            'nombre': 'Dra. Claudia Ruiz',
            'email': 'reumatologia@medicare.com',
            'username': 'drreumatologia',
            'password': 'doctor123',
            'especialidad': 'Reumatología',
            'telefono': '809-555-0116'
        },
        {
            'nombre': 'Dr. Antonio Silva',
            'email': 'cirugiagral@medicare.com',
            'username': 'drcirugiagral',
            'password': 'doctor123',
            'especialidad': 'Cirugía General',
            'telefono': '809-555-0117'
        },
        {
            'nombre': 'Dra. Beatriz Morales',
            'email': 'alergologia@medicare.com',
            'username': 'dralergologia',
            'password': 'doctor123',
            'especialidad': 'Alergología',
            'telefono': '809-555-0118'
        },
        {
            'nombre': 'Dr. Fernando Castro',
            'email': 'otorrino@medicare.com',
            'username': 'drotorrino',
            'password': 'doctor123',
            'especialidad': 'Otorrinolaringología',
            'telefono': '809-555-0119'
        }
    ]
    
    try:
        for doctor in nuevos_doctores:
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
        print(f"\n ¡{len(nuevos_doctores)} doctores agregados exitosamente!")
        print("\n Resumen:")
        
        # Contar total de doctores
        total = c.execute('SELECT COUNT(*) FROM usuarios WHERE role = "doctor"').fetchone()[0]
        print(f"Total de doctores en el sistema: {total}")
        
        # Listar todas las especialidades
        especialidades = c.execute('''
            SELECT DISTINCT especialidad 
            FROM usuarios 
            WHERE role = "doctor" 
            ORDER BY especialidad
        ''').fetchall()
        
        print(f"\n Especialidades disponibles ({len(especialidades)}):")
        for i, (esp,) in enumerate(especialidades, 1):
            print(f"{i}. {esp}")
        
    except Exception as e:
        print(f" Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    print(" Agregando 9 doctores nuevos al sistema Medicare...")
    print("=" * 60)
    agregar_doctores()
