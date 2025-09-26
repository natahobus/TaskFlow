import os
from pathlib import Path

# Configurações do aplicativo
APP_NAME = "TaskFlow CLI"
VERSION = "1.0.0"

# Diretório de dados
DATA_DIR = Path.home() / ".taskflow"
TASKS_FILE = DATA_DIR / "tasks.json"
CONFIG_FILE = DATA_DIR / "config.json"

# Criar diretório se não existir
DATA_DIR.mkdir(exist_ok=True)

# Configurações padrão
DEFAULT_CONFIG = {
    "theme": "default",
    "auto_save": True,
    "show_timestamps": False
}