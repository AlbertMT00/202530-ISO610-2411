#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Migración de Base de Datos - Medicare
Este script actualiza la estructura de la base de datos sin perder datos existentes
"""

import sqlite3
import os

DATABASE = 'database/medicare.db'

def migrate_database():
    """Migra la base de datos a la última versión sin perder datos"""
    
    if not os.path.exists(DATABASE):
        print(" No se encontró la base de datos")
        print(" Se creará una nueva al ejecutar: python app.py")
        return
    
    print("=" * 60)
    print("  MIGRACIÓN DE BASE DE DATOS - Medicare v3.0")
    print("=" * 60)
    print()
    
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Verificar si ya tiene las columnas nuevas
        cursor.execute("PRAGMA table_info(usuarios)")
        columnas_existentes = [col[1] for col in cursor.fetchall()]
        
        print(f" Base de datos encontrada: {DATABASE}")
        print(f" Columnas actuales: {len(columnas_existentes)}")
        print()
        
        migraciones_aplicadas = 0
        
        # Migración 1: Agregar campo cedula
        if 'cedula' not in columnas_existentes:
            print(" Aplicando migración: Agregar campo 'cedula'")
            try:
                cursor.execute("ALTER TABLE usuarios ADD COLUMN cedula TEXT UNIQUE")
                conn.commit()
                print("   Campo 'cedula' agregado exitosamente")
                migraciones_aplicadas += 1
            except sqlite3.OperationalError as e:
                print(f"   Ya existe o error: {e}")
        else:
            print(" Campo 'cedula' ya existe")
        
        # Migración 2: Agregar campo foto_perfil
        if 'foto_perfil' not in columnas_existentes:
            print(" Aplicando migración: Agregar campo 'foto_perfil'")
            try:
                cursor.execute("ALTER TABLE usuarios ADD COLUMN foto_perfil TEXT DEFAULT 'default.png'")
                conn.commit()
                print("   Campo 'foto_perfil' agregado exitosamente")
                migraciones_aplicadas += 1
            except sqlite3.OperationalError as e:
                print(f"   Ya existe o error: {e}")
        else:
            print(" Campo 'foto_perfil' ya existe")
        
        # Migración 3: Agregar campo estado_doctor
        if 'estado_doctor' not in columnas_existentes:
            print(" Aplicando migración: Agregar campo 'estado_doctor'")
            try:
                cursor.execute("ALTER TABLE usuarios ADD COLUMN estado_doctor TEXT DEFAULT 'disponible'")
                conn.commit()
                print("   Campo 'estado_doctor' agregado exitosamente")
                migraciones_aplicadas += 1
            except sqlite3.OperationalError as e:
                print(f"   Ya existe o error: {e}")
        else:
            print(" Campo 'estado_doctor' ya existe")
        
        # Migración 4: Agregar campo hora_inicio
        if 'hora_inicio' not in columnas_existentes:
            print(" Aplicando migración: Agregar campo 'hora_inicio'")
            try:
                cursor.execute("ALTER TABLE usuarios ADD COLUMN hora_inicio TEXT DEFAULT '08:00'")
                conn.commit()
                print("   Campo 'hora_inicio' agregado exitosamente")
                migraciones_aplicadas += 1
            except sqlite3.OperationalError as e:
                print(f"   Ya existe o error: {e}")
        else:
            print(" Campo 'hora_inicio' ya existe")
        
        # Migración 5: Agregar campo hora_fin
        if 'hora_fin' not in columnas_existentes:
            print(" Aplicando migración: Agregar campo 'hora_fin'")
            try:
                cursor.execute("ALTER TABLE usuarios ADD COLUMN hora_fin TEXT DEFAULT '17:00'")
                conn.commit()
                print("   Campo 'hora_fin' agregado exitosamente")
                migraciones_aplicadas += 1
            except sqlite3.OperationalError as e:
                print(f"   Ya existe o error: {e}")
        else:
            print(" Campo 'hora_fin' ya existe")
        
        # Verificar columnas después de la migración
        cursor.execute("PRAGMA table_info(usuarios)")
        columnas_nuevas = [col[1] for col in cursor.fetchall()]
        
        # Verificar tabla citas
        try:
            cursor.execute("PRAGMA table_info(citas)")
            columnas_citas = [col[1] for col in cursor.fetchall()]
            
            # Verificar si citas tiene el campo 'servicio' (antiguo)
            if 'servicio' in columnas_citas and 'especialidad' not in columnas_citas:
                print()
                print(" Detectado campo antiguo 'servicio' en tabla citas")
                print("   Se requiere recrear la tabla citas")
                print("   Esto eliminará las citas existentes")
                
                respuesta = input("  ¿Deseas continuar? (s/n): ")
                if respuesta.lower() == 's':
                    cursor.execute("DROP TABLE IF EXISTS citas")
                    cursor.execute('''CREATE TABLE citas (
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
                    conn.commit()
                    print("   Tabla citas recreada exitosamente")
                    migraciones_aplicadas += 1
        except:
            pass
        
        conn.close()
        
        print()
        print("=" * 60)
        print(f" Migración completada exitosamente")
        print(f" Total de cambios aplicados: {migraciones_aplicadas}")
        print(f" Columnas actuales: {len(columnas_nuevas)}")
        print()
        print("Columnas en la tabla usuarios:")
        for col in columnas_nuevas:
            print(f"  - {col}")
        print()
        print(" Puedes iniciar la aplicación: python app.py")
        print("=" * 60)
        
    except Exception as e:
        print(f" Error durante la migración: {e}")
        print()
        print("Solución alternativa:")
        print("  1. Haz backup de tu base de datos:")
        print("     copy database\\medicare.db database\\medicare_backup.db")
        print("  2. Elimina la base de datos:")
        print("     del database\\medicare.db")
        print("  3. Ejecuta la aplicación:")
        print("     python app.py")

if __name__ == '__main__':
    migrate_database()
