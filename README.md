# TaskFlow CLI 🚀

Um gerenciador de tarefas moderno via linha de comando, construído em Python com interface rica e colorida.

## ✨ Funcionalidades

- ➕ **Adicionar tarefas** - Crie novas tarefas rapidamente
- 📝 **Listar tarefas** - Visualize todas as tarefas em uma tabela organizada
- ✅ **Marcar como concluída** - Complete tarefas por ID
- 🗑️ **Remover tarefas** - Delete tarefas específicas
- 🧹 **Limpar concluídas** - Remove todas as tarefas finalizadas
- 📊 **Estatísticas** - Veja métricas de produtividade
- 🎨 **Interface rica** - Cores e emojis para melhor experiência

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/natahobus/TaskFlow.git
cd TaskFlow
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Uso

### Comandos disponíveis:

```bash
# Adicionar uma nova tarefa
python taskflow.py add "Estudar Python"

# Listar todas as tarefas
python taskflow.py list

# Marcar tarefa como concluída
python taskflow.py complete 1

# Remover uma tarefa
python taskflow.py remove 1

# Ver estatísticas
python taskflow.py stats

# Limpar tarefas concluídas
python taskflow.py clear

# Ver versão
python taskflow.py version
```

## 📱 Exemplo de Uso

```bash
$ python taskflow.py add "Fazer exercícios"
✅ Tarefa adicionada: Fazer exercícios

$ python taskflow.py add "Ler um livro"
✅ Tarefa adicionada: Ler um livro

$ python taskflow.py list
                    Suas Tarefas                    
┌────┬──────────────────┬─────────────┐
│ ID │ Descrição        │ Status      │
├────┼──────────────────┼─────────────┤
│ 1  │ Fazer exercícios │ ⏳ Pendente │
│ 2  │ Ler um livro     │ ⏳ Pendente │
└────┴──────────────────┴─────────────┘

$ python taskflow.py complete 1
✅ Tarefa 1 marcada como concluída!

$ python taskflow.py stats
┌───────────── 📊 Estatísticas ─────────────┐
│ Total: 2                           │
│ Concluídas: 1                      │
│ Pendentes: 1                       │
│ Taxa de conclusão: 50.0%            │
└────────────────────────────────────┘
```

## 💾 Armazenamento

As tarefas são armazenadas em `~/.taskflow/tasks.json` no seu diretório home.

## 🛠️ Tecnologias

- **Python 3.7+**
- **Click** - Interface de linha de comando
- **Rich** - Interface rica com cores e tabelas
- **JSON** - Armazenamento de dados

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature
3. Fazer commit das mudanças
4. Fazer push para a branch
5. Abrir um Pull Request
