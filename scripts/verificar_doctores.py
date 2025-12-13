#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para Verificar y Agregar Doctores Faltantes
"""

import sqlite3
import os
from werkzeug.security import generate_password_hash

DATABASE = 'database/medicare.db'

def verificar_y_agregar_doctores():
    print("=" * 70)
    print("  VERIFICACIÓN DE DOCTORES - Medicare")
    print("=" * 70)
    print()
    
    if not os.path.exists(DATABASE):
        print(" No se encontró la base de datos")
        print(" Ejecuta: python app.py para crear la base de datos")
        return
    
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # Verificar doctores existentes
    c.execute("SELECT username, nombre, especialidad FROM usuarios WHERE role = 'doctor'")
    doctores_existentes = c.fetchall()
    
    print(f" Doctores actuales en la base de datos: {len(doctores_existentes)}")
    print()
    
    if doctores_existentes:
        print("Doctores encontrados:")
        for i, doc in enumerate(doctores_existentes, 1):
            print(f"  {i}. {doc['nombre']} ({doc['username']}) - {doc['especialidad']}")
        print()
    
    # Doctores que deberían existir
    doctores_requeridos = [
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
    
    # Obtener usernames existentes
    usernames_existentes = [doc['username'] for doc in doctores_existentes]
    
    # Encontrar doctores faltantes
    doctores_faltantes = []
    for doctor in doctores_requeridos:
        if doctor[2] not in usernames_existentes:  # doctor[2] es el username
            doctores_faltantes.append(doctor)
    
    if not doctores_faltantes:
        print(" TODOS LOS DOCTORES ESTÁN EN LA BASE DE DATOS")
        print(" Total: 10 doctores (uno por especialidad)")
    else:
        print(f"  Faltan {len(doctores_faltantes)} doctores:")
        print()
        for doc in doctores_faltantes:
            print(f"  - {doc[0]} ({doc[3]})")
        print()
        
        respuesta = input("¿Deseas agregar los doctores faltantes? (s/n): ")
        
        if respuesta.lower() == 's':
            doctor_password = generate_password_hash('doctor123')
            agregados = 0
            
            for nombre, email, username, especialidad, telefono, cedula in doctores_faltantes:
                try:
                    c.execute('''INSERT INTO usuarios (nombre, email, username, password, role, especialidad, telefono, cedula)
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                              (nombre, email, username, doctor_password, 'doctor', especialidad, telefono, cedula))
                    conn.commit()
                    print(f"   {nombre} agregado")
                    agregados += 1
                except sqlite3.IntegrityError as e:
                    print(f"   {nombre} - Error: {e}")
            
            print()
            print(f" {agregados} doctores agregados exitosamente")
            print()
            
            # Verificar de nuevo
            c.execute("SELECT COUNT(*) as total FROM usuarios WHERE role = 'doctor'")
            total = c.fetchone()['total']
            print(f" Total de doctores ahora: {total}")
    
    conn.close()
    print()
    print("=" * 70)

if __name__ == '__main__':
    verificar_y_agregar_doctores()
