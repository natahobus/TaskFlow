import json
import os
from datetime import datetime
from config import TASKS_FILE

def load_tasks():
    """Carrega tarefas do arquivo JSON"""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_tasks(tasks):
    """Salva tarefas no arquivo JSON"""
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def get_next_id(tasks):
    """Retorna o próximo ID disponível"""
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def format_date(date_string):
    """Formata data para exibição"""
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%d/%m/%Y %H:%M")
    except:
        return "Data inválida"