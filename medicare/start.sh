#!/bin/bash

echo "==================================="
echo "  Sistema Medicare - Iniciando..."
echo "==================================="
echo ""

# Crear directorio de base de datos si no existe
mkdir -p database

# Iniciar aplicación
echo "🚀 Iniciando servidor Flask..."
echo "📍 Accede a: http://localhost:5000"
echo ""
echo "👤 Usuarios de prueba:"
echo "   Admin: admin / admin123"
echo "   Doctor: drmartinez / doctor123"
echo "   Paciente: mariagonzalez / paciente123"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo "==================================="
echo ""

python app.py
