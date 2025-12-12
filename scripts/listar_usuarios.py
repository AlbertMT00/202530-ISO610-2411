#!/usr/bin/env python3
"""
Script para generar lista de usuarios con contraseñas
"""
import sqlite3

def listar_usuarios():
    conn = sqlite3.connect('database/medicare.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    print("=" * 80)
    print("LISTA COMPLETA DE USUARIOS - Medicare v4.3")
    print("=" * 80)
    
    # Admin
    print("\n ADMINISTRADOR")
    print("-" * 80)
    admin = c.execute('SELECT username, nombre FROM usuarios WHERE role = "admin"').fetchall()
    for a in admin:
        print(f"{a['username']:30s} / admin123")
    
    # Doctores
    print("\n‍ DOCTORES (19)")
    print("-" * 80)
    doctores = c.execute('''
        SELECT username, nombre, especialidad 
        FROM usuarios 
        WHERE role = "doctor" 
        ORDER BY username
    ''').fetchall()
    
    for i, doc in enumerate(doctores, 1):
        print(f"{i:2d}. {doc['username']:25s} / doctor123  - {doc['nombre']:30s} ({doc['especialidad']})")
    
    # Pacientes
    print("\n PACIENTES")
    print("-" * 80)
    pacientes = c.execute('SELECT username, nombre FROM usuarios WHERE role = "paciente" ORDER BY username').fetchall()
    for p in pacientes:
        print(f"{p['username']:30s} / paciente123  - {p['nombre']}")
    
    print("\n" + "=" * 80)
    print(f"TOTAL: 1 admin + {len(doctores)} doctores + {len(pacientes)} pacientes = {1 + len(doctores) + len(pacientes)}")
    print("=" * 80)
    
    # Generar archivo de texto
    with open('USUARIOS_ACTUALIZADOS.txt', 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("LISTA COMPLETA DE USUARIOS - Medicare v4.3\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("ADMIN:\n")
        f.write("admin / admin123\n\n")
        
        f.write("DOCTORES (19):\n")
        for doc in doctores:
            f.write(f"{doc['username']} / doctor123\n")
        
        f.write("\nPACIENTES:\n")
        for p in pacientes:
            f.write(f"{p['username']} / paciente123\n")
    
    print("\n Archivo generado: USUARIOS_ACTUALIZADOS.txt")
    
    conn.close()

if __name__ == '__main__':
    listar_usuarios()
