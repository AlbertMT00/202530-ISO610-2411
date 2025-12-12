#!/usr/bin/env python3
"""
Script para verificar y arreglar contraseñas de doctores
"""
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def arreglar_contraseñas():
    conn = sqlite3.connect('database/medicare.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # Lista de usuarios que deben tener doctor123
    usuarios_doctores = [
        'drcardiologia', 'drpediatria', 'drurologia', 'drgastroenterologia',
        'drneumologia', 'droncologia', 'drnefrologia', 'drreumatologia',
        'drcirugiagral', 'dralergologia', 'drotorrino', 'drneurologia2',
        'drtraumatologia2', 'drendocrinologia2', 'drmedicinainterna2',
        'drginecologia2', 'drdermatologia2', 'droftalmologia2', 'drpsiquiatria2'
    ]
    
    password_correcta = 'doctor123'
    password_hash = generate_password_hash(password_correcta)
    
    print(" Verificando contraseñas de doctores...\n")
    
    actualizados = 0
    correctos = 0
    
    for username in usuarios_doctores:
        # Verificar si existe
        doctor = c.execute('SELECT id, username, password FROM usuarios WHERE username = ?', 
                          (username,)).fetchone()
        
        if not doctor:
            print(f" {username} - NO EXISTE en la base de datos")
            continue
        
        # Verificar contraseña
        if check_password_hash(doctor['password'], password_correcta):
            print(f" {username} - Contraseña correcta")
            correctos += 1
        else:
            # Actualizar contraseña
            c.execute('UPDATE usuarios SET password = ? WHERE username = ?',
                     (password_hash, username))
            print(f" {username} - Contraseña actualizada")
            actualizados += 1
    
    conn.commit()
    
    print(f"\n Resumen:")
    print(f" Correctos: {correctos}")
    print(f" Actualizados: {actualizados}")
    print(f" No encontrados: {len(usuarios_doctores) - correctos - actualizados}")
    
    # Listar todos los doctores en la BD
    print(f"\n‍ Doctores en la base de datos:")
    doctores = c.execute('SELECT username, nombre, especialidad FROM usuarios WHERE role = "doctor" ORDER BY username').fetchall()
    for i, doc in enumerate(doctores, 1):
        print(f"{i:2d}. {doc['username']:25s} - {doc['nombre']:30s} ({doc['especialidad']})")
    
    conn.close()

if __name__ == '__main__':
    print(" Arreglando contraseñas de doctores...")
    print("=" * 70)
    arreglar_contraseñas()
