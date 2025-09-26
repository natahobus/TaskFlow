import unittest
import tempfile
import os
import json
from datetime import datetime
import sys
sys.path.append('..')
from utils import load_tasks, save_tasks, get_next_id, format_date

class TestUtils(unittest.TestCase):
    
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.test_file.close()
        
    def tearDown(self):
        if os.path.exists(self.test_file.name):
            os.unlink(self.test_file.name)
    
    def test_load_empty_tasks(self):
        """Testa carregamento de arquivo vazio"""
        tasks = load_tasks()
        self.assertEqual(tasks, [])
    
    def test_save_and_load_tasks(self):
        """Testa salvamento e carregamento de tarefas"""
        test_tasks = [
            {'id': 1, 'description': 'Teste', 'completed': False}
        ]
        
        # Temporariamente substitui o arquivo de tarefas
        import config
        original_file = config.TASKS_FILE
        config.TASKS_FILE = self.test_file.name
        
        save_tasks(test_tasks)
        loaded_tasks = load_tasks()
        
        config.TASKS_FILE = original_file
        
        self.assertEqual(loaded_tasks, test_tasks)
    
    def test_get_next_id(self):
        """Testa geração de próximo ID"""
        # Lista vazia
        self.assertEqual(get_next_id([]), 1)
        
        # Lista com tarefas
        tasks = [
            {'id': 1, 'description': 'Teste 1'},
            {'id': 3, 'description': 'Teste 3'},
            {'id': 2, 'description': 'Teste 2'}
        ]
        self.assertEqual(get_next_id(tasks), 4)
    
    def test_format_date(self):
        """Testa formatação de data"""
        date_str = "2024-01-15T10:30:00"
        formatted = format_date(date_str)
        self.assertIn("15/01/2024", formatted)
        
        # Data inválida
        invalid_formatted = format_date("data_invalida")
        self.assertEqual(invalid_formatted, "Data inválida")

if __name__ == '__main__':
    unittest.main()