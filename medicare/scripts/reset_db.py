#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para resetear la base de datos de Medicare
Ejecutar este script si hay errores con la estructura de la base de datos
"""

import os
import sqlite3

DATABASE = 'database/medicare.db'

print("=" * 60)
print("  RESETEAR BASE DE DATOS - Sistema Medicare")
print("=" * 60)
print()

if os.path.exists(DATABASE):
    print(f" Base de datos encontrada: {DATABASE}")
    respuesta = input("¿Deseas eliminarla y crear una nueva? (s/n): ")
    
    if respuesta.lower() == 's':
        os.remove(DATABASE)
        print(" Base de datos eliminada")
        print(" La nueva base de datos se creará al iniciar la aplicación")
        print()
        print("Ahora ejecuta: python app.py")
    else:
        print(" Operación cancelada")
else:
    print(" No se encontró base de datos existente")
    print(" Se creará una nueva al ejecutar: python app.py")

print()
print("=" * 60)
