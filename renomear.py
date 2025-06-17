import os
import mutagen
from mutagen.id3 import ID3
import re

def sanitize_filename(name):
    """Remove caracteres inválidos para nomes de arquivos."""
    return re.sub(r'[<>:"/\\|?*]', '', name).strip()

def rename_music_files(folder_path):
    """Renomeia arquivos de música na pasta usando metadados."""
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.mp3'):
            file_path = os.path.join(folder_path, filename)
            try:
                audio = ID3(file_path)
                artist = audio.get('TPE1', ['Desconhecido'])[0]
                title = audio.get('TIT2', ['Sem Título'])[0]
                
                artist = sanitize_filename(artist)
                title = sanitize_filename(title)
                
                new_filename = f"{artist} - {title}.mp3"
                new_file_path = os.path.join(folder_path, new_filename)
                
                os.rename(file_path, new_file_path)
                print(f"Renomeado: {filename} -> {new_filename}")
                
            except Exception as e:
                print(f"Erro ao processar {filename}: {e}")

if __name__ == "__main__":
    folder = os.path.dirname(os.path.abspath(__file__))
    print(f"Processando arquivos na pasta: {folder}")
    rename_music_files(folder)