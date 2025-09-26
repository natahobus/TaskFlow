#!/usr/bin/env python3
import click
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from config import APP_NAME, VERSION
from utils import load_tasks, save_tasks, get_next_id

console = Console()

@click.group()
def cli():
    """TaskFlow - Gerenciador de tarefas via CLI 🚀"""
    pass

@cli.command()
@click.argument('description')
def add(description):
    """Adiciona uma nova tarefa"""
    tasks = load_tasks()
    task = {
        'id': get_next_id(tasks),
        'description': description,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    console.print(f"✅ Tarefa adicionada: {description}", style="green")

@cli.command()
def list():
    """Lista todas as tarefas"""
    tasks = load_tasks()
    if not tasks:
        console.print("📝 Nenhuma tarefa encontrada", style="yellow")
        return
    
    table = Table(title="Suas Tarefas")
    table.add_column("ID", style="cyan")
    table.add_column("Descrição", style="white")
    table.add_column("Status", style="green")
    
    for task in tasks:
        status = "✅ Concluída" if task['completed'] else "⏳ Pendente"
        table.add_row(str(task['id']), task['description'], status)
    
    console.print(table)

@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Marca uma tarefa como concluída"""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            console.print(f"✅ Tarefa {task_id} marcada como concluída!", style="green")
            return
    console.print(f"❌ Tarefa {task_id} não encontrada", style="red")

@cli.command()
@click.argument('task_id', type=int)
def remove(task_id):
    """Remove uma tarefa"""
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            removed_task = tasks.pop(i)
            save_tasks(tasks)
            console.print(f"🗑️ Tarefa removida: {removed_task['description']}", style="red")
            return
    console.print(f"❌ Tarefa {task_id} não encontrada", style="red")

@cli.command()
def stats():
    """Mostra estatísticas das tarefas"""
    tasks = load_tasks()
    if not tasks:
        console.print("📊 Nenhuma tarefa para mostrar estatísticas", style="yellow")
        return
    
    total = len(tasks)
    completed = sum(1 for task in tasks if task['completed'])
    pending = total - completed
    completion_rate = (completed / total) * 100 if total > 0 else 0
    
    stats_text = f"""Total: {total}
Concluídas: [green]{completed}[/green]
Pendentes: [yellow]{pending}[/yellow]
Taxa de conclusão: [cyan]{completion_rate:.1f}%[/cyan]"""
    
    panel = Panel(stats_text, title="📊 Estatísticas", border_style="blue")
    console.print(panel)

@cli.command()
def clear():
    """Remove todas as tarefas concluídas"""
    tasks = load_tasks()
    completed_tasks = [task for task in tasks if task['completed']]
    remaining_tasks = [task for task in tasks if not task['completed']]
    
    if not completed_tasks:
        console.print("🗑️ Nenhuma tarefa concluída para remover", style="yellow")
        return
    
    save_tasks(remaining_tasks)
    console.print(f"🗑️ {len(completed_tasks)} tarefa(s) concluída(s) removida(s)", style="green")

@cli.command()
def version():
    """Mostra a versão do aplicativo"""
    console.print(f"{APP_NAME} v{VERSION}", style="bold cyan")

if __name__ == '__main__':
    cli()