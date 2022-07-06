import os 
from pathlib import Path


DIRETÓRIOS = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGENS": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heic"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTOS": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp", ".pdf", ".tex", ".txt", ".md", ".xml"],
    "AUDIO": [".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a"],
    "ARQUIVOS": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".z", ".deb", ".rpm", ".exe", ".msi", ".bin", ".iso", ".dmg"],
    "OUTROS": [".exe", ".msi", ".bin", ".iso", ".dmg", ".dll", ".deb", ".msp", ".vb", ".bat", ".cmd", ".c", ".class", ".cpp", ".cs", ".h", ".hpp", ".js", ".json", ".pl", ".sh", ".swift", ".vbscript", ".wsf", ".wsh", ".xml", ".yml", ".yaml"]
}

FILE_FORMATS = {file_format: directory 
                for directory, file_formats in DIRETÓRIOS.items() 
                for file_format in file_formats}

def file_organizer():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(parents=True, exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

        for dir in os.scandir():
            try: 
                os.rmdir(dir)
            except:
                pass

if __name__ == "__main__":
    file_organizer()