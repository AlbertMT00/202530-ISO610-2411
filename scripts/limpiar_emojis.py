#!/usr/bin/env python3
"""
Script para eliminar emojis de todos los archivos del proyecto
"""
import os
import re

def remove_emojis(text):
    """Elimina emojis del texto"""
    # Lista de emojis comunes en el proyecto
    emojis = ['', '', '', '', '', '', '', '', '', '', '', '', 
              '', '', '', '', '', '', '', '', '', '', '', 
              '', '', '', '', '', '', '', '', '', '']
    
    for emoji in emojis:
        text = text.replace(emoji, '')
    
    # Remover emojis usando regex (cualquier carácter emoji Unicode)
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(r'', text)

def clean_file(filepath):
    """Limpia emojis de un archivo"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = remove_emojis(content)
        
        # Solo escribir si hubo cambios
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"Error procesando {filepath}: {e}")
    return False

def main():
    # Directorios a limpiar
    directories = ['templates', 'docs', 'scripts']
    files_to_clean = ['README.md', 'app.py']
    
    total_cleaned = 0
    
    # Limpiar directorios
    for directory in directories:
        if os.path.exists(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(('.html', '.py', '.md', '.txt')):
                        filepath = os.path.join(root, file)
                        if clean_file(filepath):
                            print(f" Limpiado: {filepath}")
                            total_cleaned += 1
    
    # Limpiar archivos específicos
    for file in files_to_clean:
        if os.path.exists(file):
            if clean_file(file):
                print(f" Limpiado: {file}")
                total_cleaned += 1
    
    print(f"\n{total_cleaned} archivos limpiados de emojis")

if __name__ == '__main__':
    main()
