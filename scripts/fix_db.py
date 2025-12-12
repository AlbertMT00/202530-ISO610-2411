#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Solución Rápida - Medicare
Elimina la BD antigua y crea una nueva con la estructura correcta
"""

import os
import sys

DATABASE = 'database/medicare.db'

def main():
    print("=" * 70)
    print("  SOLUCIÓN RÁPIDA - Medicare v3.2")
    print("=" * 70)
    print()
    
    if os.path.exists(DATABASE):
        print(f" Base de datos encontrada: {DATABASE}")
        print()
        print("  ADVERTENCIA: Esto eliminará TODOS los datos existentes")
        print("   - Usuarios")
        print("   - Citas")
        print("   - Recetas")
        print("   - Urgencias")
        print()
        
        respuesta = input("¿Deseas continuar? (escribe 'SI' para confirmar): ")
        
        if respuesta.upper() == 'SI':
            try:
                os.remove(DATABASE)
                print()
                print(" Base de datos eliminada exitosamente")
                print()
                print("=" * 70)
                print("  SIGUIENTE PASO")
                print("=" * 70)
                print()
                print("Ejecuta:")
                print("  python app.py")
                print()
                print("Esto creará una nueva base de datos con:")
                print("   Estructura completa v3.2")
                print("   Usuario admin: admin / admin123")
                print("   10 doctores (uno por especialidad)")
                print("   3 pacientes de ejemplo")
                print("   Todas las columnas necesarias")
                print()
            except Exception as e:
                print(f" Error al eliminar: {e}")
                print()
                print("Intenta eliminarlo manualmente:")
                print(f"  del {DATABASE}")
        else:
            print()
            print("Operación cancelada.")
            print()
            print("Si el error persiste, elimina manualmente:")
            print(f"  del {DATABASE}")
            print()
            print("Y luego ejecuta:")
            print("  python app.py")
    else:
        print(" No hay base de datos existente")
        print()
        print("Ejecuta:")
        print("  python app.py")
        print()
        print("Para crear una nueva base de datos.")
    
    print("=" * 70)

if __name__ == '__main__':
    main()
