#!/usr/bin/env python3
import click
import json
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@click.group()
def cli():
    """TaskFlow - Gerenciador de tarefas via CLI"""
    pass

@cli.command()
@click.argument('description')
def add(description):
    """Adiciona uma nova tarefa"""
    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    console.print(f"✅ Tarefa adicionada: {description}", style="green")

if __name__ == '__main__':
    cli()